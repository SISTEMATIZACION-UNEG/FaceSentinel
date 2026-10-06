/**
 * useBlinkDetector.ts
 *
 * Detects eye blinks locally using MediaPipe FaceLandmarker (WASM) at ~30 FPS.
 * Computes EAR (Eye Aspect Ratio) frame-by-frame and fires onBlink() with the
 * current frame as base64 JPEG when a complete close->open cycle is detected.
 */

import { useEffect, useRef, useCallback } from "react"
import { FaceLandmarker, FilesetResolver } from "@mediapipe/tasks-vision"

// Same landmark indices as the Python backend
const LEFT_EYE  = [33, 160, 158, 133, 153, 144]
const RIGHT_EYE = [362, 385, 387, 263, 373, 380]

function euclidean(a: { x: number; y: number }, b: { x: number; y: number }): number {
  return Math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)
}

function computeEAR(
  landmarks: Array<{ x: number; y: number; z: number }>,
  indices: number[]
): number {
  const [p1, p2, p3, p4, p5, p6] = indices.map((i) => landmarks[i])
  const v1 = euclidean(p2, p6)
  const v2 = euclidean(p3, p5)
  const h  = euclidean(p1, p4)
  return (v1 + v2) / (2.0 * h)
}

export interface BlinkDetectorOptions {
  videoEl: HTMLVideoElement | null
  canvasEl: HTMLCanvasElement | null
  earThreshold?: number
  openThreshold?: number
  onBlink: (imageBase64: string, ear: number) => void
  onEarUpdate?: (ear: number) => void
  active: boolean
}

export function useBlinkDetector({
  videoEl,
  canvasEl,
  earThreshold = 0.24,
  openThreshold = 0.27,
  onBlink,
  onEarUpdate,
  active,
}: BlinkDetectorOptions): void {
  const landmarkerRef  = useRef<FaceLandmarker | null>(null)
  const rafRef         = useRef<number | null>(null)
  const lastVideoTime  = useRef<number>(-1)
  const frameCounter   = useRef<number>(0)
  const blinkFiredRef  = useRef<boolean>(false)
  const activeRef      = useRef<boolean>(active)

  useEffect(() => { activeRef.current = active }, [active])

  // Initialize FaceLandmarker once
  useEffect(() => {
    let cancelled = false
    async function init() {
      try {
        const vision = await FilesetResolver.forVisionTasks(
          "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@latest/wasm"
        )
        const fl = await FaceLandmarker.createFromOptions(vision, {
          baseOptions: {
            modelAssetPath:
              "https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/1/face_landmarker.task",
            delegate: "GPU",
          },
          runningMode: "VIDEO",
          numFaces: 1,
          minFaceDetectionConfidence: 0.35,
          minFacePresenceConfidence: 0.35,
          minTrackingConfidence: 0.35,
          outputFaceBlendshapes: false,
        })
        if (!cancelled) {
          landmarkerRef.current = fl
          console.log("[BlinkDetector] FaceLandmarker loaded")
        }
      } catch (err) {
        console.warn("[BlinkDetector] init failed:", err)
      }
    }
    init()
    return () => {
      cancelled = true
      landmarkerRef.current?.close()
      landmarkerRef.current = null
    }
  }, [])

  const captureFrame = useCallback((): string | null => {
    if (!videoEl || !canvasEl || videoEl.videoWidth === 0) return null
    canvasEl.width  = videoEl.videoWidth
    canvasEl.height = videoEl.videoHeight
    const ctx = canvasEl.getContext("2d")
    if (!ctx) return null
    ctx.drawImage(videoEl, 0, 0)
    return canvasEl.toDataURL("image/jpeg", 0.7).replace(/^data:image\/[a-z]+;base64,/, "")
  }, [videoEl, canvasEl])

  // RAF detection loop
  useEffect(() => {
    if (!active || !videoEl || !canvasEl) return

    function tick() {
      if (!activeRef.current) return
      const fl  = landmarkerRef.current
      const vid = videoEl!

      if (fl && vid.readyState >= 2 && vid.currentTime !== lastVideoTime.current) {
        lastVideoTime.current = vid.currentTime
        try {
          const result = fl.detectForVideo(vid, performance.now())
          const lms    = result.faceLandmarks?.[0]

          if (lms && lms.length >= 468) {
            const ear = ((computeEAR(lms, LEFT_EYE) + computeEAR(lms, RIGHT_EYE)) / 2)
            onEarUpdate?.(ear)

            if (ear < earThreshold) {
              frameCounter.current++
              blinkFiredRef.current = false
            } else if (ear >= openThreshold) {
              if (frameCounter.current >= 1 && !blinkFiredRef.current) {
                const b64 = captureFrame()
                if (b64) {
                  blinkFiredRef.current = true
                  onBlink(b64, ear)
                }
              }
              frameCounter.current = 0
            }
          }
        } catch { /* swallow per-frame errors */ }
      }

      rafRef.current = requestAnimationFrame(tick)
    }

    rafRef.current = requestAnimationFrame(tick)
    return () => {
      if (rafRef.current !== null) cancelAnimationFrame(rafRef.current)
      frameCounter.current  = 0
      blinkFiredRef.current = false
      lastVideoTime.current = -1
    }
  }, [active, videoEl, canvasEl, earThreshold, openThreshold, onBlink, onEarUpdate, captureFrame])
}

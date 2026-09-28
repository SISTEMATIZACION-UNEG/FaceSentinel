import asyncio
import websockets

async def run_ws_check():
    url = "ws://127.0.0.1:8000/api/v1/ws/liveness?client_id=APP_PRUEBA_123"
    try:
        async with websockets.connect(url) as ws:
            print("Successfully connected!")
            await ws.send('{"image_base64": ""}')
            res = await ws.recv()
            print("Received:", res)
    except Exception as e:
        print("Failed to connect:", e)

if __name__ == "__main__":
    asyncio.run(run_ws_check())

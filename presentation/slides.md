---
theme: default
class: cover-slide
highlighter: shiki
lineNumbers: false
drawings:
  persist: false
transition: slide-left
title: "Portada Principal"
mdc: true
---

<!-- Slide 1: Portada Principal con Membrete Oficial y Estilo Canva / UNEG -->
<div class="h-full w-full flex flex-col justify-between py-6 px-10 relative overflow-hidden bg-white">
<svg class="absolute inset-0 w-full h-full pointer-events-none z-0" viewBox="0 0 980 550" preserveAspectRatio="none" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M 640 0 C 700 90, 770 140, 980 180 L 980 0 Z" fill="#97c8eb" />
  <path d="M 760 0 C 790 70, 840 105, 980 140 L 980 0 Z" fill="#1b4d89" />
  <path d="M 0 320 C 60 350, 110 410, 150 470 C 180 515, 230 535, 300 550 L 0 550 Z" fill="#97c8eb" />
  <path d="M 0 460 C 60 465, 110 500, 150 550 L 0 550 Z" fill="#3b77a8" />
  <path d="M 0 480 C 40 480, 80 515, 100 550 L 0 550 Z" fill="#1b4d89" />
  <circle cx="518" cy="38" r="6.5" fill="#97c8eb" />
  <circle cx="616" cy="46" r="10" fill="#1b4d89" />
  <circle cx="835" cy="128" r="6" fill="#97c8eb" />
  <circle cx="968" cy="225" r="7.5" fill="#1b4d89" />
  <circle cx="32" cy="320" r="8" fill="#1b4d89" />
  <circle cx="120" cy="445" r="5.5" fill="#97c8eb" />
  <circle cx="370" cy="505" r="9" fill="#1b4d89" />
  <circle cx="470" cy="518" r="5.5" fill="#97c8eb" />
</svg>
<div class="flex items-center justify-center gap-6 relative z-10 pt-1 px-4">
  <img src="/diagrams/uneg logo.png" alt="Logo UNEG" class="h-15 w-auto object-contain drop-shadow-sm" />
  <div class="text-center font-bold text-[#1b365d] leading-tight">
    <span class="text-[12px] uppercase tracking-wider block font-black">UNIVERSIDAD NACIONAL EXPERIMENTAL DE GUAYANA</span>
    <span class="text-[11px] uppercase tracking-wide block font-bold">VICERRECTORADO ACADÉMICO</span>
    <span class="text-[11px] uppercase tracking-wide block font-bold">COORDINACIÓN GENERAL DE PREGRADO</span>
    <span class="text-[11px] uppercase tracking-wide block font-black text-[#1b365d]">PROYECTO DE CARRERA: INGENIERÍA EN INFORMÁTICA</span>
  </div>
</div>
<div class="my-auto text-center px-8 max-w-3xl mx-auto relative z-10">
  <div class="cover-title">
    SISTEMA PROVEEDOR DE IDENTIDAD (IDP) CIBERFÍSICO BASADO EN<br>
    AUTENTICACIÓN BIOMÉTRICA FACIAL ANTI-SPOOFING Y REGISTRO<br>
    INMUTABLE EN BLOCKCHAIN PARA LA GESTIÓN UNIFICADA DE CONTROL DE ACCESO
  </div>
</div>
<div class="relative z-10 pb-2 px-8">
  <div class="flex justify-between items-end text-xs font-semibold text-[#1b365d]">
    <div class="text-left leading-tight">
      <span class="font-bold text-[#1b365d] block text-[12px]">Tutor academico</span>
      <span class="block text-slate-800 font-bold text-[12px] mt-0.5">Ing. Livia Borjas</span>
      <span class="text-[11px] text-slate-600 block font-normal">C.I: V-10.928.181</span>
    </div>
    <div class="text-center text-[12px] text-[#1b365d] font-bold pb-0.5">
      Ciudad Guayana, Septiembre 2026.
    </div>
    <div class="text-right leading-tight">
      <span class="font-bold text-[#1b365d] block text-[12px]">Autor:</span>
      <span class="block text-slate-800 font-bold text-[12px] mt-0.5">Br. Héctor Tovar</span>
      <span class="text-[11px] text-slate-600 block font-normal">C.I: V-30.335.783</span>
    </div>
  </div>
</div>
</div>

<!-- 
Buenas tardes a los honorables miembros del jurado y tutora. Hoy presento el resultado de mi Trabajo de Grado titulado SISTEMA PROVEEDOR DE IDENTIDAD (IDP) CIBERFÍSICO BASADO EN AUTENTICACIÓN BIOMÉTRICA FACIAL ANTI-SPOOFING Y REGISTRO INMUTABLE EN BLOCKCHAIN PARA LA GESTIÓN UNIFICADA DE CONTROL DE ACCESO, una solución diseñada para modernizar la infraestructura de seguridad lógica y física.
-->

---
layout: default
title: "Introducción al Escenario"
---

<!-- Slide 2: Introducción -->
<div class="h-full flex flex-col justify-between">
<div>
<div class="flex items-center justify-between mb-2">
<span class="badge-tag">Contexto</span>
<span class="text-xs text-sky-700 font-mono font-bold">02 / 19</span>
</div>
<h1 class="text-3xl font-extrabold text-slate-900">Introducción al Escenario Actual</h1>
<p class="text-sm text-sky-800 mt-1 font-medium">Desconexión crítica entre accesos físicos y seguridad lógica.</p>
</div>

<div class="grid grid-cols-3 gap-6 my-auto">
<div class="card-light card-light-hover p-6 text-center flex flex-col items-center">
<div class="icon-box icon-box-red mb-4">
<carbon:password class="text-2xl" />
</div>
<h3 class="text-base font-bold text-slate-900 mb-1">Sistemas Vulnerables</h3>
<span class="badge-tag badge-tag-red mb-2 text-[10px]">Contraseñas y Carnets</span>
<p class="text-xs text-slate-600 m-0">Credenciales compartidas y tarjetas clonables sin confirmación identitaria real.</p>
</div>

<div class="card-light card-light-hover p-6 text-center flex flex-col items-center">
<div class="icon-box icon-box-amber mb-4">
<carbon:face-mask class="text-2xl" />
</div>
<h3 class="text-base font-bold text-slate-900 mb-1">El Reto Biométrico</h3>
<span class="badge-tag badge-tag-amber mb-2 text-[10px]">Ataques de Spoofing</span>
<p class="text-xs text-slate-600 m-0">Suplantación mediante fotos impresas, pantallas 2D o reproducción de videos.</p>
</div>

<div class="card-light card-light-hover p-6 text-center flex flex-col items-center border-sky-300 bg-sky-50/40">
<div class="icon-box icon-box-navy mb-4">
<carbon:security class="text-2xl" />
</div>
<h3 class="text-base font-bold text-slate-900 mb-1">Solución FaceSentinel</h3>
<span class="badge-tag badge-tag-navy mb-2 text-[10px]">IdP Ciberfísico</span>
<p class="text-xs text-slate-700 m-0 font-medium">Unificación de Edge Computing, Inteligencia Artificial y Registro Blockchain.</p>
</div>
</div>

<div class="card-light px-4 py-2.5 flex items-center justify-between text-xs text-slate-600 font-medium bg-slate-50/80">
<span>🔒 Paradigma Zero-Trust</span>
<span>⚡ Procesamiento Perimetral</span>
<span>⛓️ Trazabilidad Criptográfica Inmutable</span>
</div>
</div>

<!-- 
La seguridad en los entornos institucionales está fragmentada en silos. El acceso físico depende de tarjetas clonables y cámaras pasivas, mientras que el lógico depende de contraseñas vulnerables. Aunque la biometría facial resuelve parte del problema, introduce el riesgo de ataques de suplantación. Este proyecto nace para unificar y blindar ambos mundos.
-->

---
layout: center
class: text-center
title: "Capítulo I: El Problema"
---

<!-- Slide 3: Capítulo I Separator -->
<div class="py-12 px-14 card-light-featured max-w-xl mx-auto text-center border-sky-300">
<div class="badge-tag mb-3">
Diagnóstico
</div>
<h1 class="text-5xl font-black text-slate-900 tracking-tight mb-2">
CAPÍTULO I
</h1>
<div class="w-20 h-1 bg-sky-500 mx-auto my-3 rounded-full"></div>
<h2 class="text-xl font-bold text-sky-800">
EL PROBLEMA Y JUSTIFICACIÓN
</h2>
</div>

<!-- 
(Transición al Capítulo I)
-->

---
layout: default
title: "Planteamiento del Problema"
---

<!-- Slide 4: El Problema -->
<div class="h-full flex flex-col justify-between">
<div>
<div class="flex items-center justify-between mb-2">
<span class="badge-tag">Diagnóstico</span>
<span class="text-xs text-sky-700 font-mono font-bold">04 / 19</span>
</div>
<h1 class="text-3xl font-extrabold text-slate-900">El Problema</h1>
<p class="text-sm text-sky-800 mt-1 font-medium">Puntos críticos en los esquemas de seguridad convencionales.</p>
</div>

<div class="flex flex-col gap-3.5 my-auto">
<div class="card-light card-light-hover p-4 flex items-center gap-4">
<div class="icon-box icon-box-red">
<carbon:identification class="text-2xl" />
</div>
<div class="flex-1">
<div class="flex items-center justify-between">
<h3 class="text-base font-bold text-slate-900 m-0">Credenciales Inseguras</h3>
<span class="text-[10px] font-bold text-red-700 bg-red-100 px-2 py-0.5 rounded border border-red-200 uppercase">Suplantación Física</span>
</div>
<p class="text-xs text-slate-600 m-0 mt-1">Préstamo de tarjetas, carnets extraviados y ausencia de verificación biométrica en vivo.</p>
</div>
</div>

<div class="card-light card-light-hover p-4 flex items-center gap-4">
<div class="icon-box icon-box-amber">
<carbon:video class="text-2xl" />
</div>
<div class="flex-1">
<div class="flex items-center justify-between">
<h3 class="text-base font-bold text-slate-900 m-0">Vigilancia CCTV Pasiva</h3>
<span class="text-[10px] font-bold text-amber-700 bg-amber-100 px-2 py-0.5 rounded border border-amber-200 uppercase">Sin Inteligencia</span>
</div>
<p class="text-xs text-slate-600 m-0 mt-1">Cámaras que solo graban para análisis forense post-evento sin capacidad de acción preventiva.</p>
</div>
</div>

<div class="card-light card-light-hover p-4 flex items-center gap-4">
<div class="icon-box icon-box-navy">
<carbon:data-base class="text-2xl" />
</div>
<div class="flex-1">
<div class="flex items-center justify-between">
<h3 class="text-base font-bold text-slate-900 m-0">Bitácoras Centralizadas (SPOF)</h3>
<span class="text-[10px] font-bold text-sky-800 bg-sky-100 px-2 py-0.5 rounded border border-sky-300 uppercase">Riesgo de Datos</span>
</div>
<p class="text-xs text-slate-600 m-0 mt-1">Bases de datos manipulables internamente y vulnerables a caídas de red total.</p>
</div>
</div>
</div>

<div class="text-right text-xs text-slate-500 font-medium">
Diagnóstico operacional en entornos universitarios y corporativos
</div>
</div>

<!-- 
El problema radica en que los controles físicos actúan como barreras aisladas, las cámaras solo sirven como registro forense post-incidente, y las bitácoras tradicionales son puntos únicos de falla que pueden ser manipulados desde adentro de la institución.
-->

---
layout: two-cols
title: "Objetivos del Proyecto"
---

<!-- Slide 5: Objetivos del Proyecto -->
<div class="h-full flex flex-col justify-between pr-4">
<div>
<div class="badge-tag mb-2">Alcance</div>
<h1 class="text-2xl font-extrabold text-slate-900">Objetivos</h1>
</div>

<div class="card-light-featured p-6 text-center my-auto flex flex-col items-center">
<div class="w-20 h-20 rounded-2xl bg-sky-100 border-2 border-sky-400 flex items-center justify-center text-sky-700 shadow-sm mb-3">
<carbon:target class="text-4xl" />
</div>
<span class="badge-tag badge-tag-navy mb-2">Objetivo General</span>
<p class="text-xs text-slate-800 leading-relaxed font-bold m-0">
Desarrollar un IdP ciberfísico con biometría facial anti-spoofing y registro inmutable en Blockchain.
</p>
</div>

<div class="text-[11px] text-sky-700 font-bold">
6 fases metodológicas completadas
</div>
</div>

::right::

<div class="h-full flex flex-col justify-between pl-2">
<div>
<span class="text-xs font-bold text-sky-700 uppercase tracking-wider block mb-1">Específicos</span>
<h3 class="text-base font-bold text-slate-900 mb-2">Objetivos Específicos</h3>
</div>

<div class="space-y-2 text-xs">
<div class="card-light p-2.5 flex items-center gap-3 border-l-4 border-sky-500">
<span class="w-5 h-5 rounded-full bg-sky-200 text-sky-900 font-bold flex items-center justify-center text-[10px]">1</span>
<span class="text-slate-800 font-medium">Analizar protocolos ópticos de video en tiempo real (RTSP).</span>
</div>

<div class="card-light p-2.5 flex items-center gap-3 border-l-4 border-sky-500">
<span class="w-5 h-5 rounded-full bg-sky-200 text-sky-900 font-bold flex items-center justify-center text-[10px]">2</span>
<span class="text-slate-800 font-medium">Diseñar arquitectura ciberfísica con procesamiento Edge.</span>
</div>

<div class="card-light p-2.5 flex items-center gap-3 border-l-4 border-sky-500">
<span class="w-5 h-5 rounded-full bg-sky-200 text-sky-900 font-bold flex items-center justify-center text-[10px]">3</span>
<span class="text-slate-800 font-medium">Desarrollar embudo Anti-Spoofing de 4 niveles (Liveness).</span>
</div>

<div class="card-light p-2.5 flex items-center gap-3 border-l-4 border-sky-500">
<span class="w-5 h-5 rounded-full bg-sky-200 text-sky-900 font-bold flex items-center justify-center text-[10px]">4</span>
<span class="text-slate-800 font-medium">Implementar Smart Contract en Solidity sobre red Ethereum.</span>
</div>

<div class="card-light p-2.5 flex items-center gap-3 border-l-4 border-sky-500">
<span class="w-5 h-5 rounded-full bg-sky-200 text-sky-900 font-bold flex items-center justify-center text-[10px]">5</span>
<span class="text-slate-800 font-medium">Integrar API RESTful centralizada con protocolo SSO.</span>
</div>

<div class="card-light p-2.5 flex items-center gap-3 border-l-4 border-sky-500">
<span class="w-5 h-5 rounded-full bg-sky-200 text-sky-900 font-bold flex items-center justify-center text-[10px]">6</span>
<span class="text-slate-800 font-medium">Validar rendimiento y seguridad bajo 421 ensayos empíricos.</span>
</div>
</div>

<div class="text-right text-[11px] text-emerald-700 font-bold">
✓ Cumplimiento: 100%
</div>
</div>

<!-- 
Nuestro norte fue crear un Proveedor de Identidad. Para ello, cumplimos seis fases: analizar cómo conectar las cámaras, diseñar la arquitectura en el borde, programar la IA anti-fraudes, escribir el contrato inteligente para la auditoría, empaquetarlo en una API y, finalmente, someterlo a pruebas de estrés.
-->

---
layout: default
title: "Justificación del Proyecto"
---

<!-- Slide 6: Justificación -->
<div class="h-full flex flex-col justify-between">
<div>
<div class="flex items-center justify-between mb-2">
<span class="badge-tag">Justificación</span>
<span class="text-xs text-sky-700 font-mono font-bold">06 / 19</span>
</div>
<h1 class="text-3xl font-extrabold text-slate-900">Justificación del Proyecto</h1>
</div>

<div class="grid grid-cols-2 gap-4 my-auto">
<div class="card-light p-4 flex items-start gap-3">
<div class="icon-box">
<carbon:machine-learning class="text-2xl" />
</div>
<div>
<h3 class="text-sm font-bold text-slate-900 m-0">Tecnológica</h3>
<p class="text-xs text-slate-600 m-0 mt-1">Visión computacional profunda con embeddings ArcFace y Edge Computing perimetral.</p>
</div>
</div>

<div class="card-light p-4 flex items-start gap-3">
<div class="icon-box icon-box-emerald">
<carbon:finance class="text-2xl" />
</div>
<div>
<h3 class="text-sm font-bold text-slate-900 m-0">Económica</h3>
<p class="text-xs text-slate-600 m-0 mt-1">Reutilización de cámaras analógicas/IP existentes (RTSP) sin licencias de hardware privativo.</p>
</div>
</div>

<div class="card-light p-4 flex items-start gap-3">
<div class="icon-box icon-box-navy">
<carbon:locked class="text-2xl" />
</div>
<div>
<h3 class="text-sm font-bold text-slate-900 m-0">Seguridad</h3>
<p class="text-xs text-slate-600 m-0 mt-1">Auditoría inmutable descentralizada con hashes SHA-256 en blockchain privada.</p>
</div>
</div>

<div class="card-light p-4 flex items-start gap-3 border-sky-400 bg-sky-50/50">
<div class="icon-box icon-box-amber">
<carbon:scales class="text-2xl" />
</div>
<div>
<div class="flex items-center gap-2 mb-1">
<h3 class="text-sm font-bold text-slate-900 m-0">Legal: Art. 28 CRBV</h3>
<span class="badge-tag text-[9px]">Privacy by Design</span>
</div>
<p class="text-xs text-slate-700 m-0 leading-relaxed font-medium">
Cumplimiento estricto del Art. 28 de la Constitución de la República Bolivariana de Venezuela: jamás se almacenan fotos en blockchain ni base de datos pública; solo se ancla un hash criptográfico irreversible garantizando la autodeterminación informativa.
</p>
</div>
</div>
</div>

<div class="text-right text-xs text-slate-500 font-medium">
Soberanía tecnológica y cumplimiento normativo institucional
</div>
</div>

<!-- 
Esta investigación no requiere comprar hardware biométrico costoso, ya que procesa el video de las cámaras existentes en el borde. Además, protege la identidad del usuario: nunca se guarda una foto en la Blockchain, solo un hash criptográfico irreversible, garantizando la privacidad exigida por la Constitución.
-->

---
layout: center
class: text-center
title: "Capítulo II: Marco Referencial"
---

<!-- Slide 7: Capítulo II Separator -->
<div class="py-12 px-14 card-light-featured max-w-xl mx-auto text-center border-sky-300">
<div class="badge-tag mb-3">
Fundamentos
</div>
<h1 class="text-5xl font-black text-slate-900 tracking-tight mb-2">
CAPÍTULO II
</h1>
<div class="w-20 h-1 bg-sky-500 mx-auto my-3 rounded-full"></div>
<h2 class="text-xl font-bold text-sky-800">
MARCO TEÓRICO Y STACK TECNOLÓGICO
</h2>
</div>

<!-- 
(Transición al Capítulo II)
-->

---
layout: default
title: "Bases Teóricas"
---

<!-- Slide 8: Bases Teóricas (Separado) -->
<div class="h-full flex flex-col justify-between">
<div>
<div class="flex items-center justify-between mb-1">
<span class="badge-tag">Marco Teórico</span>
<span class="text-xs text-sky-700 font-mono font-bold">08 / 19</span>
</div>
<h1 class="text-2xl font-extrabold text-slate-900">Bases Teóricas y Modelos</h1>
</div>

<div class="grid grid-cols-2 gap-4 my-auto">
<div class="card-light p-4">
<div class="flex items-center gap-3 mb-2">
<div class="w-9 h-9 rounded-lg bg-sky-100 text-sky-700 flex items-center justify-center text-xl"><carbon:face-activated-add /></div>
<div>
<h4 class="text-sm font-bold text-slate-900 m-0">ArcFace (Additive Angular Margin)</h4>
<span class="text-[10px] text-sky-700 font-mono font-bold">Deep Residual Networks</span>
</div>
</div>
<p class="text-xs text-slate-700 m-0 leading-relaxed">
Función de pérdida que añade un margen angular aditivo $m$ directamente sobre el ángulo de la esfera hiperelemental para maximizar la separación inter-clase y cohesión intra-clase en vectores de 512 dimensiones.
</p>
</div>

<div class="card-light p-4">
<div class="flex items-center gap-3 mb-2">
<div class="w-9 h-9 rounded-lg bg-emerald-100 text-emerald-700 flex items-center justify-center text-xl"><carbon:chart-network /></div>
<div>
<h4 class="text-xs font-bold text-slate-900 m-0">Mapeo Topológico y EAR</h4>
<span class="text-[10px] text-emerald-700 font-mono font-bold">468 Puntos Faciales 3D</span>
</div>
</div>
<p class="text-xs text-slate-700 m-0 leading-relaxed">
Estimación de la apertura palpebral mediante el índice Eye Aspect Ratio (EAR). Permite identificar el ciclo de parpadeo espontáneo cuando $EAR \le 0.21$ de forma local en el nodo perimetral.
</p>
</div>

<div class="card-light p-4">
<div class="flex items-center gap-3 mb-2">
<div class="w-9 h-9 rounded-lg bg-amber-100 text-amber-700 flex items-center justify-center text-xl"><carbon:fingerprint-recognition /></div>
<div>
<h4 class="text-xs font-bold text-slate-900 m-0">Detección de Ataques (PAD / LBP)</h4>
<span class="text-[10px] text-amber-700 font-mono font-bold">Patrones Binarios Locales</span>
</div>
</div>
<p class="text-xs text-slate-700 m-0 leading-relaxed">
Análisis microtextural mediante operadores LBP y entropía de Shannon sobre la región facial para discriminar reflectancias no naturales generadas por papel fotográfico o pantallas LCD/OLED.
</p>
</div>

<div class="card-light p-4">
<div class="flex items-center gap-3 mb-2">
<div class="w-9 h-9 rounded-lg bg-purple-100 text-purple-700 flex items-center justify-center text-xl"><carbon:blockchain /></div>
<div>
<h4 class="text-xs font-bold text-slate-900 m-0">Criptografía e Inmutabilidad</h4>
<span class="text-[10px] text-purple-700 font-mono font-bold">Consenso Proof of Authority</span>
</div>
</div>
<p class="text-xs text-slate-700 m-0 leading-relaxed">
Estructura de bloques enlazados criptográficamente mediante árboles de Merkle y hashes SHA-256 que garantizan la integridad probatoria y la imposibilidad de manipulación retroactiva de auditorías.
</p>
</div>
</div>

<div class="card-light px-4 py-2 flex items-center justify-between text-xs text-slate-600 font-medium bg-slate-50">
<span>📐 Modelos matemáticos de visión computacional y criptografía aplicada</span>
<span class="text-sky-800 font-bold">Vector 512D + EAR + LBP + SHA-256</span>
</div>
</div>

<!-- 
Nuestra base teórica se sustenta en la visión artificial con ArcFace para generar vectores de 512 dimensiones, y MediaPipe para extraer la geometría ocular. A nivel de seguridad, el análisis de textura LBP descarta fotos y pantallas, mientras que la criptografía asimétrica y la Blockchain anclan el no repudio.
-->

---
layout: default
title: "Stack Tecnológico"
---

<!-- Slide 9: Stack Tecnológico (Separado) -->
<div class="h-full flex flex-col justify-between">
<div>
<div class="flex items-center justify-between mb-1">
<span class="badge-tag">Arquitectura de Software</span>
<span class="text-xs text-sky-700 font-mono font-bold">09 / 19</span>
</div>
<h1 class="text-2xl font-extrabold text-slate-900">Stack Tecnológico</h1>
</div>

<div class="grid grid-cols-3 gap-3.5 my-auto">
<div class="card-light p-3.5 flex flex-col justify-between">
<div>
<div class="flex items-center gap-2 mb-2">
<div class="w-8 h-8 rounded-lg bg-sky-100 text-sky-700 flex items-center justify-center text-base"><carbon:video /></div>
<h4 class="text-xs font-bold text-slate-900 m-0">Edge Gateway</h4>
</div>
<span class="badge-tag text-[9px] mb-2">Python & OpenCV</span>
<p class="text-xs text-slate-600 m-0">Captura de flujos RTSP, filtrado previo de movimiento y parpadeo local.</p>
</div>
</div>

<div class="card-light p-3.5 flex flex-col justify-between">
<div>
<div class="flex items-center gap-2 mb-2">
<div class="w-8 h-8 rounded-lg bg-emerald-100 text-emerald-700 flex items-center justify-center text-base"><carbon:api /></div>
<h4 class="text-xs font-bold text-slate-900 m-0">FastAPI & AsyncIO</h4>
</div>
<span class="badge-tag badge-tag-emerald text-[9px] mb-2">Microservicios REST</span>
<p class="text-xs text-slate-600 m-0">Servidor backend asíncrono con canales WebSockets para streaming dúplex.</p>
</div>
</div>

<div class="card-light p-3.5 flex flex-col justify-between">
<div>
<div class="flex items-center gap-2 mb-2">
<div class="w-8 h-8 rounded-lg bg-amber-100 text-amber-700 flex items-center justify-center text-base"><carbon:data-blob /></div>
<h4 class="text-xs font-bold text-slate-900 m-0">ChromaDB</h4>
</div>
<span class="badge-tag badge-tag-amber text-[9px] mb-2">Vector Database</span>
<p class="text-xs text-slate-600 m-0">Indexación HNSW para búsqueda por similitud de distancia coseno en sub-milisegundos.</p>
</div>
</div>

<div class="card-light p-3.5 flex flex-col justify-between">
<div>
<div class="flex items-center gap-2 mb-2">
<div class="w-8 h-8 rounded-lg bg-blue-100 text-blue-700 flex items-center justify-center text-base"><carbon:data-1 /></div>
<h4 class="text-xs font-bold text-slate-900 m-0">SQLite & SQLAlchemy</h4>
</div>
<span class="badge-tag text-[9px] mb-2">Almacén Transaccional</span>
<p class="text-xs text-slate-600 m-0">Persistencia relacional ACID para identidades, credenciales y configuración.</p>
</div>
</div>

<div class="card-light p-3.5 flex flex-col justify-between">
<div>
<div class="flex items-center gap-2 mb-2">
<div class="w-8 h-8 rounded-lg bg-purple-100 text-purple-700 flex items-center justify-center text-base"><carbon:blockchain /></div>
<h4 class="text-xs font-bold text-slate-900 m-0">Solidity & Ethereum PoA</h4>
</div>
<span class="badge-tag text-[9px] mb-2">Smart Contracts</span>
<p class="text-xs text-slate-600 m-0">Contrato inteligente BioAuthLog en red privada de validadores institucionales.</p>
</div>
</div>

<div class="card-light p-3.5 flex flex-col justify-between">
<div>
<div class="flex items-center gap-2 mb-2">
<div class="w-8 h-8 rounded-lg bg-sky-100 text-sky-800 flex items-center justify-center text-base"><carbon:application-web /></div>
<h4 class="text-xs font-bold text-slate-900 m-0">React + TypeScript</h4>
</div>
<span class="badge-tag text-[9px] mb-2">Frontend Dashboard</span>
<p class="text-xs text-slate-600 m-0">Panel de control administrativo, auditoría en vivo y portal biométrico SSO.</p>
</div>
</div>
</div>

<div class="card-light px-4 py-2 flex items-center justify-between text-xs text-slate-700 font-medium bg-slate-50">
<span>⚙️ Despliegue contenerizado mediante Docker y Nginx Reverse Proxy</span>
<span class="text-sky-800 font-bold">100% Software Libre y Estándares Abiertos</span>
</div>
</div>

<!-- 
A nivel tecnológico usamos Python y OpenCV en el borde, FastAPI con WebSockets en el backend, un almacenamiento híbrido con SQLite y ChromaDB, y contratos inteligentes en Solidity para la auditoría inmutable, todo empaquetado en Docker.
-->

---
layout: center
class: text-center
title: "Capítulo III: Metodología"
---

<!-- Slide 10: Capítulo III Separator -->
<div class="py-12 px-14 card-light-featured max-w-xl mx-auto text-center border-sky-300">
<div class="badge-tag mb-3">
Metodología
</div>
<h1 class="text-5xl font-black text-slate-900 tracking-tight mb-2">
CAPÍTULO III
</h1>
<div class="w-20 h-1 bg-sky-500 mx-auto my-3 rounded-full"></div>
<h2 class="text-xl font-bold text-sky-800">
MARCO METODOLÓGICO
</h2>
</div>

<!-- 
(Transición al Capítulo III)
-->

---
layout: two-cols
title: "Metodología Scrum"
---

<!-- Slide 11: Metodología -->
<div class="h-full flex flex-col justify-between pr-4">
<div>
<div class="badge-tag mb-2">Diseño</div>
<h1 class="text-2xl font-extrabold text-slate-900">Metodología</h1>
</div>

<div class="space-y-3 my-auto">
<div class="card-light p-3.5 border-l-4 border-sky-500">
<span class="text-[10px] font-bold text-sky-700 uppercase block">Tipo</span>
<h4 class="text-sm font-bold text-slate-900 m-0">Aplicada y Proyectiva</h4>
<p class="text-xs text-slate-600 m-0 mt-0.5">Solución funcional de ingeniería para una problemática real.</p>
</div>

<div class="card-light p-3.5 border-l-4 border-emerald-500">
<span class="text-[10px] font-bold text-emerald-700 uppercase block">Diseño</span>
<h4 class="text-sm font-bold text-slate-900 m-0">De Campo y Experimental</h4>
<p class="text-xs text-slate-600 m-0 mt-0.5">Validación empírica en laboratorio (S-LAB) y multicámara (S-CAM).</p>
</div>

<div class="card-light p-3 border-l-4 border-navy-500 text-xs text-slate-800 font-bold bg-sky-50/50">
Marco Ágil: Scrum en 6 Sprints iterativos
</div>
</div>

<div class="text-[11px] text-slate-500 font-medium">
Ingeniería de software con entregables continuos
</div>
</div>

::right::

<div class="h-full flex flex-col justify-between pl-2">
<div>
<span class="text-xs font-bold text-sky-700 uppercase tracking-wider block mb-1">Distribución</span>
<h3 class="text-sm font-bold text-slate-900 mb-2">Fases Scrum (6 Sprints)</h3>
</div>

<div class="card-light p-3 flex flex-col items-center justify-center my-auto">
```mermaid
pie title Distribución del Esfuerzo (%)
    "Diagnóstico" : 25
    "Diseño" : 25
    "Construcción" : 30
    "Pruebas" : 20
```
</div>

<div class="text-center text-xs text-sky-800 font-bold">
421 pruebas ejecutadas en la fase final
</div>
</div>

<!-- 
La investigación fue aplicada y de campo, bajo el marco ágil Scrum. Dividimos el trabajo en 6 Sprints, desarrollando el sistema en un entorno de laboratorio (S-LAB) y validándolo en un entorno de campo (S-MULTICÁMARA) con sensores reales.
-->

---
layout: center
class: text-center
title: "Capítulo IV: Resultados"
---

<!-- Slide 12: Capítulo IV Separator -->
<div class="py-12 px-14 card-light-featured max-w-xl mx-auto text-center border-sky-300">
<div class="badge-tag mb-3">
Resultados
</div>
<h1 class="text-5xl font-black text-slate-900 tracking-tight mb-2">
CAPÍTULO IV
</h1>
<div class="w-20 h-1 bg-sky-500 mx-auto my-3 rounded-full"></div>
<h2 class="text-xl font-bold text-sky-800">
RESULTADOS Y ANÁLISIS DE SEGURIDAD
</h2>
</div>

<!-- 
(Transición al Capítulo IV)
-->

---
layout: default
title: "Arquitectura C4 del Sistema"
---

<!-- Slide 13: Arquitectura del Sistema con Diagrama C4 Real -->
<div class="h-full flex flex-col justify-between">
<div class="flex items-center justify-between">
<div>
<div class="badge-tag mb-1">Arquitectura</div>
<h1 class="text-2xl font-extrabold text-slate-900">Arquitectura C4 Ciberfísica Desacoplada</h1>
</div>
<span class="text-xs text-sky-700 font-mono font-bold">13 / 19</span>
</div>

<div class="diagram-frame my-auto flex items-center justify-center max-h-[380px]">
<img src="/diagrams/architecture_c4_layers.png" alt="Arquitectura C4 FaceSentinel" class="max-h-[360px] w-auto mx-auto object-contain rounded" />
</div>

<div class="grid grid-cols-4 gap-3 text-center text-xs">
<div class="card-light py-1.5 px-2 font-bold text-sky-800 bg-sky-50">1. Edge (RTSP/EAR)</div>
<div class="card-light py-1.5 px-2 font-bold text-emerald-800 bg-emerald-50">2. FastAPI & WebSockets</div>
<div class="card-light py-1.5 px-2 font-bold text-amber-800 bg-amber-50">3. SQLite + ChromaDB</div>
<div class="card-light py-1.5 px-2 font-bold text-purple-800 bg-purple-50">4. Ethereum PoA</div>
</div>
</div>

<!-- 
Este es el núcleo de FaceSentinel. Las cámaras capturan el flujo de video RTSP, el nodo Edge detecta el parpadeo localmente para ahorrar red, y envía la imagen a la API. La API valida la textura, extrae el rostro, lo busca en ChromaDB y, si hay coincidencia, sella la auditoría asíncronamente en la Blockchain.
-->

---
layout: default
title: "Embudo Anti-Spoofing"
---

<!-- Slide 14: El Embudo Anti-Spoofing (Sin símbolos rotos) -->
<div class="h-full flex flex-col justify-between">
<div>
<div class="flex items-center justify-between mb-2">
<span class="badge-tag">Liveness PAD</span>
<span class="text-xs text-sky-700 font-mono font-bold">14 / 19</span>
</div>
<h1 class="text-3xl font-extrabold text-slate-900">Embudo Anti-Spoofing Multicapa</h1>
<p class="text-sm text-sky-800 mt-0.5 font-medium">Validación jerárquica para anulación de ataques de presentación (ISO/IEC 30107-3).</p>
</div>

<div class="flex flex-col items-center justify-center gap-2 my-auto max-w-2xl mx-auto w-full">
<div class="w-full funnel-step bg-sky-600 text-white">
<div class="flex items-center gap-3">
<span class="px-2.5 py-0.5 rounded bg-black/25 text-xs font-mono font-bold">Nivel 1</span>
<span class="text-sm font-bold">EAR en Edge: Detección de Parpadeo Fisiológico</span>
</div>
<span class="text-xs font-mono font-bold bg-white/20 px-2 py-0.5 rounded">EAR ≤ 0.21</span>
</div>

<div class="text-sky-600 font-bold text-lg">↓</div>

<div class="w-[88%] funnel-step bg-sky-700 text-white">
<div class="flex items-center gap-3">
<span class="px-2.5 py-0.5 rounded bg-black/25 text-xs font-mono font-bold">Nivel 2</span>
<span class="text-sm font-bold">LBP en Servidor: Análisis de Textura Microdérmica</span>
</div>
<span class="text-xs font-mono font-bold bg-white/20 px-2 py-0.5 rounded">Anti-Papel Mate</span>
</div>

<div class="text-sky-600 font-bold text-lg">↓</div>

<div class="w-[76%] funnel-step bg-blue-800 text-white">
<div class="flex items-center gap-3">
<span class="px-2.5 py-0.5 rounded bg-black/25 text-xs font-mono font-bold">Nivel 3</span>
<span class="text-sm font-bold">FFT 2D en Servidor: Frecuencia Espectral</span>
</div>
<span class="text-xs font-mono font-bold bg-white/20 px-2 py-0.5 rounded">Anti-Pantallas LCD/OLED</span>
</div>

<div class="text-sky-600 font-bold text-lg">↓</div>

<div class="w-[64%] funnel-step bg-slate-900 text-white">
<div class="flex items-center gap-3">
<span class="px-2.5 py-0.5 rounded bg-sky-500 text-xs font-mono font-bold text-slate-950">Nivel 4</span>
<span class="text-sm font-bold">Desafío Activo Web: Retos Aleatorios</span>
</div>
<span class="text-xs font-mono font-bold bg-white/20 px-2 py-0.5 rounded">Anti-Video Replay</span>
</div>
</div>

<div class="card-light px-4 py-2.5 flex items-center justify-between text-xs font-bold text-slate-700 bg-sky-50/60">
<span>Defensa en profundidad contra suplantación biométrica</span>
<span class="text-emerald-700">Tasa APCER Lograda: 0.98%</span>
</div>
</div>

<!-- 
Para evitar fraudes, creamos un embudo implacable de 4 niveles. Primero, el usuario parpadea (EAR). Luego, analizamos la textura de la piel mediante LBP para descartar papel. En el tercer nivel, FFT 2D detecta la trama de pantallas. Y en la web, retos de movimiento impiden videos grabados.
-->

---
layout: default
title: "Secuencia de Autenticación SSO"
---

<!-- Slide 15: Integración Práctica con Diagrama de Secuencia Real -->
<div class="h-full flex flex-col justify-between">
<div class="flex items-center justify-between">
<div>
<div class="badge-tag mb-1">Integración SSO</div>
<h1 class="text-2xl font-extrabold text-slate-900">Secuencia de Autenticación e IdP Federation</h1>
</div>
<span class="text-xs text-sky-700 font-mono font-bold">15 / 19</span>
</div>

<div class="diagram-frame my-auto flex items-center justify-center max-h-[380px]">
<img src="/diagrams/sequence_authentication2.jpeg" alt="Secuencia de Autenticación FaceSentinel" class="max-h-[360px] w-auto mx-auto object-contain rounded" />
</div>

<div class="card-light px-4 py-2 flex items-center justify-between text-xs text-slate-700 font-medium bg-slate-50">
<span>Eliminación de contraseñas mediante Claims JWT asimétricos</span>
<span class="text-sky-800 font-bold">Handshake seguro &lt; 400ms</span>
</div>
</div>

<!-- 
Aquí vemos el resultado operativo. Logramos integrar FaceSentinel como Proveedor de Identidad en un software externo preliminar del ecosistema UNEGIA. El usuario ya no necesita contraseñas; se redirige al portal biométrico mediante WebSockets, supera los retos y retorna autenticado mediante un Token JWT seguro.
-->

---
layout: default
title: "Resultados de Seguridad"
---

<!-- Slide 16: Resultados de Seguridad -->
<div class="h-full flex flex-col justify-between">
<div>
<div class="flex items-center justify-between mb-2">
<span class="badge-tag">Métricas Empíricas</span>
<span class="text-xs text-sky-700 font-mono font-bold">16 / 19</span>
</div>
<h1 class="text-3xl font-extrabold text-slate-900">Resultados de Seguridad (421 Ensayos)</h1>
</div>

<div class="grid grid-cols-3 gap-8 my-auto">
<div class="flex flex-col items-center">
<div class="metric-circle-light metric-circle-emerald">
<span class="text-3xl font-black text-emerald-700">95.72%</span>
<span class="text-[10px] text-emerald-800 uppercase font-bold tracking-wider mt-1">Eficacia</span>
</div>
<h3 class="text-base font-bold text-slate-900 mt-3 mb-0">Exactitud Global</h3>
<p class="text-xs text-slate-600 text-center mt-1 m-0">Precisión en condiciones de luz diurna y controlada.</p>
</div>

<div class="flex flex-col items-center">
<div class="metric-circle-light">
<span class="text-3xl font-black text-sky-700">0.98%</span>
<span class="text-[10px] text-sky-800 uppercase font-bold tracking-wider mt-1">APCER</span>
</div>
<h3 class="text-base font-bold text-slate-900 mt-3 mb-0">Aceptación de Ataque</h3>
<p class="text-xs text-slate-600 text-center mt-1 m-0">Bloqueo de fotos HD, pantallas OLED y papel mate.</p>
</div>

<div class="flex flex-col items-center">
<div class="metric-circle-light metric-circle-navy">
<span class="text-3xl font-black text-slate-900">367 ms</span>
<span class="text-[10px] text-slate-700 uppercase font-bold tracking-wider mt-1">Latencia</span>
</div>
<h3 class="text-base font-bold text-slate-900 mt-3 mb-0">Tiempo de Respuesta</h3>
<p class="text-xs text-slate-600 text-center mt-1 m-0">Liveness + Vector Match + Notarización Blockchain.</p>
</div>
</div>

<div class="card-light px-4 py-2 flex items-center justify-between text-xs text-slate-700 font-bold bg-sky-50/70">
<span>Umbral Coseno: 0.60</span>
<span class="text-emerald-700">Impostores Directos Aceptados: 0%</span>
<span>Consenso PoA Instantáneo</span>
</div>
</div>

<!-- 
Las pruebas masivas sobre 421 ensayos confirmaron el éxito. Bloqueamos el 99% de las intrusiones con fotos y pantallas. Al establecer la distancia coseno en 0.60, tuvimos cero por ciento de aceptación de impostores (incluso familiares directos). Y todo este proceso, incluyendo el sellado en Blockchain, ocurre en apenas 367 milisegundos.
-->

---
layout: two-cols
title: "Conclusiones"
---

<!-- Slide 17: Conclusiones -->
<div class="h-full flex flex-col justify-between pr-4">
<div>
<div class="badge-tag mb-2">Cierre</div>
<h1 class="text-2xl font-extrabold text-slate-900">Conclusiones</h1>
</div>

<div class="card-light-featured p-6 text-center my-auto flex flex-col items-center">
<div class="w-20 h-20 rounded-2xl bg-emerald-100 border-2 border-emerald-400 flex items-center justify-center text-emerald-700 shadow-sm mb-3">
<carbon:task-star class="text-4xl" />
</div>
<span class="badge-tag badge-tag-emerald mb-2">Objetivo Alcanzado</span>
<p class="text-xs text-slate-800 leading-relaxed font-bold m-0">
Viabilidad técnica demostrada: alta seguridad perimetral y costo mínimo de despliegue.
</p>
</div>

<div class="text-[11px] text-slate-500 font-medium">
Resultados respaldados experimentalmente
</div>
</div>

::right::

<div class="h-full flex flex-col justify-between pl-2">
<div>
<span class="text-xs font-bold text-sky-700 uppercase tracking-wider block mb-1">Aportes</span>
<h3 class="text-base font-bold text-slate-900 mb-2">Hallazgos Principales</h3>
</div>

<div class="space-y-3.5 my-auto">
<div class="card-light p-3.5 border-l-4 border-sky-500 flex items-start gap-3">
<div class="w-6 h-6 rounded-md bg-sky-100 text-sky-800 flex items-center justify-center flex-shrink-0 mt-0.5">
<carbon:checkmark-outline class="text-base" />
</div>
<div>
<h4 class="text-xs font-bold text-slate-900 m-0">Unificación Ciberfísica Soberana</h4>
<p class="text-xs text-slate-600 m-0 mt-0.5">Control unificado físico y lógico bajo software libre sin licenciamiento privativo.</p>
</div>
</div>

<div class="card-light p-3.5 border-l-4 border-emerald-500 flex items-start gap-3">
<div class="w-6 h-6 rounded-md bg-emerald-100 text-emerald-800 flex items-center justify-center flex-shrink-0 mt-0.5">
<carbon:checkmark-outline class="text-base" />
</div>
<div>
<h4 class="text-xs font-bold text-slate-900 m-0">Bloqueo Efectivo de Spoofing</h4>
<p class="text-xs text-slate-600 m-0 mt-0.5">Embudo multicapa con APCER de 0.98% y cero aceptación de impostores.</p>
</div>
</div>

<div class="card-light p-3.5 border-l-4 border-navy-500 flex items-start gap-3">
<div class="w-6 h-6 rounded-md bg-slate-100 text-slate-900 flex items-center justify-center flex-shrink-0 mt-0.5">
<carbon:checkmark-outline class="text-base" />
</div>
<div>
<h4 class="text-xs font-bold text-slate-900 m-0">Privacidad Constitucional (CRBV)</h4>
<p class="text-xs text-slate-600 m-0 mt-0.5">Notarización criptográfica sin almacenar material biométrico en la cadena.</p>
</div>
</div>
</div>

<div class="text-right text-[11px] text-emerald-700 font-bold">
Sistemas Críticos Protegidos
</div>
</div>

<!-- 
Concluimos que es viable modernizar la universidad reutilizando tecnología pasiva mediante Edge Computing. El embudo Anti-Spoofing fue vital, y la integración de Blockchain nos garantiza que nadie, ni siquiera un administrador, pueda alterar los registros de entrada, manteniendo privada la biometría real.
-->

---
layout: default
title: "Recomendaciones"
---

<!-- Slide 18: Recomendaciones -->
<div class="h-full flex flex-col justify-between">
<div>
<div class="flex items-center justify-between mb-2">
<span class="badge-tag">Escalabilidad</span>
<span class="text-xs text-sky-700 font-mono font-bold">18 / 19</span>
</div>
<h1 class="text-3xl font-extrabold text-slate-900">Recomendaciones</h1>
</div>

<div class="grid grid-cols-3 gap-6 my-auto">
<div class="card-light card-light-hover p-5 flex flex-col justify-between">
<div>
<div class="icon-box mb-3"><carbon:collaborate class="text-2xl" /></div>
<span class="badge-tag mb-1.5 text-[10px]">Infraestructura</span>
<h3 class="text-sm font-bold text-slate-900 mb-1">Nodos Edge Dedicados</h3>
<p class="text-xs text-slate-600 m-0">Desplegar microcomputadores (MiniPCs / Raspberry Pi) acoplados a los switches de cámaras para aislar tráfico perimetral.</p>
</div>
<div class="mt-3 pt-2 border-t border-sky-100 text-[10px] text-sky-700 font-bold">
Aislamiento de VLAN
</div>
</div>

<div class="card-light card-light-hover p-5 flex flex-col justify-between">
<div>
<div class="icon-box icon-box-emerald mb-3"><carbon:security class="text-2xl" /></div>
<span class="badge-tag badge-tag-emerald mb-1.5 text-[10px]">Ciberseguridad</span>
<h3 class="text-sm font-bold text-slate-900 mb-1">Cifrado mTLS y WebRTC</h3>
<p class="text-xs text-slate-600 m-0">Implementar túneles TLS 1.3 estrictos en las transmisiones de video y certificados mutuos entre nodos y API.</p>
</div>
<div class="mt-3 pt-2 border-t border-emerald-100 text-[10px] text-emerald-700 font-bold">
Cero Confianza de Red
</div>
</div>

<div class="card-light card-light-hover p-5 flex flex-col justify-between">
<div>
<div class="icon-box icon-box-navy mb-3"><carbon:task-star class="text-2xl" /></div>
<span class="badge-tag badge-tag-navy mb-1.5 text-[10px]">Electromecánica</span>
<h3 class="text-sm font-bold text-slate-900 mb-1">Actuadores ESP32</h3>
<p class="text-xs text-slate-600 m-0">Integrar relés optoacoplados con microcontroladores ESP32 para apertura de torniquetes y cerraduras magnéticas.</p>
</div>
<div class="mt-3 pt-2 border-t border-slate-100 text-[10px] text-slate-800 font-bold">
Control de Acceso Físico
</div>
</div>
</div>

<div class="card-light px-4 py-2 flex items-center justify-between text-xs text-slate-600 font-medium bg-slate-50">
<span>Hoja de ruta lista para despliegue en campus universitario UNEG</span>
</div>
</div>

<!-- 
Para implementar esto físicamente en la institución de forma segura, recomendamos aislar los DVRs y usar microordenadores locales que consuman el video. El siguiente paso lógico será integrar placas de desarrollo para accionar las cerraduras electromagnéticas y expandir el sistema a todo el campus.
-->

---
layout: center
class: text-center
title: "Muchas Gracias / Preguntas"
---

<!-- Slide 19: Despedida y Preguntas -->
<div class="max-w-2xl mx-auto py-8">
<div class="w-18 h-18 rounded-2xl bg-sky-50 border-2 border-sky-300 flex items-center justify-center text-sky-700 shadow-sm mx-auto mb-4">
<carbon:education class="text-4xl" />
</div>

<div class="badge-tag mb-3">
Defensa Culminada
</div>

<h1 class="text-5xl font-black text-slate-900 tracking-tight mb-2">
¡MUCHAS GRACIAS!
</h1>

<h2 class="text-lg font-bold text-sky-800 max-w-lg mx-auto mb-6">
A disposición del honorable jurado y tutora para el ciclo de preguntas.
</h2>

<div class="card-light py-3 px-6 max-w-md mx-auto flex items-center justify-around border-sky-200">
<div class="text-left">
<span class="text-[10px] text-sky-700 font-bold uppercase block">Ponente</span>
<span class="text-sm font-bold text-slate-900">Br. Héctor Tovar</span>
</div>
<div class="h-6 w-px bg-sky-200"></div>
<div class="text-left">
<span class="text-[10px] text-sky-700 font-bold uppercase block">UNEG</span>
<span class="text-sm font-bold text-slate-900">Ingeniería en Informática</span>
</div>
</div>
</div>

<!-- 
Gracias por su atención, estoy a su entera disposición para la ronda de preguntas.
-->

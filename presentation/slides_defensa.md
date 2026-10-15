---
theme: default
class: cover-slide
highlighter: shiki
lineNumbers: false
drawings:
  persist: false
transition: slide-left
title: "Defensa de Trabajo de Grado - FaceSentinel"
mdc: true
---

<!-- Diapositiva 1 · Portada (30 s) -->
<div class="h-full w-full flex flex-col justify-between py-6 px-10 relative overflow-hidden bg-white">
<svg class="absolute inset-0 w-full h-full pointer-events-none z-0" viewBox="0 0 980 550" preserveAspectRatio="none" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M 640 0 C 700 90, 770 140, 980 180 L 980 0 Z" fill="#97c8eb" opacity="0.8" />
<path d="M 760 0 C 790 70, 840 105, 980 140 L 980 0 Z" fill="#1b4d89" />
<path d="M 0 320 C 60 350, 110 410, 150 470 C 180 515, 230 535, 300 550 L 0 550 Z" fill="#97c8eb" opacity="0.6" />
<path d="M 0 460 C 60 465, 110 500, 150 550 L 0 550 Z" fill="#3b77a8" />
<path d="M 0 480 C 40 480, 80 515, 100 550 L 0 550 Z" fill="#1b4d89" />
<circle cx="518" cy="38" r="6" fill="#97c8eb" />
<circle cx="616" cy="46" r="9" fill="#1b4d89" />
<circle cx="835" cy="128" r="5" fill="#97c8eb" />
<circle cx="32" cy="320" r="7" fill="#1b4d89" />
<circle cx="370" cy="505" r="8" fill="#1b4d89" />
</svg>
<div class="flex items-center justify-center gap-6 relative z-10 pt-1 px-4">
<img src="/diagrams/uneg_logo.png" alt="Logo UNEG" class="h-14 w-auto object-contain drop-shadow-sm" />
<div class="text-center font-bold text-[#1b365d] leading-tight">
<span class="text-[12px] uppercase tracking-wider block font-black">Universidad Nacional Experimental de Guayana</span>
<span class="text-[10px] uppercase tracking-wide block font-bold text-slate-600">Vicerrectorado Académico · Coordinación General de Pregrado</span>
<span class="text-[11px] uppercase tracking-wide block font-black text-[#1b365d]">Ingeniería en Informática</span>
</div>
</div>
<div class="my-auto text-center px-6 max-w-4xl mx-auto relative z-10">
<div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-sky-100/80 border border-sky-300 text-sky-900 text-xs font-bold mb-3">
<span>🛡️ FaceSentinel</span>
<span>·</span>
<span class="text-sky-700 font-semibold">Defensa de Trabajo de Grado</span>
</div>
<h1 class="text-xl md:text-2xl font-black text-[#0f274a] leading-snug uppercase tracking-tight">
Sistema Proveedor de Identidad (IdP) ciberfísico basado en autenticación biométrica facial anti-spoofing y registro inmutable en Blockchain para la gestión unificada de control de acceso
</h1>
</div>
<div class="relative z-10 pb-2 px-8">
<div class="flex justify-between items-end text-xs font-semibold text-[#1b365d] border-t border-slate-200/60 pt-3">
<div class="text-left leading-tight">
<span class="font-bold text-[#1b365d] block text-[11px] uppercase tracking-wider text-slate-500">Tutora Académica</span>
<span class="block text-slate-900 font-bold text-[13px] mt-0.5">Ing. Livia Borjas</span>
</div>
<div class="text-center text-[12px] text-slate-600 font-medium pb-0.5">
Ciudad Guayana, octubre de 2026
</div>
<div class="text-right leading-tight">
<span class="font-bold text-[#1b365d] block text-[11px] uppercase tracking-wider text-slate-500">Autor</span>
<span class="block text-slate-900 font-bold text-[13px] mt-0.5">Héctor Tovar</span>
</div>
</div>
</div>
</div>

<!--
Guion (30 s): "Buenos días, honorable jurado, profesora tutora y público presente. Mi nombre es Héctor Tovar y presento mi Trabajo de Grado para optar al título de Ingeniero en Informática: un sistema proveedor de identidad ciberfísico que combina reconocimiento facial con detección de vida y auditoría en Blockchain, al que denominé FaceSentinel. Agradezco a mi tutora, la ingeniera Livia Borjas, su guía durante este proceso."
Transición: "Empiezo con las tres amenazas que originaron este trabajo."
-->

---
layout: default
title: "Introducción"
---

<!-- Diapositiva 2 · Introducción (1 min) -->
<div class="h-full flex flex-col justify-between">
<div class="flex items-center justify-between pb-2 border-b border-slate-200">
<div class="flex items-center gap-2 text-xs font-bold text-slate-400">
<span class="text-sky-600 font-black">Apertura</span> · I · II · III · IV · Conclusiones
</div>
<span class="text-xs font-mono font-bold text-slate-500">02 / 32</span>
</div>
<div class="my-auto">
<div class="text-center mb-6">
<span class="text-xs uppercase tracking-wider font-extrabold text-red-600 bg-red-50 border border-red-200 px-3 py-1 rounded-full">
Tres Amenazas Críticas
</span>
<h2 class="text-2xl font-black text-slate-900 mt-2">Vulnerabilidades del Control de Acceso Convencional</h2>
</div>
<div class="grid grid-cols-3 gap-6 max-w-4xl mx-auto">
<div class="card-light p-6 text-center border-red-200 bg-red-50/30">
<div class="w-14 h-14 mx-auto mb-3 rounded-2xl bg-red-100 flex items-center justify-center text-red-600 text-2xl">📸</div>
<h3 class="text-base font-bold text-slate-900 mb-1">Spoofing Facial</h3>
<p class="text-xs text-slate-600 font-medium">Fotos y videos que burlan cámaras simples.</p>
</div>
<div class="card-light p-6 text-center border-amber-200 bg-amber-50/30">
<div class="w-14 h-14 mx-auto mb-3 rounded-2xl bg-amber-100 flex items-center justify-center text-amber-700 text-2xl">🏢</div>
<h3 class="text-base font-bold text-slate-900 mb-1">Sistemas Aislados</h3>
<p class="text-xs text-slate-600 font-medium">Silos físicos y de software sin conexión.</p>
</div>
<div class="card-light p-6 text-center border-rose-200 bg-rose-50/30">
<div class="w-14 h-14 mx-auto mb-3 rounded-2xl bg-rose-100 flex items-center justify-center text-rose-700 text-2xl">⚡</div>
<h3 class="text-base font-bold text-slate-900 mb-1">Punto Único de Falla</h3>
<p class="text-xs text-slate-600 font-medium">Bases de datos vulnerables a alteración.</p>
</div>
</div>
<div class="mt-8 text-center">
<div class="inline-flex items-center gap-3 px-6 py-3 rounded-2xl bg-sky-900 text-white font-bold text-sm shadow-md">
<span>➡️ FaceSentinel:</span>
<span class="text-sky-300 font-normal">Rostro + Detección de Vida + Auditoría en Blockchain</span>
</div>
</div>
</div>
<div class="text-center text-[11px] text-slate-400">
En la cadena solo se registran huellas criptográficas, nunca el rostro.
</div>
</div>

<!--
Guion (1 min): "La biometría facial, el cómputo en el borde y la Blockchain permiten controlar accesos con precisión y trazabilidad. Pero al llevarlas a una institución real aparecen tres amenazas: primero, el spoofing, engañar al sistema con una foto o un video; segundo, que el software y los controles físicos funcionan como silos separados; y tercero, los puntos únicos de falla de las bases de datos centralizadas. FaceSentinel responde a las tres: reconocimiento facial profundo, un embudo de detección de vida y un registro de auditoría resistente a alteración, donde en la cadena solo se registran huellas criptográficas, nunca el rostro."
Transición: "Veamos el problema con detalle en el Capítulo I."
-->

---
layout: center
class: text-center
title: "Capítulo I · Portada"
---

<!-- Diapositiva 3 · Portada del capítulo (5 s) -->
<div class="py-12 px-16 card-light-featured max-w-xl mx-auto text-center border-sky-300">
<span class="badge-tag badge-tag-navy mb-4">Contexto y Diagnóstico</span>
<h1 class="text-5xl font-black text-slate-900 tracking-tight mb-3">CAPÍTULO I</h1>
<div class="w-24 h-1.5 bg-sky-500 mx-auto my-4 rounded-full"></div>
<h2 class="text-2xl font-bold text-sky-800">EL PROBLEMA</h2>
</div>

<!--
Guion (5 s): "El primer capítulo plantea el problema, los objetivos y el alcance."
Transición: "Pasemos a analizar el problema."
-->

---
layout: default
title: "El Problema"
---

<!-- Diapositiva 4 · El problema (1 min) -->
<div class="h-full flex flex-col justify-between">
<div class="flex items-center justify-between pb-2 border-b border-slate-200">
<div class="flex items-center gap-2 text-xs font-bold text-slate-400">
Apertura · <span class="text-sky-600 font-black">I · El Problema</span> · II · III · IV · Conclusiones
</div>
<span class="text-xs font-mono font-bold text-slate-500">04 / 32</span>
</div>
<div class="grid grid-cols-2 gap-8 my-auto items-center">
<div class="space-y-4">
<div class="card-light p-4 flex items-center gap-3 border-red-200">
<span class="text-2xl">💳</span>
<div>
<h4 class="font-bold text-sm text-slate-900 m-0">Tarjetas RFID y contraseñas</h4>
<p class="text-xs text-red-600 font-semibold m-0">Fácilmente clonables y compartibles</p>
</div>
</div>
<div class="card-light p-4 flex items-center gap-3 border-amber-200">
<span class="text-2xl">🏢</span>
<div>
<h4 class="font-bold text-sm text-slate-900 m-0">Repositorios centralizados</h4>
<p class="text-xs text-amber-700 font-semibold m-0">Punto único de falla (Stanford, 2023)</p>
</div>
</div>
<div class="card-light p-4 flex items-center gap-3 border-slate-300">
<span class="text-2xl">📹</span>
<div>
<h4 class="font-bold text-sm text-slate-900 m-0">UNEG: CCTV pasivo</h4>
<p class="text-xs text-slate-600 font-semibold m-0">Vigilancia manual sin verificación activa</p>
</div>
</div>
</div>
<div class="card-light p-6 text-center border-sky-300 bg-sky-50/40">
<span class="text-xs uppercase tracking-wider font-extrabold text-sky-800">Situación Actual en UNEG</span>
<div class="my-6 flex items-center justify-center gap-3 text-xs font-bold text-slate-700">
<span class="px-2.5 py-1 bg-white rounded border border-slate-200 shadow-sm">Cámaras</span>
<span>→</span>
<span class="px-2.5 py-1 bg-white rounded border border-slate-200 shadow-sm">DVR</span>
<span>→</span>
<span class="px-2.5 py-1 bg-white rounded border border-slate-200 shadow-sm">Monitor</span>
<span>→</span>
<span class="px-2.5 py-1 bg-red-100 text-red-800 rounded border border-red-200 shadow-sm">Vigilante</span>
</div>
<div class="p-3 bg-white rounded-xl border border-sky-200 text-xs font-bold text-sky-900">
¿Cómo unificar y asegurar el control de acceso lógico y físico?
</div>
</div>
</div>
<div class="text-right text-[11px] text-slate-400">
Diagnóstico de infraestructura Edificio Administrativo UNEG
</div>
</div>

<!--
Guion (1 min): "Tradicionalmente validamos identidad con contraseñas o tarjetas, y la literatura muestra que las credenciales de proximidad se pueden clonar con dispositivos de bajo costo. Concentrar las identidades en una sola base de datos crea además un punto único de falla; universidades como Stanford sufrieron una exfiltración masiva por ransomware en 2023. En la UNEG, el control de acceso del Edificio Administrativo descansa en vigilancia manual y en un circuito cerrado pasivo: las cámaras graban, pero no verifican identidad ni se integran con los sistemas de software. De allí surge la pregunta de investigación que aparece al pie: cómo unificar y asegurar el control de acceso lógico y físico."
Transición: "De esa pregunta salen cuatro objetivos."
-->

---
layout: default
title: "Objetivos"
---

<!-- Diapositiva 5 · Objetivos (1.5 min) -->
<div class="h-full flex flex-col justify-between">
<div class="flex items-center justify-between pb-2 border-b border-slate-200">
<div class="flex items-center gap-2 text-xs font-bold text-slate-400">
Apertura · <span class="text-sky-600 font-black">I · Objetivos</span> · II · III · IV · Conclusiones
</div>
<span class="text-xs font-mono font-bold text-slate-500">05 / 32</span>
</div>
<div class="grid grid-cols-12 gap-6 my-auto items-center">
<div class="col-span-4 card-light p-6 text-center border-sky-300 bg-sky-50/50">
<div class="w-16 h-16 mx-auto mb-3 rounded-2xl bg-sky-500 text-white flex items-center justify-center text-3xl shadow-md">🎯</div>
<span class="badge-tag badge-tag-navy mb-2">Objetivo General</span>
<p class="text-xs text-slate-800 font-bold leading-relaxed m-0">
Desarrollar un IdP ciberfísico con autenticación facial anti-spoofing y registro en Blockchain.
</p>
</div>
<div class="col-span-8 space-y-3">
<div class="p-3.5 rounded-xl border border-sky-300 bg-sky-50/80 flex items-center gap-3">
<span class="px-2.5 py-1 rounded-md bg-sky-600 text-white text-xs font-extrabold">OE1</span>
<span class="text-xs font-bold text-slate-900">Diseñar la arquitectura ciberfísica (a partir del diagnóstico).</span>
</div>
<div class="p-3.5 rounded-xl border border-purple-300 bg-purple-50/80 flex items-center gap-3">
<span class="px-2.5 py-1 rounded-md bg-purple-600 text-white text-xs font-extrabold">OE2</span>
<span class="text-xs font-bold text-slate-900">Desarrollar el núcleo del IdP: motor biométrico + API asíncrona.</span>
</div>
<div class="p-3.5 rounded-xl border border-amber-300 bg-amber-50/80 flex items-center gap-3">
<span class="px-2.5 py-1 rounded-md bg-amber-600 text-white text-xs font-extrabold">OE3</span>
<span class="text-xs font-bold text-slate-900">Implementar el contrato inteligente de auditoría inmutable.</span>
</div>
<div class="p-3.5 rounded-xl border border-emerald-300 bg-emerald-50/80 flex items-center gap-3">
<span class="px-2.5 py-1 rounded-md bg-emerald-600 text-white text-xs font-extrabold">OE4</span>
<span class="text-xs font-bold text-slate-900">Evaluar rendimiento, latencia y seguridad en entornos reales.</span>
</div>
</div>
</div>
<div class="text-center text-[11px] text-slate-400">
Los colores de OE1 a OE4 identifican cada sección de resultados en el Capítulo IV.
</div>
</div>

<!--
Guion (1.5 min): "El objetivo general es desarrollar ese sistema. Para lograrlo planteé cuatro objetivos específicos. El primero, diseñar la arquitectura ciberfísica partiendo del diagnóstico de la infraestructura existente. El segundo, desarrollar el núcleo del proveedor de identidad: el motor biométrico con ArcFace y detección de vida, integrado con el almacenamiento híbrido en una API asíncrona para inicio de sesión único y comunicación máquina a máquina. El tercero, implementar el contrato inteligente de auditoría. Y el cuarto, evaluar rendimiento, latencia y seguridad. Cada objetivo corresponde a una sección del Capítulo IV, y los colores que ven aquí los usaré en los resultados."
Transición: "¿Por qué vale la pena? La justificación."
-->

---
layout: default
title: "Justificación"
---

<!-- Diapositiva 6 · Justificación (45 s) -->
<div class="h-full flex flex-col justify-between">
<div class="flex items-center justify-between pb-2 border-b border-slate-200">
<div class="flex items-center gap-2 text-xs font-bold text-slate-400">
Apertura · <span class="text-sky-600 font-black">I · Justificación</span> · II · III · IV · Conclusiones
</div>
<span class="text-xs font-mono font-bold text-slate-500">06 / 32</span>
</div>
<div class="my-auto">
<div class="text-center mb-8">
<h2 class="text-2xl font-black text-slate-900">Justificación Cuatridimensional</h2>
<p class="text-xs text-slate-500 mt-1">Impacto integral del sistema FaceSentinel</p>
</div>
<div class="grid grid-cols-4 gap-4 max-w-4xl mx-auto">
<div class="card-light p-5 text-center border-sky-300">
<div class="w-12 h-12 mx-auto mb-3 rounded-full bg-sky-100 flex items-center justify-center text-sky-700 text-xl font-bold">1</div>
<h3 class="text-sm font-bold text-slate-900 mb-2">Tecnológica</h3>
<p class="text-xs text-slate-600 m-0">Visión profunda + liveness + vectores + Blockchain.</p>
</div>
<div class="card-light p-5 text-center border-blue-300">
<div class="w-12 h-12 mx-auto mb-3 rounded-full bg-blue-100 flex items-center justify-center text-blue-700 text-xl font-bold">2</div>
<h3 class="text-sm font-bold text-slate-900 mb-2">Operativa</h3>
<p class="text-xs text-slate-600 m-0">Compatible con CCTV analógico instalado.</p>
</div>
<div class="card-light p-5 text-center border-indigo-300">
<div class="w-12 h-12 mx-auto mb-3 rounded-full bg-indigo-100 flex items-center justify-center text-indigo-700 text-xl font-bold">3</div>
<h3 class="text-sm font-bold text-slate-900 mb-2">Ética y Legal</h3>
<p class="text-xs text-slate-600 m-0">Privacidad por diseño: datos pseudonimizados.</p>
</div>
<div class="card-light p-5 text-center border-emerald-300">
<div class="w-12 h-12 mx-auto mb-3 rounded-full bg-emerald-100 flex items-center justify-center text-emerald-700 text-xl font-bold">4</div>
<h3 class="text-sm font-bold text-slate-900 mb-2">Soberana</h3>
<p class="text-xs text-slate-600 m-0">100% Software libre (Ley de Infogobierno).</p>
</div>
</div>
</div>
<div class="text-center text-[11px] text-slate-400">
Articulación con los lineamientos de soberanía tecnológica nacional
</div>
</div>

<!--
Guion (45 s): "El trabajo se justifica en cuatro dimensiones. Tecnológicamente, integra en una sola plataforma visión artificial profunda, detección de vida, una base vectorial y registro distribuido. Operativamente, está pensado para consumir video por protocolos estándar, de modo que sea compatible con cámaras analógicas ya instaladas. En lo ético y legal, aplica privacidad por diseño: en la cadena solo hay identificadores pseudonimizados. Y en lo soberano, está construido con software libre, en línea con la Ley de Infogobierno."
Transición: "Y hasta dónde llega el trabajo."
-->

---
layout: default
title: "Alcance y Limitaciones"
---

<!-- Diapositiva 7 · Alcance y limitaciones (1 min) -->
<div class="h-full flex flex-col justify-between">
<div class="flex items-center justify-between pb-2 border-b border-slate-200">
<div class="flex items-center gap-2 text-xs font-bold text-slate-400">
Apertura · <span class="text-sky-600 font-black">I · Alcance y Limitaciones</span> · II · III · IV · Conclusiones
</div>
<span class="text-xs font-mono font-bold text-slate-500">07 / 32</span>
</div>
<div class="my-auto space-y-6 max-w-4xl mx-auto w-full">
<div>
<span class="text-xs uppercase tracking-wider font-extrabold text-sky-800 block mb-2">Alcance de la Investigación</span>
<div class="grid grid-cols-4 gap-3">
<div class="p-3 rounded-lg bg-sky-50 border border-sky-200 text-center text-xs font-bold text-sky-900">Fase 1: Diagnóstico</div>
<div class="p-3 rounded-lg bg-purple-50 border border-purple-200 text-center text-xs font-bold text-purple-900">Fase 2: Motor + API</div>
<div class="p-3 rounded-lg bg-amber-50 border border-amber-200 text-center text-xs font-bold text-amber-900">Fase 3: Contrato</div>
<div class="p-3 rounded-lg bg-emerald-50 border border-emerald-200 text-center text-xs font-bold text-emerald-900">Fase 4: Evaluación</div>
</div>
<p class="text-xs text-slate-500 text-center mt-2 italic font-medium">
"Ciberfísico" = Hasta la emisión del veredicto lógico M2M (cerraduras como trabajo futuro).
</p>
</div>
<div class="card-light p-5 border-amber-300 bg-amber-50/60">
<div class="flex items-center gap-2 text-amber-900 font-black text-sm mb-2">
<span>⚠️</span>
<span>Limitaciones Declaradas</span>
</div>
<div class="grid grid-cols-3 gap-4 text-xs font-semibold text-slate-800">
<div class="p-2.5 bg-white rounded-lg border border-amber-200 shadow-sm">
<strong>N = 6 participantes:</strong> Muestra física intencional de casos críticos.
</div>
<div class="p-2.5 bg-white rounded-lg border border-amber-200 shadow-sm">
<strong>DVR institucional:</strong> Sin conexión directa; validado por equivalencia RTSP.
</div>
<div class="p-2.5 bg-white rounded-lg border border-amber-200 shadow-sm">
<strong>Modo 1:N:</strong> Búsqueda en galería con acumulación teórica de error.
</div>
</div>
</div>
</div>
<div class="text-center text-[11px] text-slate-400">
Transparencia metodológica: límites reconocidos y mitigados
</div>
</div>

<!--
Guion (1 min): "El alcance se organizó en cuatro fases, una por objetivo, en el Edificio Administrativo y la Dirección de Sistemas Automatizados Inteligentes de la UNEG. Quiero declarar desde ahora tres limitaciones. Primera: la muestra física es pequeña, seis participantes. Segunda: por políticas de seguridad institucional no se me autorizó conectar el sistema al DVR del Edificio Administrativo; lo resolví con equipos equivalentes, como mostraré. Y tercera: el sistema identifica buscando entre todos los usuarios enrolados, lo que tiene una consecuencia que explicaré en los resultados. Además, 'ciberfísico' aquí significa que el sistema llega hasta emitir el veredicto lógico; accionar cerraduras queda como trabajo futuro."
Transición: "Pasemos al marco referencial."
-->

---
layout: center
class: text-center
title: "Capítulo II · Portada"
---

<!-- Diapositiva 8 · Portada del capítulo (5 s) -->
<div class="py-12 px-16 card-light-featured max-w-xl mx-auto text-center border-sky-300">
<span class="badge-tag badge-tag-navy mb-4">Fundamentación Científica</span>
<h1 class="text-5xl font-black text-slate-900 tracking-tight mb-3">CAPÍTULO II</h1>
<div class="w-24 h-1.5 bg-sky-500 mx-auto my-4 rounded-full"></div>
<h2 class="text-2xl font-bold text-sky-800">MARCO REFERENCIAL</h2>
</div>

<!--
Guion (5 s): "Este capítulo reúne los antecedentes, las bases teóricas y el sustento legal."
Transición: "Comenzamos con los cuatro antecedentes."
-->

---
layout: default
title: "Antecedentes"
---

<!-- Diapositiva 9 · Antecedentes (45 s) -->
<div class="h-full flex flex-col justify-between">
<div class="flex items-center justify-between pb-2 border-b border-slate-200">
<div class="flex items-center gap-2 text-xs font-bold text-slate-400">
Apertura · I · <span class="text-sky-600 font-black">II · Antecedentes</span> · III · IV · Conclusiones
</div>
<span class="text-xs font-mono font-bold text-slate-500">09 / 32</span>
</div>
<div class="my-auto max-w-4xl mx-auto w-full">
<div class="grid grid-cols-2 gap-4">
<div class="card-light p-4 border-amber-300">
<span class="text-[10px] font-bold text-amber-800 bg-amber-100 px-2 py-0.5 rounded">Blockchain</span>
<h4 class="text-sm font-bold text-slate-900 mt-2">Seijas (2025, UNEG)</h4>
<p class="text-xs text-slate-600 m-0">Auditoría en Geth PoA → Base para la capa de contratos.</p>
</div>
<div class="card-light p-4 border-purple-300">
<span class="text-[10px] font-bold text-purple-800 bg-purple-100 px-2 py-0.5 rounded">API & IAM</span>
<h4 class="text-sm font-bold text-slate-900 mt-2">Medina (2024, UNEG)</h4>
<p class="text-xs text-slate-600 m-0">IAM y RBAC con FastAPI → Base para la API del IdP.</p>
</div>
<div class="card-light p-4 border-blue-300">
<span class="text-[10px] font-bold text-blue-800 bg-blue-100 px-2 py-0.5 rounded">Datos</span>
<h4 class="text-sm font-bold text-slate-900 mt-2">Salazar y Aguirre (2024, UNEG)</h4>
<p class="text-xs text-slate-600 m-0">Almacenamiento híbrido → SQLite + Base vectorial ChromaDB.</p>
</div>
<div class="card-light p-4 border-sky-300">
<span class="text-[10px] font-bold text-sky-800 bg-sky-100 px-2 py-0.5 rounded">Visión</span>
<h4 class="text-sm font-bold text-slate-900 mt-2">Morcillo (2020, UPV)</h4>
<p class="text-xs text-slate-600 m-0">Reconocimiento facial OpenCV → Base para pipeline visual.</p>
</div>
</div>
<div class="mt-6 p-3 rounded-xl bg-slate-900 text-white text-center text-xs font-semibold">
💡 Integración sinérgica: 4 líneas de investigación consolidadas en una plataforma unificada.
</div>
</div>
<div class="text-center text-[11px] text-slate-400">
Tres de los cuatro antecedentes provienen de la propia escuela de informática de la UNEG
</div>
</div>

<!--
Guion (45 s): "Seleccioné cuatro antecedentes y tres son de la propia UNEG. Seijas implementó un contrato de auditoría sobre Geth con consenso de autoridad, base de mi capa Blockchain. Medina trabajó gestión de identidades con FastAPI, base de mi API. Salazar y Aguirre mostraron la viabilidad del almacenamiento híbrido con una base vectorial. Y Morcillo aporta la visión artificial para reconocimiento facial. No partí de cero: integré cuatro líneas de trabajo en un solo sistema."
Transición: "Y estos son los conceptos que sostienen cada bloque."
-->

---
layout: default
title: "Bases Teóricas"
---

<!-- Diapositiva 10 · Bases teóricas (1 min) -->
<div class="h-full flex flex-col justify-between">
<div class="flex items-center justify-between pb-2 border-b border-slate-200">
<div class="flex items-center gap-2 text-xs font-bold text-slate-400">
Apertura · I · <span class="text-sky-600 font-black">II · Bases Teóricas</span> · III · IV · Conclusiones
</div>
<span class="text-xs font-mono font-bold text-slate-500">10 / 32</span>
</div>
<div class="my-auto max-w-4xl mx-auto w-full">
<div class="grid grid-cols-3 gap-4">
<div class="card-light p-4 text-center border-sky-300">
<div class="text-2xl mb-1">📐</div>
<h4 class="text-sm font-bold text-slate-900">ArcFace</h4>
<p class="text-xs text-slate-600 m-0">Vector de 512D · Distancia coseno angular.</p>
</div>
<div class="card-light p-4 text-center border-purple-300">
<div class="text-2xl mb-1">👁️</div>
<h4 class="text-sm font-bold text-slate-900">PAD (Liveness)</h4>
<p class="text-xs text-slate-600 m-0">Embudo multicapa: EAR + LBP + FFT 2D.</p>
</div>
<div class="card-light p-4 text-center border-indigo-300">
<div class="text-2xl mb-1">⚖️</div>
<h4 class="text-sm font-bold text-slate-900">1:1 vs. 1:N</h4>
<p class="text-xs text-slate-600 m-0">Verificación declarada vs. Búsqueda en galería.</p>
</div>
<div class="card-light p-4 text-center border-blue-300">
<div class="text-2xl mb-1">🗄️</div>
<h4 class="text-sm font-bold text-slate-900">Datos Híbridos</h4>
<p class="text-xs text-slate-600 m-0">SQLite relacional + ChromaDB con HNSW.</p>
</div>
<div class="card-light p-4 text-center border-amber-300">
<div class="text-2xl mb-1">⛓️</div>
<h4 class="text-sm font-bold text-slate-900">Blockchain PoA</h4>
<p class="text-xs text-slate-600 m-0">Consenso Clique: validadores institucionales.</p>
</div>
<div class="card-light p-4 text-center border-emerald-300">
<div class="text-2xl mb-1">🔑</div>
<h4 class="text-sm font-bold text-slate-900">IdP, SSO & JWT</h4>
<p class="text-xs text-slate-600 m-0">Tokens RS256 para personas y M2M para máquinas.</p>
</div>
</div>
</div>
<div class="text-center text-[11px] text-slate-400">
Fundamentos matemáticos y arquitectónicos que sustentan la solución
</div>
</div>

<!--
Guion (1 min): "Destaco tres ideas. Primera, ArcFace convierte un rostro en un vector de 512 dimensiones que se compara por distancia coseno. Segunda, la detección de vida, o PAD, busca distinguir un rostro real de una foto o un video, y yo la construí como un embudo de capas. Y tercera, una distinción que será clave en los resultados: la verificación 1:1 compara contra una identidad declarada, mientras que la identificación 1:N busca entre todos los usuarios enrolados. Esa diferencia determina cómo se acumula el error."
Transición: "Y el marco legal."
-->

---
layout: default
title: "Bases Legales"
---

<!-- Diapositiva 11 · Bases legales (30 s) -->
<div class="h-full flex flex-col justify-between">
<div class="flex items-center justify-between pb-2 border-b border-slate-200">
<div class="flex items-center gap-2 text-xs font-bold text-slate-400">
Apertura · I · <span class="text-sky-600 font-black">II · Bases Legales</span> · III · IV · Conclusiones
</div>
<span class="text-xs font-mono font-bold text-slate-500">11 / 32</span>
</div>
<div class="my-auto max-w-4xl mx-auto w-full">
<div class="grid grid-cols-2 gap-4">
<div class="card-light p-5 border-sky-300">
<div class="flex items-center gap-3">
<span class="text-2xl">📜</span>
<h4 class="text-sm font-bold text-slate-900 m-0">CRBV Art. 28</h4>
</div>
<p class="text-xs text-slate-600 mt-2 m-0">Autodeterminación informativa: sin imágenes ni datos personales en claro en la cadena.</p>
</div>
<div class="card-light p-5 border-emerald-300">
<div class="flex items-center gap-3">
<span class="text-2xl">🐧</span>
<h4 class="text-sm font-bold text-slate-900 m-0">Ley de Infogobierno</h4>
</div>
<p class="text-xs text-slate-600 mt-2 m-0">Software libre, formatos y estándares abiertos para el Estado venezolano.</p>
</div>
<div class="card-light p-5 border-red-300">
<div class="flex items-center gap-3">
<span class="text-2xl">⚖️</span>
<h4 class="text-sm font-bold text-slate-900 m-0">Delitos Informáticos</h4>
</div>
<p class="text-xs text-slate-600 mt-2 m-0">Tipificación y prevención del acceso indebido a sistemas de información.</p>
</div>
<div class="card-light p-5 border-blue-300">
<div class="flex items-center gap-3">
<span class="text-2xl">✍️</span>
<h4 class="text-sm font-bold text-slate-900 m-0">Mensajes de Datos</h4>
</div>
<p class="text-xs text-slate-600 mt-2 m-0">Validez y eficacia probatoria de bitácoras y firmas electrónicas.</p>
</div>
</div>
</div>
<div class="text-center text-[11px] text-slate-400">
Alineación estricta con el ordenamiento jurídico de la República Bolivariana de Venezuela
</div>
</div>

<!--
Guion (30 s): "El diseño responde al marco venezolano. El Artículo 28 de la Constitución protege la autodeterminación informativa, por eso en la cadena no se registran imágenes ni datos personales en claro. La Ley de Infogobierno promueve software libre y estándares abiertos, que es el camino que seguí. La Ley contra los Delitos Informáticos tipifica el acceso indebido, que el sistema busca prevenir, y la Ley de Mensajes de Datos reconoce el valor de los registros electrónicos."
Transición: "Veamos cómo se hizo: el marco metodológico."
-->

---
layout: center
class: text-center
title: "Capítulo III · Portada"
---

<!-- Diapositiva 12 · Portada del capítulo (5 s) -->
<div class="py-12 px-16 card-light-featured max-w-xl mx-auto text-center border-sky-300">
<span class="badge-tag badge-tag-navy mb-4">Rigor Experimental</span>
<h1 class="text-5xl font-black text-slate-900 tracking-tight mb-3">CAPÍTULO III</h1>
<div class="w-24 h-1.5 bg-sky-500 mx-auto my-4 rounded-full"></div>
<h2 class="text-2xl font-bold text-sky-800">MARCO METODOLÓGICO</h2>
</div>

<!--
Guion (5 s): "Explico ahora cómo se diseñó la investigación y cómo se midió."
Transición: "Comenzamos con el diseño y los escenarios."
-->

---
layout: default
title: "Diseño y Escenarios"
---

<!-- Diapositiva 13 · Diseño y escenarios (1 min) -->
<div class="h-full flex flex-col justify-between">
<div class="flex items-center justify-between pb-2 border-b border-slate-200">
<div class="flex items-center gap-2 text-xs font-bold text-slate-400">
Apertura · I · II · <span class="text-sky-600 font-black">III · Diseño y Escenarios</span> · IV · Conclusiones
</div>
<span class="text-xs font-mono font-bold text-slate-500">13 / 32</span>
</div>
<div class="my-auto max-w-4xl mx-auto w-full space-y-4">
<div class="flex justify-between items-center px-4 py-2 bg-slate-100 rounded-lg text-xs font-bold text-slate-700">
<span>Tipo: Investigación Aplicada y Proyectiva</span>
<span>·</span>
<span>Diseño: Experimental en banco de pruebas y de campo</span>
</div>
<div class="card-light overflow-hidden border-sky-300">
<table class="w-full text-left text-xs">
<thead class="bg-sky-50 border-b border-sky-200 text-sky-900 font-extrabold">
<tr>
<th class="p-3">Escenario</th>
<th class="p-3">Entorno Físico / Tecnológico</th>
<th class="p-3">Variable Evaluada</th>
</tr>
</thead>
<tbody class="divide-y divide-slate-100 font-medium text-slate-700">
<tr>
<td class="p-3 font-bold text-sky-800">S-RES (Banco)</td>
<td class="p-3">Cámara HiLook + DVR Hikvision (RTSP/TCP)</td>
<td class="p-3">Detección de vida y reconocimiento</td>
</tr>
<tr>
<td class="p-3 font-bold text-purple-800">S-UNEG (Campo)</td>
<td class="p-3">Edificio Administrativo UNEG en red WAN</td>
<td class="p-3">Latencia de red real y flujo SSO</td>
</tr>
<tr>
<td class="p-3 font-bold text-emerald-800">S-DATASET (LFW)</td>
<td class="p-3">Benchmark público (978 pares) en servidor</td>
<td class="p-3">Reconocimiento en población amplia</td>
</tr>
<tr>
<td class="p-3 font-bold text-amber-800">S-CADENA (Geth)</td>
<td class="p-3">Nodo Geth privado institucional (PoA)</td>
<td class="p-3">Notarización, latencia y consumo de gas</td>
</tr>
</tbody>
</table>
</div>
</div>
<div class="text-center text-[11px] text-slate-400">
Tabla 3.1 de la tesis: Cobertura multi-escenario para mitigar limitaciones de campo
</div>
</div>

<!--
Guion (1 min): "La investigación es aplicada, porque produce una solución funcional, y proyectiva, porque propone un modelo a partir de un diagnóstico. El diseño es experimental, en banco de pruebas y de campo, y se organizó en cuatro escenarios: un banco de pruebas, el Edificio Administrativo de la UNEG con la red real de la universidad, una evaluación sobre el conjunto público LFW para el reconocimiento facial, y el nodo Geth institucional para la auditoría. Cada escenario responde a una pregunta distinta, y los resultados del Capítulo IV se presentan en ese orden."
Transición: "¿Con quién y con cuántos ensayos?"
-->

---
layout: default
title: "Muestra y Ensayos"
---

<!-- Diapositiva 14 · Muestra (1 min) -->
<div class="h-full flex flex-col justify-between">
<div class="flex items-center justify-between pb-2 border-b border-slate-200">
<div class="flex items-center gap-2 text-xs font-bold text-slate-400">
Apertura · I · II · <span class="text-sky-600 font-black">III · Muestra</span> · IV · Conclusiones
</div>
<span class="text-xs font-mono font-bold text-slate-500">14 / 32</span>
</div>
<div class="grid grid-cols-2 gap-8 my-auto items-center max-w-4xl mx-auto w-full">
<div class="card-light p-6 border-sky-300 text-center">
<span class="text-4xl font-black text-sky-800 block mb-1">N = 6</span>
<span class="text-xs font-bold text-slate-500 uppercase tracking-wider block mb-4">Participantes Totales</span>
<div class="space-y-3 text-left text-xs font-medium text-slate-700">
<div class="p-2.5 rounded bg-sky-50 border border-sky-200">
<strong>3 Casos Críticos:</strong> Investigador · Hermano consanguíneo (impostor) · Voluntario UNEG.
</div>
<div class="p-2.5 rounded bg-purple-50 border border-purple-200">
<strong>3 Prueba SSO:</strong> Estudiantes UNEG ajenos al desarrollo.
</div>
</div>
</div>
<div class="card-light p-6 border-slate-200">
<div class="flex justify-between items-center mb-3">
<span class="text-lg font-black text-slate-900">421 Ensayos</span>
<span class="text-xs font-bold text-slate-500">Banco de Pruebas</span>
</div>
<div class="space-y-2 text-xs font-bold">
<div class="flex justify-between p-2 rounded bg-emerald-100 text-emerald-900">
<span>Legítimos Genuinos</span><span>104</span>
</div>
<div class="flex justify-between p-2 rounded bg-amber-100 text-amber-900">
<span>Hermano Consanguíneo</span><span>113</span>
</div>
<div class="flex justify-between p-2 rounded bg-rose-100 text-rose-900">
<span>Ataque Video (Teléfono)</span><span>97</span>
</div>
<div class="flex justify-between p-2 rounded bg-red-100 text-red-900">
<span>Ataque Fotografía Impresa</span><span>107</span>
</div>
</div>
</div>
</div>
<div class="text-center text-[11px] text-slate-400">
Muestreo intencional de casos críticos complementado con 978 pares de LFW
</div>
</div>

<!--
Guion (1 min): "Apliqué un muestreo intencional de casos críticos: tres sujetos, el investigador, mi hermano, que es el caso de máxima semejanza facial, y un voluntario administrativo de la UNEG. Con ellos hice 421 ensayos: 104 intentos legítimos, 113 del impostor consanguíneo y 204 ataques de presentación, 97 con video en un teléfono y 107 con fotografía impresa. Además, tres estudiantes de la UNEG probaron el inicio de sesión único, lo que da seis participantes en total. Soy transparente: es una muestra pequeña; por eso la complementé con un benchmark público de 978 pares."
Transición: "¿Y cómo se midió?"
-->

---
layout: default
title: "Instrumentos y Métricas"
---

<!-- Diapositiva 15 · Instrumentos y métricas (45 s) -->
<div class="h-full flex flex-col justify-between">
<div class="flex items-center justify-between pb-2 border-b border-slate-200">
<div class="flex items-center gap-2 text-xs font-bold text-slate-400">
Apertura · I · II · <span class="text-sky-600 font-black">III · Instrumentos y Métricas</span> · IV · Conclusiones
</div>
<span class="text-xs font-mono font-bold text-slate-500">15 / 32</span>
</div>
<div class="my-auto max-w-4xl mx-auto w-full grid grid-cols-2 gap-6">
<div class="card-light p-5 border-sky-300">
<h3 class="text-sm font-bold text-slate-900 mb-3 flex items-center gap-2">
<span>📋</span> Instrumentos de Recolección
</h3>
<ul class="space-y-2 text-xs font-medium text-slate-700 m-0 p-0 list-none">
<li class="p-2 bg-slate-50 rounded border border-slate-200">
<strong>Bitácoras automáticas:</strong> Logs estructurados en FastAPI.
</li>
<li class="p-2 bg-slate-50 rounded border border-slate-200">
<strong>Archivo CSV de ensayos:</strong> 421 filas con vector, puntaje y veredicto.
</li>
<li class="p-2 bg-slate-50 rounded border border-slate-200">
<strong>Repositorio Git:</strong> Commits e historial de despliegue.
</li>
</ul>
</div>
<div class="card-light p-5 border-purple-300">
<h3 class="text-sm font-bold text-slate-900 mb-3 flex items-center gap-2">
<span>📏</span> Métricas y Estándares
</h3>
<ul class="space-y-2 text-xs font-medium text-slate-700 m-0 p-0 list-none">
<li class="p-2 bg-purple-50 rounded border border-purple-200">
<strong>ISO/IEC 19795-1:</strong> FMR (falsa coincidencia), FNMR (falso rechazo).
</li>
<li class="p-2 bg-purple-50 rounded border border-purple-200">
<strong>ISO/IEC 30107-3:</strong> APCER (ataque aceptado), BPCER (rechazo genuino).
</li>
<li class="p-2 bg-purple-50 rounded border border-purple-200">
<strong>Estadística inferencial:</strong> Intervalos Wilson al 95% y prueba McNemar.
</li>
</ul>
</div>
</div>
<div class="text-center text-[11px] text-slate-400">
Las normas ISO se adoptan como marco de terminología y reporte, sin alegar certificación completa
</div>
</div>

<!--
Guion (45 s): "Los datos salen de bitácoras automáticas del sistema, del archivo de ensayos con cada intento registrado y del repositorio de código. Para medir adopté las métricas definidas en las normas ISO/IEC 19795-1 y 30107-3: tasas de falsa coincidencia y de falso rechazo, y de error en la clasificación de ataques de presentación. Utilizo esas normas como marco de terminología y reporte; no afirmo conformidad con sus protocolos completos. Y los porcentajes de LFW van con intervalo de confianza al 95%."
Transición: "Y el procedimiento de desarrollo."
-->

---
layout: default
title: "Procedimiento de Desarrollo"
---

<!-- Diapositiva 16 · Procedimiento de desarrollo (1 min) -->
<div class="h-full flex flex-col justify-between">
<div class="flex items-center justify-between pb-2 border-b border-slate-200">
<div class="flex items-center gap-2 text-xs font-bold text-slate-400">
Apertura · I · II · <span class="text-sky-600 font-black">III · Procedimiento</span> · IV · Conclusiones
</div>
<span class="text-xs font-mono font-bold text-slate-500">16 / 32</span>
</div>
<div class="my-auto max-w-4xl mx-auto w-full space-y-6">
<div class="text-center">
<span class="text-xs uppercase tracking-wider font-extrabold text-sky-800">Metodología Ágil</span>
<h3 class="text-xl font-black text-slate-900 mt-1">Desarrollo Iterativo (Scrum Adaptado)</h3>
</div>
<div class="grid grid-cols-4 gap-3 text-center">
<div class="p-3 rounded-xl border border-sky-300 bg-sky-50">
<span class="text-xs font-black text-sky-800 block">Iteración 1</span>
<span class="text-[11px] font-semibold text-slate-600 mt-1 block">Diagnóstico y Diseño (OE1)</span>
</div>
<div class="p-3 rounded-xl border border-purple-300 bg-purple-50">
<span class="text-xs font-black text-purple-800 block">Iteración 2</span>
<span class="text-[11px] font-semibold text-slate-600 mt-1 block">Motor Biométrico & API (OE2)</span>
</div>
<div class="p-3 rounded-xl border border-amber-300 bg-amber-50">
<span class="text-xs font-black text-amber-800 block">Iteración 3</span>
<span class="text-[11px] font-semibold text-slate-600 mt-1 block">Contrato y Notarización (OE3)</span>
</div>
<div class="p-3 rounded-xl border border-emerald-300 bg-emerald-50">
<span class="text-xs font-black text-emerald-800 block">Iteración 4</span>
<span class="text-[11px] font-semibold text-slate-600 mt-1 block">Evaluación Integral (OE4)</span>
</div>
</div>
<div class="card-light p-4 bg-slate-900 text-white text-center">
<span class="text-xs text-sky-300 font-bold block mb-2">Stack 100% Software Libre</span>
<p class="text-xs font-mono text-slate-300 m-0">
Python · FastAPI · OpenCV · MediaPipe · ArcFace · SQLite · ChromaDB · Solidity · Geth · React · Docker
</p>
</div>
</div>
<div class="text-center text-[11px] text-slate-400">
Trazabilidad completa en repositorio Git (febrero a octubre de 2026)
</div>
</div>

<!--
Guion (1 min): "El desarrollo siguió un proceso iterativo inspirado en Scrum y adaptado a un trabajo individual, en cuatro iteraciones vinculadas una a una con los objetivos. Todo se construyó con software libre: Python y FastAPI en el servidor, OpenCV, MediaPipe y ArcFace para la visión, SQLite y ChromaDB para los datos, Solidity y Geth para la cadena, y React para la interfaz, desplegado con Docker. El historial del repositorio documenta el trabajo realizado."
Transición: "Con esto, los resultados: el Capítulo IV."
-->

---
layout: center
class: text-center
title: "Capítulo IV · Portada"
---

<!-- Diapositiva 17 · Portada del capítulo (5 s) -->
<div class="py-12 px-16 card-light-featured max-w-2xl mx-auto text-center border-sky-300">
<span class="badge-tag badge-tag-navy mb-4">Evidencia y Validación</span>
<h1 class="text-5xl font-black text-slate-900 tracking-tight mb-2">CAPÍTULO IV</h1>
<h2 class="text-xl font-bold text-sky-800 mb-6">DESARROLLO Y RESULTADOS</h2>
<div class="flex justify-center gap-3">
<span class="px-3 py-1 bg-sky-100 text-sky-800 rounded-lg text-xs font-extrabold border border-sky-300">OE1 · Arquitectura</span>
<span class="px-3 py-1 bg-purple-100 text-purple-800 rounded-lg text-xs font-extrabold border border-purple-300">OE2 · Motor & API</span>
<span class="px-3 py-1 bg-amber-100 text-amber-800 rounded-lg text-xs font-extrabold border border-amber-300">OE3 · Blockchain</span>
<span class="px-3 py-1 bg-emerald-100 text-emerald-800 rounded-lg text-xs font-extrabold border border-emerald-300">OE4 · Evaluación</span>
</div>
</div>

<!--
Guion (5 s): "Presento los resultados siguiendo los cuatro objetivos."
Transición: "Comenzamos con el Objetivo 1: Diagnóstico de la infraestructura."
-->

---
layout: default
title: "OE1 · Diagnóstico"
---

<!-- Diapositiva 18 · OE1 · Diagnóstico de la infraestructura (1.5 min) -->
<div class="h-full flex flex-col justify-between">
<div class="flex items-center justify-between pb-2 border-b border-sky-200">
<div class="flex items-center gap-2 text-xs font-bold text-slate-400">
I · II · III · <span class="text-sky-600 font-black">IV · OE1 Diagnóstico</span> · Conclusiones
</div>
<span class="px-2 py-0.5 rounded bg-sky-100 text-sky-800 text-xs font-extrabold">OE1</span>
</div>
<div class="my-auto max-w-4xl mx-auto w-full space-y-5">
<div class="text-center">
<h3 class="text-xl font-black text-slate-900">Validación por Equivalencia de Interfaz</h3>
<p class="text-xs text-sky-700 font-bold mt-1">CCTV Analógico Institucional → Transmisión Estándar RTSP sobre TCP</p>
</div>
<div class="grid grid-cols-2 gap-6 items-center">
<div class="card-light p-5 border-slate-300 text-center">
<span class="text-xs font-bold text-slate-400 uppercase tracking-wider block mb-2">Esquema Tradicional UNEG</span>
<div class="p-3 bg-slate-50 rounded-lg text-xs font-semibold text-slate-600 space-y-1">
<div>Cámara Hikvision DS-2CE66C0T-IRM</div>
<div>↓ (Cable coaxial analógico)</div>
<div>DVR centralizado → Monitor pasivo</div>
<div class="text-red-600 font-bold">❌ Sin analítica ni verificación activa</div>
</div>
</div>
<div class="card-light p-5 border-sky-400 bg-sky-50/40 text-center">
<span class="text-xs font-bold text-sky-800 uppercase tracking-wider block mb-2">Con FaceSentinel</span>
<div class="p-3 bg-white rounded-lg text-xs font-semibold text-slate-800 space-y-1 border border-sky-200">
<div>Cámara + DVR equivalente (HiLook)</div>
<div>↓ RTSP sobre TCP (Sin error POC 0)</div>
<div>Edge Gateway → API Asíncrona</div>
<div class="text-emerald-700 font-bold">✔ Identificación biométrica en vivo</div>
</div>
</div>
</div>
<div class="p-3 bg-amber-50 border border-amber-200 rounded-xl text-center text-xs text-amber-900 font-medium">
Hallazgo técnico: UDP generó pérdidas de trama (POC 0); se resolvió forzando transporte TCP.
</div>
</div>
<div class="text-center text-[11px] text-slate-400">
Tabla 4.1 de la tesis: Banco experimental equivalente ante restricción de conexión al DVR institucional
</div>
</div>

<!--
Guion (1.5 min): "La institución me suministró una cámara analógica Hikvision para analizar el tipo de infraestructura que existe; aquí está. Por políticas de seguridad no se autorizó conectar el sistema al DVR del Edificio Administrativo, así que validé por equivalencia de interfaz: reproduje la cadena con una cámara HiLook y un DVR Hikvision, entregando video por RTSP sobre TCP; y en el edificio probé en la red real de la universidad con teléfonos como nodos de borde. El argumento técnico es que el software consume video por protocolos estándar, no depende del modelo del sensor. En el banco encontré un problema real: con UDP las tramas llegaban dañadas, error POC 0, y lo resolví forzando TCP. Lo que no evalué es el DVR institucional específico."
Transición: "Con ese diagnóstico, la arquitectura."
-->

---
layout: default
title: "OE1 · Arquitectura"
---

<!-- Diapositiva 19 · OE1 · Arquitectura (1 min) -->
<div class="h-full flex flex-col justify-between">
<div class="flex items-center justify-between pb-2 border-b border-sky-200">
<div class="flex items-center gap-2 text-xs font-bold text-slate-400">
I · II · III · <span class="text-sky-600 font-black">IV · OE1 Arquitectura</span> · Conclusiones
</div>
<span class="px-2 py-0.5 rounded bg-sky-100 text-sky-800 text-xs font-extrabold">OE1</span>
</div>
<div class="my-auto max-w-4xl mx-auto w-full grid grid-cols-12 gap-6 items-center">
<div class="col-span-7 space-y-2.5">
<div class="p-3 rounded-xl border border-sky-400 bg-sky-50 flex items-center justify-between">
<span class="text-xs font-black text-sky-900">4. Capa Auditoría</span>
<span class="text-[11px] font-mono text-sky-700">Geth PoA · AccessRegistry.sol</span>
</div>
<div class="p-3 rounded-xl border border-blue-400 bg-blue-50 flex items-center justify-between">
<span class="text-xs font-black text-blue-900">3. Datos Híbridos</span>
<span class="text-[11px] font-mono text-blue-700">SQLite (Roles) + ChromaDB (Embeddings)</span>
</div>
<div class="p-3 rounded-xl border border-indigo-400 bg-indigo-50 flex items-center justify-between">
<span class="text-xs font-black text-indigo-900">2. API Asíncrona (IdP)</span>
<span class="text-[11px] font-mono text-indigo-700">FastAPI · SSO WebSockets · M2M REST</span>
</div>
<div class="p-3 rounded-xl border border-slate-300 bg-slate-50 flex items-center justify-between">
<span class="text-xs font-black text-slate-800">1. Capa de Borde (Edge)</span>
<span class="text-[11px] font-mono text-slate-600">OpenCV + MediaPipe (EAR Parpadeo)</span>
</div>
</div>
<div class="col-span-5 space-y-3">
<div class="card-light p-4 border-sky-300">
<span class="text-xs font-bold text-sky-800 uppercase block mb-1">Aislamiento de Datos</span>
<p class="text-xs text-slate-600 m-0">Ningún almacén por sí solo reconstruye la identidad.</p>
</div>
<div class="card-light p-4 border-indigo-300">
<span class="text-xs font-bold text-indigo-800 uppercase block mb-1">Gobierno RBAC</span>
<p class="text-xs text-slate-600 m-0">4 roles: Administrador, Nodo Borde, Auditor, App Cliente.</p>
</div>
<div class="card-light p-3 border-emerald-300 bg-emerald-50 text-center text-xs font-bold text-emerald-800">
🛡️ Resiliencia: si la cadena cae, opera con bitácora local.
</div>
</div>
</div>
<div class="text-center text-[11px] text-slate-400">
Figura 2 de la tesis: Arquitectura ciberfísica modular de 4 capas
</div>
</div>

<!--
Guion (1 min): "La arquitectura tiene cuatro capas: el borde, donde están las cámaras y la primera verificación; la API en FastAPI, que actúa como proveedor de identidad; el almacenamiento híbrido; y la auditoría en la cadena de bloques. Separé los datos en tres espacios para que ninguno, por sí solo, permita reconstruir una identidad: SQLite guarda usuarios y permisos, ChromaDB solo los vectores, y la cadena solo huellas criptográficas. El acceso se gobierna con cuatro roles: administrador, nodo de borde, auditor y aplicación cliente, bajo el principio de mínimo privilegio. Si cae la cadena, el sistema sigue operando con su bitácora local."
Transición: "Pasemos al núcleo del proveedor de identidad: el Objetivo 2."
-->

---
layout: default
title: "OE2 · Embudo de Vida"
---

<!-- Diapositiva 20 · OE2 · Embudo de detección de vida (1.5 min) -->
<div class="h-full flex flex-col justify-between">
<div class="flex items-center justify-between pb-2 border-b border-purple-200">
<div class="flex items-center gap-2 text-xs font-bold text-slate-400">
I · II · III · <span class="text-purple-600 font-black">IV · OE2 Embudo de Vida</span> · Conclusiones
</div>
<span class="px-2 py-0.5 rounded bg-purple-100 text-purple-800 text-xs font-extrabold">OE2</span>
</div>
<div class="my-auto max-w-4xl mx-auto w-full space-y-6">
<div class="text-center">
<h3 class="text-xl font-black text-slate-900">Embudo Multicapa Anti-Spoofing (PAD)</h3>
<p class="text-xs text-purple-700 font-bold mt-1">Filtrado progresivo entre el borde y el servidor central</p>
</div>
<div class="grid grid-cols-4 gap-3 text-center">
<div class="card-light p-3.5 border-purple-300 bg-purple-50/50">
<span class="w-7 h-7 mx-auto rounded-full bg-purple-600 text-white text-xs font-black flex items-center justify-center mb-2">1</span>
<h4 class="text-xs font-bold text-slate-900">EAR (Borde)</h4>
<p class="text-[11px] text-slate-600 m-0 mt-1">Detección de parpadeo biológico natural.</p>
</div>
<div class="card-light p-3.5 border-purple-300 bg-purple-50/50">
<span class="w-7 h-7 mx-auto rounded-full bg-purple-600 text-white text-xs font-black flex items-center justify-center mb-2">2</span>
<h4 class="text-xs font-bold text-slate-900">LBP (Servidor)</h4>
<p class="text-[11px] text-slate-600 m-0 mt-1">Microtextura dérmica vs. papel impreso.</p>
</div>
<div class="card-light p-3.5 border-purple-300 bg-purple-50/50">
<span class="w-7 h-7 mx-auto rounded-full bg-purple-600 text-white text-xs font-black flex items-center justify-center mb-2">3</span>
<h4 class="text-xs font-bold text-slate-900">FFT 2D (Servidor)</h4>
<p class="text-[11px] text-slate-600 m-0 mt-1">Frecuencias espaciales: detecta pantallas.</p>
</div>
<div class="card-light p-3.5 border-purple-300 bg-purple-50/50">
<span class="w-7 h-7 mx-auto rounded-full bg-purple-600 text-white text-xs font-black flex items-center justify-center mb-2">4</span>
<h4 class="text-xs font-bold text-slate-900">Desafío Activo</h4>
<p class="text-[11px] text-slate-600 m-0 mt-1">Retos aleatorios en portal: girar y sonreír.</p>
</div>
</div>
<div class="flex justify-between items-center p-3 bg-slate-100 rounded-xl text-xs font-bold text-slate-700">
<span>Niveles de Seguridad: 1 a 4 por cámara</span>
<span>·</span>
<span>Calibración individual por óptica del sensor</span>
</div>
</div>
<div class="text-center text-[11px] text-slate-400">
Figura 5 de la tesis: Pipeline de detección de vida híbrido perimetral-central
</div>
</div>

<!--
Guion (1.5 min): "El corazón del sistema es un embudo de cuatro capas repartido entre el borde y el servidor. En el borde, el parpadeo, medido con la relación de aspecto del ojo: si hay un parpadeo real, se envía un solo fotograma al servidor en vez de video continuo. En el servidor, la textura de la piel con patrones binarios locales, y el análisis de frecuencias con la transformada de Fourier, que detecta el patrón que dejan las pantallas. Y la cuarta, un desafío activo en el canal de inicio de sesión: dos retos aleatorios, girar la cabeza y abrir la boca. Cada sensor se configura con un nivel de seguridad del 1 al 4; el nivel 1 desactiva la detección de vida y no está pensado para áreas sensibles. Los umbrales de textura se calibran por cámara, porque dependen del sensor."
Transición: "Si el intento sobrevive al embudo, entra el reconocimiento."
-->

---
layout: default
title: "OE2 · Reconocimiento e IdP"
---

<!-- Diapositiva 21 · OE2 · Reconocimiento e IdP (1 min) -->
<div class="h-full flex flex-col justify-between">
<div class="flex items-center justify-between pb-2 border-b border-purple-200">
<div class="flex items-center gap-2 text-xs font-bold text-slate-400">
I · II · III · <span class="text-purple-600 font-black">IV · OE2 Reconocimiento & IdP</span> · Conclusiones
</div>
<span class="px-2 py-0.5 rounded bg-purple-100 text-purple-800 text-xs font-extrabold">OE2</span>
</div>
<div class="my-auto max-w-4xl mx-auto w-full grid grid-cols-2 gap-6 items-center">
<div class="space-y-4">
<div class="card-light p-4 border-purple-300">
<span class="text-xs font-extrabold text-purple-800 uppercase block mb-1">Motor ArcFace</span>
<div class="text-xs font-semibold text-slate-800 space-y-1">
<div>Embedding facial: Vector de 512 dimensiones</div>
<div>Búsqueda en ChromaDB (índice HNSW)</div>
<div class="text-purple-900 font-bold">Umbral estricto: Distancia coseno d &lt; 0.60</div>
</div>
</div>
<div class="card-light p-4 border-sky-300">
<span class="text-xs font-extrabold text-sky-800 uppercase block mb-1">Manejo de Errores M2M</span>
<p class="text-xs text-slate-700 m-0">
Si el fotograma se corrompe por red: respuesta <strong>HTTP 422</strong> para reintento inmediato sin generar falsos rechazos ni registros basura en Blockchain.
</p>
</div>
</div>
<div class="card-light p-5 border-slate-300 bg-slate-50 space-y-3">
<span class="text-xs font-bold text-slate-500 uppercase tracking-wider block">Dos Vías de Autenticación</span>
<div class="p-3 bg-white rounded-lg border border-slate-200">
<h4 class="text-xs font-bold text-slate-900 m-0">1. Personas: SSO Web</h4>
<p class="text-[11px] text-slate-600 m-0 mt-1">
Redirección a portal + canal WebSocket en vivo + emisión de token JWT firmado (RS256).
</p>
</div>
<div class="p-3 bg-white rounded-lg border border-slate-200">
<h4 class="text-xs font-bold text-slate-900 m-0">2. Máquinas: Acceso Físico M2M</h4>
<p class="text-[11px] text-slate-600 m-0 mt-1">
POST /physical-access/authenticate → veredicto booleano en milisegundos.
</p>
</div>
</div>
</div>
<div class="text-center text-[11px] text-slate-400">
Figuras 6 y 7-A de la tesis: Diagrama de secuencia del IdP y documentación OpenAPI/Swagger
</div>
</div>

<!--
Guion (1 min): "Superado el embudo, ArcFace genera el vector y se busca el candidato más cercano en ChromaDB; si la distancia es menor a 0.60, hay coincidencia. La API opera como proveedor de identidad por dos vías. Para personas, el inicio de sesión único: una aplicación externa redirige al portal, donde un canal WebSocket evalúa la vida y la identidad en tiempo real, y se devuelve un token firmado. Para máquinas, un endpoint de acceso físico que recibe el fotograma y devuelve el veredicto; si el fotograma llega dañado por la red, responde con código 422 y pide otro, sin generar un falso rechazo ni basura en la cadena."
Transición: "Cada decisión queda registrada: Objetivo 3."
-->

---
layout: default
title: "OE3 · Contrato Inteligente"
---

<!-- Diapositiva 22 · OE3 · Contrato inteligente y privacidad (1.5 min) -->
<div class="h-full flex flex-col justify-between">
<div class="flex items-center justify-between pb-2 border-b border-amber-200">
<div class="flex items-center gap-2 text-xs font-bold text-slate-400">
I · II · III · <span class="text-amber-600 font-black">IV · OE3 Contrato Inteligente</span> · Conclusiones
</div>
<span class="px-2 py-0.5 rounded bg-amber-100 text-amber-800 text-xs font-extrabold">OE3</span>
</div>
<div class="my-auto max-w-4xl mx-auto w-full grid grid-cols-12 gap-6 items-center">
<div class="col-span-5 card-light p-4 font-mono text-[11px] text-slate-800 bg-slate-50 border-amber-300">
<span class="text-[10px] font-bold text-amber-800 uppercase block mb-2 font-sans">AccessRegistry.sol</span>
<div class="space-y-1">
<div>struct AuthRecord {</div>
<div class="pl-3 text-amber-900">bytes32 userIdHash;</div>
<div class="pl-3 text-slate-600">bytes32 vectorHash;</div>
<div class="pl-3 text-slate-600">uint256 timestamp;</div>
<div class="pl-3 text-emerald-700">bool granted;</div>
<div class="pl-3 text-slate-600">string deviceId;</div>
<div class="pl-3 text-slate-600">uint16 score;</div>
<div>}</div>
</div>
<div class="mt-3 pt-2 border-t border-slate-200 text-[10px] text-slate-500 font-sans">
Solidity nativo · Consenso Clique (PoA)
</div>
</div>
<div class="col-span-7 space-y-3">
<div class="grid grid-cols-3 gap-2 text-center">
<div class="p-3 rounded-lg bg-amber-50 border border-amber-200">
<span class="text-base font-black text-amber-900 block">207 430</span>
<span class="text-[10px] text-slate-600">Gas Promedio</span>
</div>
<div class="p-3 rounded-lg bg-emerald-50 border border-emerald-200">
<span class="text-base font-black text-emerald-900 block">Costo 0</span>
<span class="text-[10px] text-slate-600">Red Privada</span>
</div>
<div class="p-3 rounded-lg bg-sky-50 border border-sky-200">
<span class="text-base font-black text-sky-900 block">2 s</span>
<span class="text-[10px] text-slate-600">Período Bloque</span>
</div>
</div>
<div class="card-light p-4 border-amber-300">
<span class="text-xs font-bold text-amber-900 block mb-1">Privacidad por Diseño</span>
<p class="text-xs text-slate-700 m-0">
<strong>userIdHash = SHA-256(id + sal secreta)</strong>. La cédula nunca viaja a la Blockchain. Notarización en background para no retrasar el acceso.
</p>
</div>
</div>
</div>
<div class="text-center text-[11px] text-slate-400">
Figura 10 de la tesis: Estructura de eventos y transacciones en el nodo Geth institucional
</div>
</div>

<!--
Guion (1.5 min): "Implementé el contrato AccessRegistry en Solidity, sin librerías externas, desplegado en un nodo Geth institucional con consenso de autoridad y bloques cada dos segundos. Cada evento guarda un identificador pseudonimizado, la huella del vector, la hora, el resultado, el dispositivo y el puntaje. El consumo promedio es de unas 207 mil unidades de gas, con costo monetario cero por ser red privada. Sobre privacidad: la cédula nunca viaja en claro; el backend calcula un SHA-256 con una sal secreta que vive fuera del código, en variables de entorno. Esto es pseudonimización, no anonimización: depende de custodiar esa sal, y por eso recomiendo un gestor de secretos con versionado. Y el registro es asíncrono: primero se guarda en la base local y luego se notariza, así la cadena nunca retrasa el acceso."
Transición: "Ahora evaluamos todo esto: Objetivo 4."
-->

---
layout: default
title: "OE4 · Ensayos"
---

<!-- Diapositiva 23 · OE4 · Resultados de los 421 ensayos (1.5 min) -->
<div class="h-full flex flex-col justify-between">
<div class="flex items-center justify-between pb-2 border-b border-emerald-200">
<div class="flex items-center gap-2 text-xs font-bold text-slate-400">
I · II · III · <span class="text-emerald-600 font-black">IV · OE4 Ensayos en Banco</span> · Conclusiones
</div>
<span class="px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 text-xs font-extrabold">OE4</span>
</div>
<div class="my-auto max-w-4xl mx-auto w-full grid grid-cols-12 gap-6 items-center">
<div class="col-span-6 card-light p-5 border-emerald-300">
<span class="text-xs font-extrabold text-emerald-900 uppercase block mb-3">Matriz de Confusión (N = 421)</span>
<div class="grid grid-cols-2 gap-2 text-center text-xs">
<div class="p-3 bg-emerald-50 border border-emerald-200 rounded-lg">
<span class="block text-slate-500 text-[10px]">Verdaderos Positivos</span>
<span class="text-xl font-black text-emerald-800">88</span>
</div>
<div class="p-3 bg-amber-50 border border-amber-200 rounded-lg">
<span class="block text-slate-500 text-[10px]">Falsos Rechazos</span>
<span class="text-xl font-black text-amber-800">16</span>
</div>
<div class="p-3 bg-red-50 border border-red-200 rounded-lg">
<span class="block text-slate-500 text-[10px]">Falsas Aceptaciones</span>
<span class="text-xl font-black text-red-700">2</span>
</div>
<div class="p-3 bg-slate-100 border border-slate-200 rounded-lg">
<span class="block text-slate-500 text-[10px]">Verdaderos Negativos</span>
<span class="text-xl font-black text-slate-800">315</span>
</div>
</div>
<div class="text-[10px] text-slate-500 text-center mt-2">
Las 2 falsas aceptaciones fueron fotos impresas; 0 videos superaron el sistema.
</div>
</div>
<div class="col-span-6 space-y-3">
<div class="card-light p-4 border-emerald-300 text-center bg-emerald-50/40">
<span class="text-3xl font-black text-emerald-800 block">99.37%</span>
<span class="text-xs font-bold text-slate-600">Especificidad Global (Exactitud 95.72%)</span>
</div>
<div class="grid grid-cols-2 gap-3 text-center">
<div class="p-3 rounded-xl bg-purple-50 border border-purple-200">
<span class="text-lg font-black text-purple-900 block">0 / 113</span>
<span class="text-[11px] text-slate-600">Impostor Hermano</span>
</div>
<div class="p-3 rounded-xl bg-rose-50 border border-rose-200">
<span class="text-lg font-black text-rose-900 block">0 / 97</span>
<span class="text-[11px] text-slate-600">Ataques Video</span>
</div>
</div>
<div class="p-2.5 bg-amber-50 border border-amber-200 rounded-xl text-center text-xs font-semibold text-amber-900">
Costo de seguridad: Falso rechazo de 15.38% (priorizó no dejar entrar intrusos).
</div>
</div>
</div>
<div class="text-center text-[11px] text-slate-400">
Tablas 5 y 6 de la tesis: Ningún video ni intento del impostor consanguíneo fue aceptado
</div>
</div>

<!--
Guion (1.5 min): "De los 421 ensayos, el sistema aceptó 88 de los 104 accesos legítimos y rechazó 315 de los 317 intentos indebidos. Esto da una especificidad global de 99.37% y una exactitud de 95.72%. De los 204 ataques de presentación, solo 2 superaron el sistema, ambos fotografías impresas: ningún video fue aceptado, y mi hermano, el caso más exigente de semejanza facial, fue rechazado en los 113 intentos. Pero esta seguridad tiene un costo que presento sin esconder: un falso rechazo del 15.38%, usuarios legítimos que necesitaron un segundo intento, por ejemplo cuando parpadean muy rápido o cambia la luz. Prioricé que un intruso no entre. Y recuerdo que son tres sujetos y un solo impostor consanguíneo: es una prueba de viabilidad en banco, no una estadística poblacional."
Transición: "Para validar el flujo con usuarios ajenos al desarrollo, lo probaron tres estudiantes."
-->

---
layout: default
title: "OE4 · Prueba SSO"
---

<!-- Diapositiva 24 · OE4 · Prueba de aceptación del SSO (1.5 min) -->
<div class="h-full flex flex-col justify-between">
<div class="flex items-center justify-between pb-2 border-b border-emerald-200">
<div class="flex items-center gap-2 text-xs font-bold text-slate-400">
I · II · III · <span class="text-emerald-600 font-black">IV · OE4 Prueba SSO Usuarios</span> · Conclusiones
</div>
<span class="px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 text-xs font-extrabold">OE4</span>
</div>
<div class="my-auto max-w-4xl mx-auto w-full space-y-5">
<div class="text-center">
<span class="text-xs uppercase tracking-wider font-extrabold text-emerald-800">8 de octubre de 2026 · UNEGIA → FaceSentinel</span>
<h3 class="text-xl font-black text-slate-900 mt-1">44 Eventos de Autenticación con Usuarios Reales</h3>
</div>
<div class="grid grid-cols-3 gap-4 text-center">
<div class="card-light p-4 border-emerald-300">
<span class="text-2xl font-black text-emerald-700 block">38 / 39</span>
<span class="text-xs font-bold text-slate-900 block mt-1">Accesos Genuinos (97.4%)</span>
<span class="text-[10px] text-slate-500 block mt-1">1 reintento exitoso a los 6 s</span>
</div>
<div class="card-light p-4 border-red-300">
<span class="text-2xl font-black text-red-700 block">3 / 3</span>
<span class="text-xs font-bold text-slate-900 block mt-1">No Enrolados Rechazados</span>
<span class="text-[10px] text-slate-500 block mt-1">Distancias: 0.63 y 0.65 (umbral 0.60)</span>
</div>
<div class="card-light p-4 border-purple-300">
<span class="text-2xl font-black text-purple-700 block">2 / 2</span>
<span class="text-xs font-bold text-slate-900 block mt-1">Videos Spoofing Detenidos</span>
<span class="text-[10px] text-slate-500 block mt-1">Burlaron parpadeo, FFT los frenó</span>
</div>
</div>
<div class="p-3 bg-purple-50 border border-purple-200 rounded-xl text-center text-xs text-purple-900 font-semibold">
💡 Conclusión clave: el embudo multicapa es indispensable; ninguna técnica aislada es suficiente.
</div>
</div>
<div class="text-center text-[11px] text-slate-400">
Tabla 9.1 y Figuras 11-12 de la tesis: Validación de aceptación con estudiantes UNEG
</div>
</div>

<!--
Guion (1.5 min): "Tres estudiantes de la UNEG accedieron al módulo preliminar de UNEGIA y se autenticaron con su rostro en FaceSentinel por el canal WebSocket. Quedaron 44 eventos registrados. De 39 intentos de usuarios legítimos, 38 fueron concedidos; el único denegado se autenticó seis segundos después. Tres intentos de personas no enroladas fueron rechazados, dos de ellos con distancias de 0.63 y 0.65, muy cerca del umbral, lo que concuerda con lo que veremos en LFW. Y dos ataques con un video de parpadeo en un teléfono engañaron la capa del parpadeo y la textura, pero la FFT los detuvo: eso demuestra por qué el embudo necesita varias capas. Es una prueba de operatividad con usuarios reales, no una estadística de desempeño."
Transición: "Ahora, el reconocimiento en una población amplia."
-->

---
layout: default
title: "OE4 · Benchmark LFW"
---

<!-- Diapositiva 25 · OE4 · Evaluación poblacional (LFW) (1.5 min) -->
<div class="h-full flex flex-col justify-between">
<div class="flex items-center justify-between pb-2 border-b border-emerald-200">
<div class="flex items-center gap-2 text-xs font-bold text-slate-400">
I · II · III · <span class="text-emerald-600 font-black">IV · OE4 Evaluación LFW</span> · Conclusiones
</div>
<span class="px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 text-xs font-extrabold">OE4</span>
</div>
<div class="my-auto max-w-4xl mx-auto w-full space-y-5">
<div class="text-center">
<span class="text-xs uppercase tracking-wider font-extrabold text-emerald-800">Benchmark Poblacional · 978 Pares LFW</span>
<h3 class="text-xl font-black text-slate-900 mt-1">Calibración de Umbral en Pipeline de Producción</h3>
</div>
<div class="grid grid-cols-2 gap-6 items-center">
<div class="card-light p-4 border-slate-300 text-center">
<span class="text-xs font-bold text-slate-500 uppercase block mb-1">Literatura (d &lt; 0.68)</span>
<div class="space-y-1 text-xs">
<div>Falsas coincidencias (FMR): <strong class="text-red-600 text-base">9.28%</strong></div>
<div>Falso rechazo (FNMR): 19.68%</div>
</div>
</div>
<div class="card-light p-4 border-emerald-400 bg-emerald-50/50 text-center">
<span class="text-xs font-bold text-emerald-800 uppercase block mb-1">FaceSentinel (d &lt; 0.60)</span>
<div class="space-y-1 text-xs">
<div>Falsas coincidencias (FMR): <strong class="text-emerald-700 text-base">3.71%</strong></div>
<div>Falso rechazo (FNMR): 22.92%</div>
</div>
</div>
</div>
<div class="card-light p-4 border-emerald-300 text-center bg-emerald-50/80">
<span class="text-2xl font-black text-emerald-800 block">Reducción de 60.0% de Falsas Coincidencias</span>
<span class="text-xs font-bold text-slate-700 block mt-1">
Prueba McNemar altamente significativa (p &lt; 0.001) · Exactitud global 86.61% · EER 16.66%
</span>
</div>
</div>
<div class="text-center text-[11px] text-slate-400">
Tabla 10 de la tesis: Evaluación del pipeline completo en servidor bajo estándar ISO/IEC 19795-1
</div>
</div>

<!--
Guion (1.5 min): "Para mitigar la limitación de la muestra, evalué el reconocimiento facial sobre 978 pares del conjunto público LFW, con el pipeline real de producción dentro del servidor. Con el umbral de 0.68 que sugiere la literatura, las falsas coincidencias fueron de 9.28%; con mi umbral de 0.60 bajaron a 3.71%: 27 de 45 falsas aceptaciones eliminadas, una reducción de 60.0%, significativa según la prueba de McNemar. La contrapartida es que el falso rechazo sube a 22.92%. Debo aclarar que esto mide el pipeline completo en producción, con fallos de detección y un umbral fijo estricto, y que su exactitud de 86.61% es inferior a lo que se publica para el modelo ArcFace aislado. Lo valioso es que me da una cota poblacional realista, que el banco de tres sujetos no puede dar."
Transición: "Y esa cota tiene una consecuencia importante."
-->

---
layout: default
title: "OE4 · Modo 1:N"
---

<!-- Diapositiva 26 · OE4 · Modo 1:N y segundo factor (1.5 min) -->
<div class="h-full flex flex-col justify-between">
<div class="flex items-center justify-between pb-2 border-b border-emerald-200">
<div class="flex items-center gap-2 text-xs font-bold text-slate-400">
I · II · III · <span class="text-emerald-600 font-black">IV · OE4 Modo 1:N</span> · Conclusiones
</div>
<span class="px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 text-xs font-extrabold">OE4</span>
</div>
<div class="my-auto max-w-4xl mx-auto w-full grid grid-cols-12 gap-6 items-center">
<div class="col-span-6 card-light p-5 border-amber-300 bg-amber-50/40">
<span class="text-xs font-extrabold text-amber-900 uppercase block mb-2">Acumulación Teórica de Error</span>
<div class="p-3 bg-white rounded-lg border border-amber-200 text-center font-mono text-sm font-black text-slate-800 mb-3">
Error Global ≈ 1 − (1 − FMR)^N
</div>
<div class="space-y-1.5 text-xs font-semibold text-slate-700">
<div class="flex justify-between"><span>N = 10 usuarios:</span> <strong class="text-amber-800">31.5%</strong></div>
<div class="flex justify-between"><span>N = 20 usuarios:</span> <strong class="text-amber-800">53.1%</strong></div>
<div class="flex justify-between"><span>N = 50 usuarios:</span> <strong class="text-red-700">84.9%</strong></div>
<div class="flex justify-between"><span>N = 100 usuarios:</span> <strong class="text-red-700">97.7%</strong></div>
</div>
</div>
<div class="col-span-6 space-y-4">
<div class="card-light p-4 border-slate-300">
<h4 class="text-xs font-bold text-slate-900 m-0">El Rostro como Factor Único</h4>
<p class="text-xs text-red-600 font-bold m-0 mt-1">
No es suficiente en producción para despliegues masivos.
</p>
</div>
<div class="card-light p-4 border-emerald-300 bg-emerald-50">
<h4 class="text-xs font-bold text-emerald-900 m-0">Solución NIST SP 800-63B</h4>
<p class="text-xs text-slate-700 m-0 mt-1">
Exigir un <strong>segundo factor (PIN / tarjeta RFID)</strong> o pasar a <strong>verificación 1:1</strong> con identidad declarada previamente.
</p>
</div>
</div>
</div>
<div class="text-center text-[11px] text-slate-400">
Estimación teórica de acumulación de FMR (3.71%) vs. tamaño de galería N
</div>
</div>

<!--
Guion (1.5 min): "Esta es la conclusión más importante de mi evaluación. Como el sistema busca entre todos los usuarios enrolados, cada usuario adicional es una oportunidad de falsa coincidencia, y el error del sistema crece con el tamaño de la galería. Con el 3.71% medido en LFW, esa probabilidad teórica sería del 31% con 10 usuarios y del 85% con 50. En mi banco, con tres usuarios enrolados, ese efecto casi no se manifiesta, y por eso mis resultados no lo contradicen. Y no es un problema particular de los familiares: ningún sistema facial tiene error cero. Por eso la guía NIST SP 800-63B admite la biometría como parte de una autenticación multifactor. Mi conclusión es que el rostro es un factor, no un oráculo: en producción se requiere un segundo factor, o verificar contra una identidad declarada. Mi tesis demuestra el factor facial y mide su límite."
Transición: "Veamos ahora la velocidad."
-->

---
layout: default
title: "OE4 · Latencia y Blockchain"
---

<!-- Diapositiva 27 · OE4 · Latencia y notarización (1 min) -->
<div class="h-full flex flex-col justify-between">
<div class="flex items-center justify-between pb-2 border-b border-emerald-200">
<div class="flex items-center gap-2 text-xs font-bold text-slate-400">
I · II · III · <span class="text-emerald-600 font-black">IV · OE4 Latencia</span> · Conclusiones
</div>
<span class="px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 text-xs font-extrabold">OE4</span>
</div>
<div class="my-auto max-w-4xl mx-auto w-full space-y-6">
<div class="text-center">
<span class="text-4xl font-black text-emerald-800 block">689.98 ms</span>
<span class="text-xs font-bold text-slate-600 uppercase tracking-wider">Latencia Extremo a Extremo en Red WAN Real</span>
</div>
<div class="card-light p-4 border-slate-300">
<span class="text-xs font-bold text-slate-500 uppercase block mb-2">Desglose de Latencia</span>
<div class="flex h-6 rounded-lg overflow-hidden text-xs font-bold text-white text-center">
<div style="width: 2%" class="bg-sky-500" title="Borde 6.30 ms"></div>
<div style="width: 70%" class="bg-amber-500 flex items-center justify-center" title="Red WAN 485.79 ms">Red WAN: 70.4%</div>
<div style="width: 28%" class="bg-emerald-600 flex items-center justify-center" title="Servidor 197.89 ms">Servidor: 28.7%</div>
</div>
<div class="flex justify-between text-[11px] font-semibold text-slate-600 mt-2">
<span>Borde: 6.30 ms</span>
<span>Red: 485.79 ms</span>
<span>Servidor: 197.89 ms (&lt; 500 ms ✔)</span>
</div>
</div>
<div class="grid grid-cols-2 gap-4 text-center">
<div class="p-3 bg-emerald-50 border border-emerald-200 rounded-xl text-xs font-bold text-emerald-900">
✔ Extremo a Extremo &lt; 1 s (Cumplido con 690 ms)
</div>
<div class="p-3 bg-sky-50 border border-sky-200 rounded-xl text-xs font-bold text-sky-900">
✔ Notarización Geth: 1.90 s (Asíncrona, en 2.º plano)
</div>
</div>
</div>
<div class="text-center text-[11px] text-slate-400">
Tablas 7 y 8 de la tesis: Medición de rendimiento en red universitaria UNEG
</div>
</div>

<!--
Guion (1 min): "La latencia de extremo a extremo medida en la red WAN de la universidad fue de 690 milisegundos. El 70% corresponde al tránsito de red, 486 ms, que no depende del sistema; el cómputo del servidor fue de 198 ms. Inicialmente el requisito de rendimiento fijaba 500 ms sin distinguir la red, y al medir en la WAN real lo reformulé en dos criterios, servidor menor a 500 ms y extremo a extremo menor a 1 segundo, y lo dejé documentado en la tesis. La notarización en Geth promedió 1.9 segundos con 20 transacciones, determinada por el período de bloque de 2 segundos; como es asíncrona, no retrasa la respuesta al usuario."
Transición: "Resumo cómo quedaron los requerimientos."
-->

---
layout: default
title: "Cumplimiento y Trazabilidad"
---

<!-- Diapositiva 28 · Cumplimiento y trazabilidad (45 s) -->
<div class="h-full flex flex-col justify-between">
<div class="flex items-center justify-between pb-2 border-b border-emerald-200">
<div class="flex items-center gap-2 text-xs font-bold text-slate-400">
I · II · III · <span class="text-emerald-600 font-black">IV · Requerimientos</span> · Conclusiones
</div>
<span class="px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 text-xs font-extrabold">OE4</span>
</div>
<div class="my-auto max-w-4xl mx-auto w-full space-y-6">
<div class="text-center">
<h3 class="text-xl font-black text-slate-900">11 de 11 Requerimientos Cumplidos (100%)</h3>
<p class="text-xs text-slate-500 mt-1">Verificación formal documentada en Tabla 11 de la tesis</p>
</div>
<div class="card-light p-5 border-emerald-300">
<div class="grid grid-cols-11 gap-1 text-center font-mono text-xs font-black">
<div class="p-2 bg-emerald-100 text-emerald-800 rounded">RF1 ✔</div>
<div class="p-2 bg-emerald-100 text-emerald-800 rounded">RF2 ✔</div>
<div class="p-2 bg-emerald-100 text-emerald-800 rounded">RF3 ✔</div>
<div class="p-2 bg-emerald-100 text-emerald-800 rounded">RF4 ✔</div>
<div class="p-2 bg-emerald-100 text-emerald-800 rounded">RF5 ✔</div>
<div class="p-2 bg-emerald-100 text-emerald-800 rounded">RF6 ✔</div>
<div class="p-2 bg-teal-100 text-teal-800 rounded">RNF1 ✔</div>
<div class="p-2 bg-teal-100 text-teal-800 rounded">RNF2 ✔</div>
<div class="p-2 bg-teal-100 text-teal-800 rounded">RNF3 ✔</div>
<div class="p-2 bg-teal-100 text-teal-800 rounded">RNF4 ✔</div>
<div class="p-2 bg-teal-100 text-teal-800 rounded">RNF5 ✔</div>
</div>
</div>
<div class="grid grid-cols-4 gap-3 text-center text-xs font-bold">
<div class="p-3 bg-sky-50 border border-sky-200 rounded-lg text-sky-900">OE1 ✔ Arquitectura</div>
<div class="p-3 bg-purple-50 border border-purple-200 rounded-lg text-purple-900">OE2 ✔ Motor + API</div>
<div class="p-3 bg-amber-50 border border-amber-200 rounded-lg text-amber-900">OE3 ✔ Contrato</div>
<div class="p-3 bg-emerald-50 border border-emerald-200 rounded-lg text-emerald-900">OE4 ✔ Evaluación</div>
</div>
</div>
<div class="text-center text-[11px] text-slate-400">
Tabla 11 de la tesis: Matriz de trazabilidad y criterios de aceptación
</div>
</div>

<!--
Guion (45 s): "Verifiqué los seis requerimientos funcionales y los cinco no funcionales de la Tabla 11, cada uno con su evidencia y su entorno de verificación, y cada uno vinculado a un objetivo. Con esto, los cuatro objetivos quedan cubiertos: la arquitectura con su diagnóstico, el motor y la API, el contrato inteligente y la evaluación. Paso a las conclusiones."
Transición: "Retomo las tres amenazas del inicio."
-->

---
layout: default
title: "Conclusiones"
---

<!-- Diapositiva 29 · Conclusiones (1.5 min) -->
<div class="h-full flex flex-col justify-between">
<div class="flex items-center justify-between pb-2 border-b border-slate-200">
<div class="flex items-center gap-2 text-xs font-bold text-slate-400">
I · II · III · IV · <span class="text-sky-600 font-black">Conclusiones</span>
</div>
<span class="text-xs font-mono font-bold text-slate-500">29 / 32</span>
</div>
<div class="my-auto max-w-4xl mx-auto w-full space-y-5">
<div class="grid grid-cols-3 gap-4">
<div class="card-light p-4 border-emerald-300 bg-emerald-50/30 text-center">
<span class="text-2xl block mb-1">📸 ✔</span>
<h4 class="text-xs font-bold text-slate-900">Anti-Spoofing</h4>
<p class="text-[11px] text-slate-600 m-0">Embudo de 4 capas: 0/97 videos aceptados.</p>
</div>
<div class="card-light p-4 border-emerald-300 bg-emerald-50/30 text-center">
<span class="text-2xl block mb-1">🏢 ✔</span>
<h4 class="text-xs font-bold text-slate-900">Fin a los Silos</h4>
<p class="text-[11px] text-slate-600 m-0">IdP federado para personas (SSO) y máquinas (M2M).</p>
</div>
<div class="card-light p-4 border-emerald-300 bg-emerald-50/30 text-center">
<span class="text-2xl block mb-1">⚡ ✔</span>
<h4 class="text-xs font-bold text-slate-900">Sin Punto Único</h4>
<p class="text-[11px] text-slate-600 m-0">Auditoría Blockchain descentralizada y log local.</p>
</div>
</div>
<div class="grid grid-cols-4 gap-3 text-center text-xs">
<div class="p-2.5 bg-sky-50 border border-sky-200 rounded-lg">
<strong class="text-sky-900 block">OE1</strong> Equivalencia interfaz
</div>
<div class="p-2.5 bg-purple-50 border border-purple-200 rounded-lg">
<strong class="text-purple-900 block">OE2</strong> 0 / 113 hermano
</div>
<div class="p-2.5 bg-amber-50 border border-amber-200 rounded-lg">
<strong class="text-amber-900 block">OE3</strong> 207 430 gas · $0
</div>
<div class="p-2.5 bg-emerald-50 border border-emerald-200 rounded-lg">
<strong class="text-emerald-900 block">OE4</strong> 689.98 ms WAN
</div>
</div>
<div class="p-3 bg-amber-50 border border-amber-300 rounded-xl text-center text-xs font-bold text-amber-900">
⚠️ Límite principal: El rostro, por sí solo, no basta como factor único en despliegues de producción masivos.
</div>
</div>
<div class="text-center text-[11px] text-slate-400">
Respuesta afirmativa y honesta a la pregunta de investigación
</div>
</div>

<!--
Guion (1.5 min): "En conclusión, el trabajo respondió la pregunta de investigación: un proveedor de identidad ciberfísico con detección de vida y auditoría en Blockchain sí unifica el control de acceso lógico y perimetral en un prototipo funcional. Retomo las tres amenazas: el spoofing se enfrentó con un embudo de cuatro capas; los silos, con un proveedor federado que sirve a personas y a máquinas; y el punto único de falla, descentralizando la auditoría y manteniendo una bitácora local. Por objetivo: diseñé una arquitectura sobre equipos equivalentes por interfaz; el motor bloqueó los videos y los intentos de mi hermano en el banco; el contrato registra cada evento a costo cero; y la latencia fue de 690 ms. Y la conclusión que más pesa: los resultados demuestran la viabilidad técnica, no el desempeño poblacional, y el rostro por sí solo no basta como factor único en producción."
Transición: "¿Y qué sigue? Las recomendaciones."
-->

---
layout: default
title: "Recomendaciones"
---

<!-- Diapositiva 30 · Recomendaciones (1 min) -->
<div class="h-full flex flex-col justify-between">
<div class="flex items-center justify-between pb-2 border-b border-slate-200">
<div class="flex items-center gap-2 text-xs font-bold text-slate-400">
I · II · III · IV · <span class="text-sky-600 font-black">Recomendaciones</span>
</div>
<span class="text-xs font-mono font-bold text-slate-500">30 / 32</span>
</div>
<div class="my-auto max-w-4xl mx-auto w-full space-y-4">
<div class="text-center mb-4">
<h3 class="text-xl font-black text-slate-900">Hoja de Ruta Tecnológica</h3>
<p class="text-xs text-slate-500 mt-1">Evolución proyectada por objetivo específico</p>
</div>
<div class="space-y-3 text-xs">
<div class="p-3 rounded-xl border border-sky-300 bg-sky-50 flex items-center gap-3">
<span class="px-2 py-0.5 rounded bg-sky-600 text-white font-extrabold text-[10px]">OE1</span>
<div class="text-slate-800">
<strong>Infraestructura:</strong> Cámaras IP con sensor infrarrojo cercano (NIR), aislamiento en VLAN y Gateways de borde locales en puertas.
</div>
</div>
<div class="p-3 rounded-xl border border-purple-300 bg-purple-50 flex items-center gap-3">
<span class="px-2 py-0.5 rounded bg-purple-600 text-white font-extrabold text-[10px]">OE2</span>
<div class="text-slate-800">
<strong>Motor Biométrico:</strong> Obligatoriedad de segundo factor (MFA) en producción y adopción de estándar OIDC con PKCE.
</div>
</div>
<div class="p-3 rounded-xl border border-amber-300 bg-amber-50 flex items-center gap-3">
<span class="px-2 py-0.5 rounded bg-amber-600 text-white font-extrabold text-[10px]">OE3</span>
<div class="text-slate-800">
<strong>Blockchain:</strong> Consorcio interinstitucional de nodos, gestor de secretos con rotación de sal y cifrado en reposo.
</div>
</div>
<div class="p-3 rounded-xl border border-emerald-300 bg-emerald-50 flex items-center gap-3">
<span class="px-2 py-0.5 rounded bg-emerald-600 text-white font-extrabold text-[10px]">OE4</span>
<div class="text-slate-800">
<strong>Evaluación Futura:</strong> Actuación física (ESP32), pruebas frente a deepfakes/máscaras 3D y piloto semestral con N ≥ 50.
</div>
</div>
</div>
</div>
<div class="text-center text-[11px] text-slate-400">
Líneas de investigación y escalabilidad institucional futura
</div>
</div>

<!--
Guion (1 min): "Las recomendaciones corresponden una a una con los objetivos. Para la infraestructura: cámaras IP con óptica infrarroja, aislar el video en una VLAN con transporte cifrado y llevar pasarelas de borde a las puertas, lo que además reduciría el 70% de latencia que vino de la red. Para el motor: el segundo factor en producción, infrarrojo cercano para reducir el falso rechazo y OpenID Connect para el inicio de sesión. Para la cadena: un consorcio de nodos entre sedes, gestión formal de secretos con versionado de claves y cifrado en reposo de los vectores. Y para la evaluación: construir la capa de actuación con microcontroladores y realizar un piloto de un semestre con 50 o más usuarios. Adicionalmente, como trabajo futuro, evaluar el sistema frente a máscaras 3D y deepfakes y bajo pruebas de carga."
Transición: "Frase final."
-->

---
layout: center
class: text-center
title: "Frase de Cierre"
---

<!-- Diapositiva 31 · Frase de cierre (15 s) -->
<div class="py-12 px-12 card-light-featured max-w-2xl mx-auto text-center border-sky-300">
<div class="text-3xl text-sky-600 mb-4 font-serif">“</div>
<blockquote class="text-2xl font-black text-slate-900 leading-snug tracking-tight m-0">
La seguridad, la privacidad y la soberanía tecnológica también se pueden construir desde la universidad.
</blockquote>
<div class="w-16 h-1 bg-sky-500 mx-auto my-4 rounded-full"></div>
<span class="text-xs font-bold text-sky-800 uppercase tracking-widest">FaceSentinel · UNEG 2026</span>
</div>

<!--
Guion (15 s): "Este trabajo muestra que es posible construir, desde la universidad, un sistema de identidad que cuide la seguridad y la privacidad con software libre."
Transición: "Agradecimiento y preguntas."
-->

---
layout: center
class: text-center
title: "Muchas Gracias"
---

<!-- Diapositiva 32 · Gracias (10 s) -->
<div class="py-10 px-12 card-light max-w-xl mx-auto text-center border-sky-300">
<img src="/diagrams/uneg_logo.png" alt="Logo UNEG" class="h-16 w-auto mx-auto mb-4 object-contain" />
<h1 class="text-4xl font-black text-[#1b365d] tracking-tight mb-2">MUCHAS GRACIAS</h1>
<p class="text-sm font-semibold text-slate-600 mb-6">
Quedo atento a las observaciones y preguntas del honorable jurado.
</p>
<div class="p-3 bg-sky-50 rounded-xl border border-sky-200 text-xs font-medium text-slate-700">
<strong>Br. Héctor Tovar</strong> · <a href="mailto:hector.tovar@ejemplo.uneg.edu.ve" class="text-sky-700 font-bold">Ingeniería en Informática · UNEG</a>
</div>
</div>

<!--
Guion (10 s): "Agradezco al jurado su atención, a mi tutora, a la UNEG y a mi familia. Quedo atento a sus preguntas."
-->

---
layout: default
title: "B1 · Matriz de Casos de Ensayo (Respaldo)"
class: backup-slide
---

<!-- B1: Matriz de casos de ensayo (extracto CSV) y tabla de sujetos por entorno -->
<div class="h-full flex flex-col justify-between">
<div class="flex items-center justify-between pb-2 border-b border-amber-300">
<div class="flex items-center gap-2 text-xs font-bold text-amber-800">
<span class="px-2 py-0.5 rounded bg-amber-200 text-amber-900 font-black">RESPALDO B1</span>
Matriz de Casos de Ensayo y Sujetos
</div>
<span class="text-xs font-mono font-bold text-slate-500">B1 / B10</span>
</div>
<div class="my-auto max-w-4xl mx-auto w-full space-y-4">
<div class="card-light p-4 text-xs">
<table class="w-full text-left">
<thead class="bg-slate-100 font-bold text-slate-800">
<tr>
<th class="p-2">Sujeto</th>
<th class="p-2">Rol / Perfil</th>
<th class="p-2">Intentos Genuinos</th>
<th class="p-2">Ataques Foto</th>
<th class="p-2">Ataques Video</th>
<th class="p-2">Total Ensayos</th>
</tr>
</thead>
<tbody class="divide-y divide-slate-100 text-slate-700">
<tr>
<td class="p-2 font-bold">Investigador</td>
<td class="p-2">Usuario Enrolado</td>
<td class="p-2">52</td>
<td class="p-2">54</td>
<td class="p-2">49</td>
<td class="p-2 font-bold">155</td>
</tr>
<tr>
<td class="p-2 font-bold">Hermano</td>
<td class="p-2 text-amber-800 font-semibold">Impostor Consanguíneo</td>
<td class="p-2">0 (113 impostor)</td>
<td class="p-2">0</td>
<td class="p-2">0</td>
<td class="p-2 font-bold">113</td>
</tr>
<tr>
<td class="p-2 font-bold">Voluntario UNEG</td>
<td class="p-2">Usuario Enrolado</td>
<td class="p-2">52</td>
<td class="p-2">53</td>
<td class="p-2">48</td>
<td class="p-2 font-bold">153</td>
</tr>
<tr class="font-extrabold bg-slate-50">
<td class="p-2">Total Banco</td>
<td class="p-2">3 Sujetos</td>
<td class="p-2">104</td>
<td class="p-2">107</td>
<td class="p-2">97</td>
<td class="p-2 text-sky-800">421</td>
</tr>
</tbody>
</table>
</div>
</div>
<div class="text-center text-[11px] text-slate-400">Extracto de ensayos.csv (Fuente: Anexo C y Tabla 3.2 de la tesis)</div>
</div>

---
layout: default
title: "B2 · Tabla 6 Completa (Respaldo)"
class: backup-slide
---

<!-- B2: Tabla 6 completa (11 indicadores) -->
<div class="h-full flex flex-col justify-between">
<div class="flex items-center justify-between pb-2 border-b border-amber-300">
<div class="flex items-center gap-2 text-xs font-bold text-amber-800">
<span class="px-2 py-0.5 rounded bg-amber-200 text-amber-900 font-black">RESPALDO B2</span>
Tabla 6 Completa: 11 Indicadores de Desempeño
</div>
<span class="text-xs font-mono font-bold text-slate-500">B2 / B10</span>
</div>
<div class="my-auto max-w-4xl mx-auto w-full">
<div class="grid grid-cols-3 gap-3 text-xs">
<div class="p-3 bg-white rounded border border-slate-200"><span class="text-slate-500 block">Exactitud (Accuracy):</span><strong class="text-sm text-slate-900">95.72%</strong></div>
<div class="p-3 bg-white rounded border border-slate-200"><span class="text-slate-500 block">Especificidad Global:</span><strong class="text-sm text-emerald-700">99.37%</strong></div>
<div class="p-3 bg-white rounded border border-slate-200"><span class="text-slate-500 block">Sensibilidad (Recall):</span><strong class="text-sm text-slate-900">84.62%</strong></div>
<div class="p-3 bg-white rounded border border-slate-200"><span class="text-slate-500 block">Precisión (PPV):</span><strong class="text-sm text-slate-900">97.78%</strong></div>
<div class="p-3 bg-white rounded border border-slate-200"><span class="text-slate-500 block">F1-Score:</span><strong class="text-sm text-slate-900">0.9072</strong></div>
<div class="p-3 bg-white rounded border border-slate-200"><span class="text-slate-500 block">APCER (Ataque Aceptado):</span><strong class="text-sm text-emerald-700">0.98%</strong></div>
<div class="p-3 bg-white rounded border border-slate-200"><span class="text-slate-500 block">BPCER (Rechazo Genuino):</span><strong class="text-sm text-amber-700">15.38%</strong></div>
<div class="p-3 bg-white rounded border border-slate-200"><span class="text-slate-500 block">FMR (Falsa Coincidencia):</span><strong class="text-sm text-emerald-700">0.00% (0/113)</strong></div>
<div class="p-3 bg-white rounded border border-slate-200"><span class="text-slate-500 block">FNMR (Falso Rechazo):</span><strong class="text-sm text-amber-700">15.38% (16/104)</strong></div>
</div>
</div>
<div class="text-center text-[11px] text-slate-400">Tabla 6 de la tesis: Resumen consolidado bajo normas ISO/IEC 19795-1 y 30107-3</div>
</div>

---
layout: default
title: "B3 · Tabla 10 LFW (Respaldo)"
class: backup-slide
---

<!-- B3: Tabla 10 (LFW) con intervalos de confianza -->
<div class="h-full flex flex-col justify-between">
<div class="flex items-center justify-between pb-2 border-b border-amber-300">
<div class="flex items-center gap-2 text-xs font-bold text-amber-800">
<span class="px-2 py-0.5 rounded bg-amber-200 text-amber-900 font-black">RESPALDO B3</span>
Tabla 10 LFW: Intervalos de Confianza al 95% (Wilson)
</div>
<span class="text-xs font-mono font-bold text-slate-500">B3 / B10</span>
</div>
<div class="my-auto max-w-4xl mx-auto w-full card-light p-4 text-xs">
<table class="w-full text-left">
<thead class="bg-slate-100 font-bold text-slate-800">
<tr>
<th class="p-2">Métrica</th>
<th class="p-2">Literatura (d &lt; 0.68)</th>
<th class="p-2">FaceSentinel (d &lt; 0.60)</th>
<th class="p-2">IC 95% (Wilson d &lt; 0.60)</th>
</tr>
</thead>
<tbody class="divide-y divide-slate-100 text-slate-700">
<tr>
<td class="p-2 font-bold">FMR (Falsa Coincidencia)</td>
<td class="p-2 text-red-600 font-bold">9.28% (45/485)</td>
<td class="p-2 text-emerald-700 font-bold">3.71% (18/485)</td>
<td class="p-2 font-mono">[2.36%, 5.79%]</td>
</tr>
<tr>
<td class="p-2 font-bold">FNMR (Falso Rechazo)</td>
<td class="p-2">19.68% (97/493)</td>
<td class="p-2 text-amber-700 font-bold">22.92% (113/493)</td>
<td class="p-2 font-mono">[19.42%, 26.83%]</td>
</tr>
<tr>
<td class="p-2 font-bold">Exactitud Global</td>
<td class="p-2">85.48%</td>
<td class="p-2">86.61%</td>
<td class="p-2 font-mono">[84.32%, 88.62%]</td>
</tr>
<tr>
<td class="p-2 font-bold">EER (Equal Error Rate)</td>
<td class="p-2">-</td>
<td class="p-2 font-bold text-sky-800">16.66%</td>
<td class="p-2 font-mono">En d ≈ 0.64</td>
</tr>
</tbody>
</table>
</div>
<div class="text-center text-[11px] text-slate-400">Prueba McNemar FMR: χ² = 25.04, p &lt; 0.001 (Reducción estadísticamente significativa)</div>
</div>

---
layout: default
title: "B4 · Tabla 9.1 SSO (Respaldo)"
class: backup-slide
---

<!-- B4: Tabla 9.1 (resumen de los 44 eventos del SSO) -->
<div class="h-full flex flex-col justify-between">
<div class="flex items-center justify-between pb-2 border-b border-amber-300">
<div class="flex items-center gap-2 text-xs font-bold text-amber-800">
<span class="px-2 py-0.5 rounded bg-amber-200 text-amber-900 font-black">RESPALDO B4</span>
Tabla 9.1: Registro Detallado de los 44 Eventos SSO
</div>
<span class="text-xs font-mono font-bold text-slate-500">B4 / B10</span>
</div>
<div class="my-auto max-w-4xl mx-auto w-full card-light p-4 text-xs">
<table class="w-full text-left">
<thead class="bg-slate-100 font-bold text-slate-800">
<tr>
<th class="p-2">Categoría</th>
<th class="p-2">Eventos</th>
<th class="p-2">Concedidos</th>
<th class="p-2">Denegados</th>
<th class="p-2">Observaciones Técnicas</th>
</tr>
</thead>
<tbody class="divide-y divide-slate-100 text-slate-700">
<tr>
<td class="p-2 font-bold">Estudiantes UNEG</td>
<td class="p-2">29</td>
<td class="p-2 text-emerald-700 font-bold">28</td>
<td class="p-2 text-amber-700">1</td>
<td class="p-2">Denegado por parpadeo incompleto; éxito a los 6 s</td>
</tr>
<tr>
<td class="p-2 font-bold">Investigador (Control)</td>
<td class="p-2">10</td>
<td class="p-2 text-emerald-700 font-bold">10</td>
<td class="p-2">0</td>
<td class="p-2">100% efectividad en canal WebSocket</td>
</tr>
<tr>
<td class="p-2 font-bold text-red-700">No Enrolados</td>
<td class="p-2">3</td>
<td class="p-2">0</td>
<td class="p-2 text-emerald-700 font-bold">3</td>
<td class="p-2">Distancias 0.63, 0.65 y 0.71 (rechazados)</td>
</tr>
<tr>
<td class="p-2 font-bold text-purple-700">Ataque Video Celular</td>
<td class="p-2">2</td>
<td class="p-2">0</td>
<td class="p-2 text-emerald-700 font-bold">2</td>
<td class="p-2">Superó EAR y LBP; detenido por filtro FFT 2D</td>
</tr>
</tbody>
</table>
</div>
<div class="text-center text-[11px] text-slate-400">Total: 44 eventos registrados en bitácora local y notarizados en Geth</div>
</div>

---
layout: default
title: "B5 · Modelos y Diagramas (Respaldo)"
class: backup-slide
---

<!-- B5: Figura 3 (modelo entidad-relación) y Figura 4 (árbol de decisión de seguridad) -->
<div class="h-full flex flex-col justify-between">
<div class="flex items-center justify-between pb-2 border-b border-amber-300">
<div class="flex items-center gap-2 text-xs font-bold text-amber-800">
<span class="px-2 py-0.5 rounded bg-amber-200 text-amber-900 font-black">RESPALDO B5</span>
Figura 3 (ERD) y Figura 4 (Árbol de Decisión PAD)
</div>
<span class="text-xs font-mono font-bold text-slate-500">B5 / B10</span>
</div>
<div class="my-auto max-w-4xl mx-auto w-full grid grid-cols-2 gap-4 text-xs">
<div class="card-light p-4">
<span class="font-bold text-sky-800 block mb-2">Entidades Principales (SQLite)</span>
<ul class="space-y-1 text-slate-700 m-0 p-0 list-none font-mono text-[11px]">
<li>• Users (id, username, password_hash, role_id)</li>
<li>• Roles (id, name, permissions)</li>
<li>• Cameras (id, ip, location, security_level)</li>
<li>• AccessLogs (id, user_hash, granted, tx_hash)</li>
</ul>
</div>
<div class="card-light p-4">
<span class="font-bold text-purple-800 block mb-2">Árbol de Decisión por Nivel PAD</span>
<ul class="space-y-1 text-slate-700 m-0 p-0 list-none text-[11px]">
<li>• Nivel 1: Sin PAD (solo ArcFace, áreas públicas)</li>
<li>• Nivel 2: EAR (Borde)</li>
<li>• Nivel 3: EAR + LBP + FFT 2D (Físico institucional)</li>
<li>• Nivel 4: EAR + LBP + FFT + Reto Activo (SSO Web)</li>
</ul>
</div>
</div>
<div class="text-center text-[11px] text-slate-400">Modelos conceptuales de arquitectura de datos y políticas de seguridad</div>
</div>

---
layout: default
title: "B6 · Contrato AccessRegistry (Respaldo)"
class: backup-slide
---

<!-- B6: Contrato AccessRegistry.sol (extracto) -->
<div class="h-full flex flex-col justify-between">
<div class="flex items-center justify-between pb-2 border-b border-amber-300">
<div class="flex items-center gap-2 text-xs font-bold text-amber-800">
<span class="px-2 py-0.5 rounded bg-amber-200 text-amber-900 font-black">RESPALDO B6</span>
Contrato AccessRegistry.sol (Funciones Clave)
</div>
<span class="text-xs font-mono font-bold text-slate-500">B6 / B10</span>
</div>
<div class="my-auto max-w-4xl mx-auto w-full text-xs">

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract AccessRegistry {
    address public owner;
    mapping(address => bool) public authorizedGateways;

    event AccessAttempt(bytes32 indexed userHash, bool granted, uint256 timestamp);

    function recordAccess(bytes32 _userHash, bytes32 _vectorHash, bool _granted,
                          string calldata _deviceId, uint16 _score) external onlyGateway {
        records.push(AuthRecord(_userHash, _vectorHash, block.timestamp, _granted, _deviceId, _score));
        emit AccessAttempt(_userHash, _granted, block.timestamp);
    }
}
```

</div>
<div class="text-center text-[11px] text-slate-400">Sin dependencias externas · Consumo de gas constante O(1)</div>
</div>

---
layout: default
title: "B7 · Tablas de Rendimiento (Respaldo)"
class: backup-slide
---

<!-- B7: Tabla 7 y Tabla 8 completas (latencia y notarización) -->
<div class="h-full flex flex-col justify-between">
<div class="flex items-center justify-between pb-2 border-b border-amber-300">
<div class="flex items-center gap-2 text-xs font-bold text-amber-800">
<span class="px-2 py-0.5 rounded bg-amber-200 text-amber-900 font-black">RESPALDO B7</span>
Tablas 7 y 8: Latencia de Pipeline y Notarización Geth
</div>
<span class="text-xs font-mono font-bold text-slate-500">B7 / B10</span>
</div>
<div class="my-auto max-w-4xl mx-auto w-full grid grid-cols-2 gap-4 text-xs">
<div class="card-light p-4">
<span class="font-bold text-slate-800 block mb-2">Desglose de Pipeline (Tabla 7)</span>
<div class="space-y-1 font-mono text-[11px]">
<div>• Borde (EAR + Crop): 6.30 ms (DE 1.2)</div>
<div>• Tránsito Red WAN: 485.79 ms (DE 42.1)</div>
<div>• Servidor (LBP + FFT): 48.10 ms</div>
<div>• Servidor (ArcFace 512D): 142.30 ms</div>
<div>• ChromaDB (HNSW Query): 7.49 ms</div>
<div class="font-bold text-emerald-800 pt-1 border-t">Total: 689.98 ms (&lt; 1000 ms)</div>
</div>
</div>
<div class="card-light p-4">
<span class="font-bold text-slate-800 block mb-2">Notarización Blockchain (Tabla 8)</span>
<div class="space-y-1 font-mono text-[11px]">
<div>• Transacciones analizadas: n = 20</div>
<div>• Tiempo promedio: 1 903.89 ms</div>
<div>• Desviación estándar: 45.20 ms</div>
<div>• Período de bloque Clique: 2.00 s</div>
<div>• Gas por transacción: 207 430 unidades</div>
<div class="font-bold text-sky-800 pt-1 border-t">Modo: Asíncrono no bloqueante</div>
</div>
</div>
</div>
<div class="text-center text-[11px] text-slate-400">Mediciones en banco y red en producción de la UNEG</div>
</div>

---
layout: default
title: "B8 · Equipamiento (Respaldo)"
class: backup-slide
---

<!-- B8: Tabla de equipos (Tabla 4.1) y foto de la cámara -->
<div class="h-full flex flex-col justify-between">
<div class="flex items-center justify-between pb-2 border-b border-amber-300">
<div class="flex items-center gap-2 text-xs font-bold text-amber-800">
<span class="px-2 py-0.5 rounded bg-amber-200 text-amber-900 font-black">RESPALDO B8</span>
Equipamiento Experimental (Tabla 4.1)
</div>
<span class="text-xs font-mono font-bold text-slate-500">B8 / B10</span>
</div>
<div class="my-auto max-w-4xl mx-auto w-full card-light p-4 text-xs">
<table class="w-full text-left">
<thead class="bg-slate-100 font-bold text-slate-800">
<tr>
<th class="p-2">Componente</th>
<th class="p-2">Modelo / Especificación</th>
<th class="p-2">Función en el Sistema</th>
</tr>
</thead>
<tbody class="divide-y divide-slate-100 text-slate-700">
<tr>
<td class="p-2 font-bold">Cámara Analógica Institucional</td>
<td class="p-2">Hikvision DS-2CE66C0T-IRM (720p)</td>
<td class="p-2">Muestra suministrada por UNEG para análisis de hardware</td>
</tr>
<tr>
<td class="p-2 font-bold">Cámara Banco Equivalente</td>
<td class="p-2">HiLook THC-B110 1MP (Sensor CMOS)</td>
<td class="p-2">Captura de video en banco experimental</td>
</tr>
<tr>
<td class="p-2 font-bold">DVR Equivalente</td>
<td class="p-2">Hikvision DS-7104HGHI-F1</td>
<td class="p-2">Codificación H.264 y streaming RTSP/TCP</td>
</tr>
<tr>
<td class="p-2 font-bold">Servidor Central FaceSentinel</td>
<td class="p-2">Intel Core i5, 16GB RAM, Docker Linux</td>
<td class="p-2">API FastAPI, ArcFace, ChromaDB, Nodo Geth</td>
</tr>
</tbody>
</table>
</div>
<div class="text-center text-[11px] text-slate-400">Validación técnica de compatibilidad por protocolos abiertos</div>
</div>

---
layout: default
title: "B9 · Tabla 11 Completa (Respaldo)"
class: backup-slide
---

<!-- B9: Tabla 11 completa (cumplimiento de requerimientos) -->
<div class="h-full flex flex-col justify-between">
<div class="flex items-center justify-between pb-2 border-b border-amber-300">
<div class="flex items-center gap-2 text-xs font-bold text-amber-800">
<span class="px-2 py-0.5 rounded bg-amber-200 text-amber-900 font-black">RESPALDO B9</span>
Tabla 11 Completa: Matriz de Requerimientos y Evidencias
</div>
<span class="text-xs font-mono font-bold text-slate-500">B9 / B10</span>
</div>
<div class="my-auto max-w-4xl mx-auto w-full card-light p-4 text-xs">
<div class="grid grid-cols-2 gap-4">
<div>
<span class="font-bold text-sky-800 block mb-2">Requerimientos Funcionales (RF)</span>
<div class="space-y-1 text-[11px] text-slate-700">
<div>• RF1: Captura y streaming RTSP (✔ S-RES)</div>
<div>• RF2: Embudo PAD multicapa (✔ S-RES, S-UNEG)</div>
<div>• RF3: Extracción ArcFace 512D (✔ S-RES, LFW)</div>
<div>• RF4: Búsqueda vectorial HNSW (✔ S-RES)</div>
<div>• RF5: Notarización en Geth (✔ S-CADENA)</div>
<div>• RF6: SSO y M2M con JWT (✔ S-UNEG)</div>
</div>
</div>
<div>
<span class="font-bold text-emerald-800 block mb-2">Requerimientos No Funcionales (RNF)</span>
<div class="space-y-1 text-[11px] text-slate-700">
<div>• RNF1: Latencia Servidor &lt; 500 ms (✔ 198 ms)</div>
<div>• RNF2: Latencia Total &lt; 1000 ms (✔ 690 ms)</div>
<div>• RNF3: Privacidad SHA-256 + sal (✔ Código)</div>
<div>• RNF4: Resiliencia ante caída de red (✔ Local log)</div>
<div>• RNF5: 100% Software Libre (✔ Stack OSS)</div>
</div>
</div>
</div>
</div>
<div class="text-center text-[11px] text-slate-400">Verificación exhaustiva certificada</div>
</div>

---
layout: default
title: "B10 · Acta de Conformidad (Respaldo)"
class: backup-slide
---

<!-- B10: Acta de conformidad (Anexo D) -->
<div class="h-full flex flex-col justify-between">
<div class="flex items-center justify-between pb-2 border-b border-amber-300">
<div class="flex items-center gap-2 text-xs font-bold text-amber-800">
<span class="px-2 py-0.5 rounded bg-amber-200 text-amber-900 font-black">RESPALDO B10</span>
Acta de Conformidad y Aceptación Institucional (Anexo D)
</div>
<span class="text-xs font-mono font-bold text-slate-500">B10 / B10</span>
</div>
<div class="my-auto max-w-2xl mx-auto w-full card-light p-6 text-center border-sky-300">
<img src="/diagrams/uneg_logo.png" alt="Logo UNEG" class="h-12 w-auto mx-auto mb-3 object-contain" />
<h3 class="text-sm font-black text-slate-900 uppercase">Dirección de Sistemas Automatizados Inteligentes (UNEG)</h3>
<p class="text-xs text-slate-600 mt-2">
Certificación de pruebas operativas del sistema <strong>FaceSentinel</strong> como IdP para el portal universitario y validación preliminar en entorno institucional.
</p>
<div class="mt-4 p-3 bg-slate-50 rounded-lg border border-slate-200 text-[11px] text-slate-700">
Fecha de suscripción: Octubre de 2026 · Ciudad Guayana, Estado Bolívar
</div>
</div>
<div class="text-center text-[11px] text-slate-400">Documento probatorio consignado en el informe final de Trabajo de Grado</div>
</div>

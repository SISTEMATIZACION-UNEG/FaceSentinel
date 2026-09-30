# FaceSentinel - Presentación de Defensa de Grado (Slidev)

Este directorio contiene las diapositivas de la defensa de grado creadas con [Slidev](https://sli.dev/).

## Estructura

- `slides.md`: Archivo principal con las diapositivas y notas del orador.
- `public/`: Imágenes, logotipos institucionales y diagramas.
- `components/`: Componentes Vue personalizados reutilizables en las diapositivas.
- `styles/index.css`: Estilos personalizados y utilidades visuales.

## Comandos

```bash
# Iniciar servidor de desarrollo con vista en navegador y modo presentador
npm run dev

# Compilar para producción (sitio estático SPA)
npm run build

# Exportar a PDF (documento vectorial)
npm run export

# Exportar a PowerPoint .pptx (para importar en Canva o PowerPoint)
npm run export:pptx

# Exportar cada diapositiva como imagen PNG
npm run export:png
```

## Atajos de Teclado en Modo Presentación
- `Space` / `→`: Siguiente diapositiva o animación.
- `←`: Diapositiva anterior.
- `P`: Abrir vista de presentador (cronómetro + notas + vista previa).
- `D`: Abrir herramientas de dibujo sobre las láminas.
- `O`: Resumen general de todas las diapositivas.

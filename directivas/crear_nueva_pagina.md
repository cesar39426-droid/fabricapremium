# Directiva: Creación de Nuevas Páginas (Estandarización Factory)

## 🎯 Objetivo General
Garantizar que CADA VEZ que un operador o agente cree una PÁGINA NUEVA (`.astro`) en la fábrica, esta nazca automáticamente integrada con los estándares inmersivos premium de la marca (Layout base con GSAP/Lenis, WebGL Shader de fondo, y la estructura de componentes de UI).

## ⚙️ Bucle Central de Generación
El script de automatización `scripts/crear_nueva_pagina.py` será el único encargado de crear nuevas vistas.

El CLI automatizado hará lo siguiente:
1. Recibir el nombre de la nueva página (ej. `python scripts/crear_nueva_pagina.py contacto`).
2. Validar que no exista un archivo `contacto.astro` en `src/pages/` para evitar sobreescritura accidental.
3. Inyectar un boilerplate premium que importe e implemente por defecto:
   - `<Layout />` (Motor de GSAP, tipografías y Lenis smooth scroll).
   - Un componente de fondo inmersivo (ej. `WebGLShader` o `AnoAI`) ya configurado con `client:only="react"`.
   - Contenedores semánticos (`<main>`, `<section>`) con clases base de Tailwind que soporten z-index sobre el WebGL.
   - Un componente CTA de demostración (ej. `LiquidButton`).

## 🚨 Restricciones y Casos Borde (Trampas Conocidas)
- **Rutas Anidadas:** Si se le pasa una ruta como `servicios/cloud`, el script debe poder crear los subdirectorios dentro de `src/pages/`.
- **Fallas de hidratación React en Astro:** Todo componente de la carpeta `src/components/ui/` que utilice Canvas o Framer Motion debe llevar el flag `client:load` o `client:only="react"` al inyectarse en el boilerplate de `.astro`. El script de Python lo inyecta pre-escrito correctamente para evitar que el desarrollador rompa el SSR.

---
**Status:** [ACTIVE]
**Orquestador:** Agente Arquitecto

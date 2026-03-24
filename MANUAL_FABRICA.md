# 🏭 Manual de Uso — Fábrica Premium V2 (Astro Edition)

Bienvenido a la **Fábrica Premium V2**. Este sistema ha sido diseñado para la generación autónoma y asistida de sitios web de alto rendimiento, utilizando una arquitectura basada en componentes y el stack tecnológico más rápido del mercado.

---

## 🚀 1. El Stack Tecnológico (Canonical)
El núcleo de la fábrica utiliza un conjunto de herramientas de última generación:

*   **Framework**: [Astro 6.x](https://astro.build/) (Islands Architecture para rendimiento extremo).
*   **UI**: [React 19](https://react.dev/) (Para componentes interactivos complejos).
*   **Animación**: [GSAP 3.x](https://gsap.com/) + [ScrollTrigger](https://gsap.com/scrolltrigger/) (Revelaciones y efectos).
*   **Scroll**: [Lenis](https://lenis.darkroom.engineering/) (Scroll suave y natural).
*   **3D (Opcional)**: Three.js + React Three Fiber (Para experiencias inmersivas).

---

## 📁 2. Estructura del Proyecto
La arquitectura se organiza de la siguiente manera:

```bash
fabrica-premium/
├── public/                 # Archivos estáticos (Logo, imágenes, favicons)
├── src/
│   ├── components/         # Bloques de construcción (.astro, .jsx)
│   ├── layouts/            # Plantillas maestras (Layout.astro)
│   ├── pages/              # Páginas del sitio (index.astro)
│   ├── styles/             # CSS Global (global.css) e Industrial Tokens
├── specs/                  # Especificaciones de diseño para agentes
├── dist/                   # Build final (lo que se sube a Hostinger)
├── package.json            # Gestión de dependencias y scripts
└── astro.config.mjs        # Configuración del ecosistema
```

---

## 🛠️ 3. Flujo de Trabajo (Protocolo de Fábrica)

### Paso A: Definición en `specs/`
Antes de crear un componente, se debe definir su objetivo y estilo en un archivo `.md` dentro de `specs/`. Esto sirve como la "orden de trabajo" para los agentes desarrolladores.

### Paso B: Creación de Componentes
Cada bloque (Hero, Footer, Servicios) se desarrolla en `src/components/`.
> [!TIP]
> Usa **Scoped Styles** (`<style>` dentro del archivo `.astro`) para evitar conflictos y mantener el código limpio.

### Paso C: Ensamblaje Global
La página principal `src/pages/index.astro` importa los componentes y define su orden:
```astro
---
import Layout from "../layouts/Layout.astro";
import Hero from "../components/Hero.astro";
import Servicios from "../components/Servicios.astro";
---
<Layout>
  <Hero />
  <Servicios />
</Layout>
```

### Paso D: Construcción y Despliegue
Para preparar el sitio para Hostinger, ejecuta:
```bash
npm run build
```
El contenido de la carpeta `dist/` es el que debe subirse al servidor (`public_html`).

---

## 🎨 4. Design System (Industrial Palette)
La fábrica utiliza **Tokens de Diseño** para mantener la consistencia. Estos se encuentran en `src/styles/global.css`:

*   `--primary-blue`: #0F172A (Fondo industrial).
*   `--safety-orange`: #F97316 (Acentos de seguridad y acción).
*   `--industry-slate`: #334155 (Textos secundarios).
*   `--grad-premium`: Degradado de azul a naranja para máxima visibilidad.

---

## 🤖 5. Directivas para Agentes (Protocolos de Modificación)
Si vas a pedirle a un Agente (como Antigravity) que modifique el sitio, recuerda:

1.  **Consultar Directiva**: El agente SIEMPRE debe leer `directivas/configuracion_fabrica_astro_SOP.md` antes de actuar.
2.  **No Monolitos**: No permitas archivos HTML gigantes. Todo debe estar en componentes separados.
3.  **Auditoría de Performance**: Tras cada cambio, pide al agente que verifique el **LCP**, **CLS** e **INP**.

---

## 🗂️ 6. Catálogo de Directivas Activas
Las siguientes reglas operativas (SOPs) rigen el comportamiento de la fábrica:

<!-- DIRECTIVAS_START -->
| Directiva | Propósito | Link |
| :--- | :--- | :--- |
| Actualización de Manual con Directivas | Mantener sincronizada la lista de directivas operativas (SOPs) dentro del `MANUAL_FABRICA.md` y `cheatsheet-empleados... | [Doc](../directivas/actualizacion_manual_directivas_SOP.md) |
| Arquitectura de Fábrica de Sitios V2 (2026) | Producir plataformas web inmersivas de alto rendimiento (60fps) bajo el modelo de **Servicio Productizado** para PyME... | [Doc](../directivas/fabrica_sistemas_SOP.md) |
| Arquitectura de Plataformas Web Premium | Este SOP es la **Fuente de Verdad actualizada** para cualquier proyecto de construcción de plataforma web corporativa... | [Doc](../directivas/arquitectura_premium_SOP.md) |
| Configuración del Scaffolding Astro para Fábrica Premium v2.0 | Configurar el entorno de desarrollo Astro para la Fábrica Premium, eliminando el ensamblaje manual por Python a favor... | [Doc](../directivas/configuracion_fabrica_astro_SOP.md) |
| Construcción NubeN Digital Vanilla | Generar el sitio web de NubeN en un archivo ÚNICO (HTML+CSS+JS) sin dependencias de compilación (frameworks), usando ... | [Doc](../directivas/nuben_vanilla_SOP.md) |
| DIRECTIVA DE ELEVACIÓN VISUAL  NIVEL ANTIGRAVITY | Elevar el estándar visual de las variantes generadas para que alcancen un nivel de "clase mundial" (estilo antigravit... | [Doc](../directivas/nivel-visual-objetivo.md) |
| ESTÁNDAR DE EFECTOS PREMIUM  FÁBRICA WEB | El output de cada variante debe ser indistinguible de un sitio terminado. El cliente abre el archivo y dice "esto es ... | [Doc](../directivas/estandar-efectos-premium.md) |
| Fondos Especializados por Industria | Garantizar que el background animado de cada sitio refleje la identidad visual específica de la industria del cliente... | [Doc](../directivas/fondos-por-industria.md) |
| Integración con Stitch (MCP) | Garantizar que los tokens visuales (colores, tipografía, espaciados y componentes) de cada proyecto provengan de un d... | [Doc](../directivas/integracion_stitch_SOP.md) |
| Maestro Fábrica Web UX v3 | Este skill define el proceso maestro para la generación de landing pages de alta conversión y nivel visual premium. | [Doc](../directivas/maestro-fabrica-web-ux-v3.md) |
| Prompt Maestro 3 Ingeniero de Conversión Front-end y Lógica de Negocio (The UIUX Engine) | Este prompt despliega el motor principal de generación de código frontal. Recibe la encomienda de poblar la estructur... | [Doc](../directivas/prompt_maestro_3_ui_ux.md) |
| Qué es un Sitio Web Viviente | Un sitio que responde a la presencia del usuario. Que tiene peso, profundidad, elasticidad. Todo lo que el visitante ... | [Doc](../directivas/efectos-living-web.md) |
| Tipos de Entregable  Definiciones Exactas | LANDING PAGE DE CONVERSIÓN (el entregable estándar): Es una página completa de una sola URL con múltiples secciones d... | [Doc](../directivas/fabrica-base.md) |
| Upgrade de Conversión NubeN | Implementar mejoras de conversión en el sitio NubeN actual (Astro exportado/HTML) sin sobreescribir el funcionamiento... | [Doc](../directivas/upgrade_conversion_nuben_SOP.md) |
<!-- DIRECTIVAS_END -->

---

## 🔧 7. Comandos útiles
Dependiendo de la fase del proyecto (desarrollo web o automatización), utiliza los siguientes comandos:

### Desarrollo Frontend (Astro)
*   `npm run dev` — Inicia el servidor de desarrollo local.
*   `npm run build` — Genera el sitio estático para producción.
*   `npm run preview` — Prueba localmente el build final.

### Automatización y Herramientas (Python)
 *   `python scripts/actualizar_index_manual.py` — Sincroniza el catálogo de directivas en el manual.
*   `python scripts/integracion_stitch.py` — Sincroniza los tokens de diseño con el proyecto.
*   `python scripts/build_nuben_vanilla.py` — Genera el build específico para NubeN Digital.

---

> [!IMPORTANT]
> **Hostinger Auto-Deploy**: Cualquier cambio pusheado a la rama `main` en GitHub se verá reflejado en el sitio [lightgray-snail-450283.hostingersite.com](https://lightgray-snail-450283.hostingersite.com/) automáticamente una vez configurado el Build Script en el panel del hosting.

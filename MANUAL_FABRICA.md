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

## 🔧 6. Comandos útiles
*   `npm run dev` — Inicia el servidor de desarrollo local.
*   `npm run build` — Genera el sitio estático para producción.
*   `npm run preview` — Prueba localmente el build final.

---

> [!IMPORTANT]
> **Hostinger Auto-Deploy**: Cualquier cambio pusheado a la rama `main` en GitHub se verá reflejado en el sitio [lightgray-snail-450283.hostingersite.com](https://lightgray-snail-450283.hostingersite.com/) automáticamente una vez configurado el Build Script en el panel del hosting.

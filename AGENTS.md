# AGENTS.md: Reglas de Orquestación para Fábrica Premium

## 🤖 Roles del Sistema (Arquitectura de Islas Astro)
- **Agente Arquitecto**: Solo él define la estructura de `/src/pages/` y `/src/layouts/`.
- **Agentes de Sección**: Encargados de editar componentes `.astro` y `.jsx` en `/src/components/`.
- **Agente Auditor**: Valida el INP (<200ms) y el CLS (<0.1) mediante Lighthouse y `browser_subagent`.

## 📂 Estructura de Trabajo
- `/src/components/`: Componentes modulares (Hero, Servicios, etc.).
- `/src/layouts/`: Plantilla maestra `Layout.astro`.
- `/specs/`: Requerimientos narrativos por sección.

## 📜 Protocolo de Modificación
1. **Lectura de Spec**: Leer `specs/{seccion}.md`.
2. **Edición de Componente**: Modificar `src/components/{seccion}.astro` o `.jsx`.
3. **Sincronización**: Git commit & push. Astro re-compila automáticamente en dev.
4. **Validación**: Correr auditoría de INP y Performance.

## 🎨 Guía de Estilo Premium (Tokens 2026)
- **Glassmorphism**: `backdrop-filter: blur(14px) saturate(160%)`.
- **Palette**: Primario `#0F172A`, Acento `#F97316` (Zárate Industrial).
- **Animations**: GSAP `ScrollTrigger` + View Transitions API.

# Mission Spec: NubeN Evolution 2026

## 🎯 Objetivo
Transformar gestionemocional.shop (NubeN) de una landing funcional a una **Plataforma de Crecimiento Inmersiva** (Living Web) que represente el tope de gama de la Fábrica Premium.

## 🛠️ Stack Arquitectónico
- **Core**: Astro 6.x (Island Architecture).
- **Visuals**: GSAP + ScrollTrigger para revelaciones cinemáticas.
- **Interactivity**: React 19 para la calculadora de ROI y componentes dinámicos.
- **Motion**: Lenis Scroll para suavidad industrial.

## 🎨 Design Upgrade (Tokens 2026)
- **Primary**: #0F172A (Deep Slate).
- **Accent**: #F97316 (Safety Orange) - Usar para CTAs y elementos críticos.
- **Surface**: Glassmorphism (blur: 20px, saturate: 180%) para el Header y tarjetas.
- **Efecto Crítico**: Corregir visibilidad del logo (Fondo con glow o logo en blanco puro con sombra proyectada).

## 🧩 Estructura de Secciones (The Global Flow)
1.  **Header Vivo**: Transparente -> Glassmorphism al scrollear.
2.  **Hero V6 (Cinematic)**: 
    - Fondo de partículas o shader (Industrial Shader #1).
    - Titular con revelado por palabras (GSAP).
    - El logo debe ser la estrella.
3.  **Trust Bar**: Marcas y socios con scroll infinito suave.
4.  **Bento Services**: Visualización de servicios usando la arquitectura de Bento Grid.
5.  **Proceso Industrial**: Línea de tiempo interactiva (24h -> 72h).
6.  **Calculadora de Impacto**: Componente interactivo para que el usuario estime su ROI.
7.  **Social Proof**: Testimonios en tarjetas Spotlight.
8.  **CTA Final**: "Iniciar Protocolo de Crecimiento".

## 🚀 Protocolo de Ejecución
1.  **Componente Hero**: Refactorizar `src/components/Hero.astro` para maximizar el impacto visual.
2.  **Integración de Assets**: Asegurar que `nuben-logo.png` sea visible.
3.  **Build & Deploy**: Testeo de performance (Lighthouse > 95).

# Directiva: Landing Page Nova Cloud (B2B Tech SOP)

## 🎯 Objetivo
Desplegar una landing page de alta conversión para Nova Cloud, posicionando a la marca como socio estratégico en IA y automatización.

## ⚙️ Bucle Central (Estructura Nova)
1. **Hero de Impacto:** H1 con tipografía `Syne`, degradado eléctrico y social proof inmediato.
2. **La Fábrica Digital (Soluciones):** Grid de 3 columnas con animaciones `stagger` de GSAP para servicios de E-commerce, IA y Cloud.
3. **Filosofía de Negocio:** Diferenciación clara ("No somos consultores") con cita final resaltada.
4. **Captura de Leads (Onboarding):** Formulario robusto con selector de puntos de dolor para pre-calificación en CRM.

## 🚨 Restricciones y Casos Borde
- **Animaciones GSAP:** Deben registrarse dentro del listener `astro:page-load` para asegurar compatibilidad con View Transitions.
- **Glassmorphism:** Usar `backdrop-blur-xl` y bordes sutiles `white/10` para mantener el estilo premium sobre el fondo oscuro `#050810`.
- **Formulario:** El botón debe usar la paleta de acento `#00C2FF` y tener un estado `active:scale-[0.98]` para feedback táctil.

---
**Status:** [ACTIVE]
**Orquestador:** Agente Arquitecto / Copywriter B2B

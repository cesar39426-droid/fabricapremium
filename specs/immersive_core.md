# SPEC: Immersive Core & SVG Transitions (V1)

## 🎯 Objetivo
Implementar transiciones de sección fluidas utilizando máscaras SVG que se expanden/contraen con el scroll, creando un efecto de "revelación" inmersiva.

## 🛠️ Requerimientos Técnicos (NotebookLM Standard)
- **Tecnología**: GSAP ScrollTrigger + SVG Clipping Paths.
- **Eficiencia**: Debe tener un costo de CPU < 5% en mobile.
- **Estética**: Bordes orgánicos (curvas de Bézier) en lugar de cortes rectos.

## 📐 Diseño
- **Dividers**: Intercalar entre secciones (ej. entre Hero e Innovation).
- **Masking**: El contenedor de la sección siguiente estará inicialmente oculto tras una máscara circular o de "onda" que se expande al hacer scroll.

## 📝 Pasos
1. Crear el componente `SectionDivider`.
2. Registrar el plugin `ScrollTrigger` en el orquestador global.
3. Aplicar la animación a los paths SVG.

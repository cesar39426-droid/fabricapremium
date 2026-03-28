import os
import sys

def create_new_page(page_name):
    # 1. Definir rutas relativas
    script_dir = os.path.dirname(os.path.abspath(__file__))
    fabrica_root = os.path.dirname(script_dir)
    pages_dir = os.path.join(fabrica_root, "src", "pages")
    
    # Manejar rutas anidadas (ej: servicios/cloud)
    if not page_name.endswith('.astro'):
        page_name += '.astro'
        
    target_path = os.path.join(pages_dir, page_name)
    target_dir = os.path.dirname(target_path)
    
    # 2. Validaciones
    if not os.path.exists(pages_dir):
        print(f"✖ Error: No se encontró la carpeta 'src/pages/'. Ejecuta esto dentro de la fábrica.")
        sys.exit(1)
        
    if os.path.exists(target_path):
        print(f"✖ Error: La página '{page_name}' ya existe. Abortando para no sobreescribir código.")
        sys.exit(1)
        
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # 3. Formateo y título de página
    title_display = os.path.basename(page_name).replace('.astro', '').replace('-', ' ').title()

    # 4. Plantilla de Estándar de Fábrica (Astro + WebGL + React UI)
    astro_template = f"""---
import Layout from '../layouts/Layout.astro';
import {{ WebGLShader }} from '../components/ui/web-gl-shader';
import {{ LiquidButton }} from '../components/ui/liquid-glass-button';

// Ajusta las importaciones relativas si la página es anidada (ej: ../../)
---

<Layout title="NubeN — {{title_display}}">
  <!-- Fondo Técnico WebGL Premium (z-0) -->
  <div class="fixed inset-0 z-[-10]">
    <WebGLShader client:only="react" />
  </div>

  <main class="relative z-10 w-full min-h-screen flex items-center justify-center text-white overflow-hidden">
    
    <section class="max-w-4xl mx-auto px-6 py-24 text-center">
      <!-- Glow Decorativo -->
      <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-96 h-96 bg-primary/20 blur-[120px] rounded-full pointer-events-none"></div>
      
      <h1 class="text-6xl md:text-8xl font-extrabold tracking-tighter mb-6 relative">
        {title_display}
      </h1>
      
      <p class="text-lg md:text-xl text-white/60 mb-12 max-w-2xl mx-auto">
        Esta página ha sido instanciada con el Sistema Estándar de la Fábrica. 
        WebGL y GSAP están activos y entrelazados.
      </p>

      <div class="flex justify-center flex-wrap gap-4">
        <LiquidButton size="xl" variant="default" client:load>
          Ver Documentación
        </LiquidButton>
      </div>

    </section>
  </main>
</Layout>
"""

    # 5. Escritura del archivo
    print(f"\n[1/2] Generando la página '{page_name}' implementando estándares de la fábrica...")
    try:
        with open(target_path, "w", encoding="utf-8") as file:
            file.write(astro_template)
            
        # Calcular URL tentativa (remover 'src/pages' y '.astro')
        url_path = page_name.replace('.astro', '')
        if url_path == 'index': url_path = '/'
        else: url_path = f"/{url_path}"
        
        print(f"[2/2] Inyección Exitosa.")
        print("---------------------------------------------------------")
        print(f"✅ Página creada: {target_path}")
        print(f"🌐 Disponible en tu entorno de desarrollo en: http://localhost:4321{url_path}")
        print("🔧 Layout, WebGL Shader y componentes base ya están envolviendo el HTML.")
        print("---------------------------------------------------------\n")
    except Exception as e:
        print(f"✖ Error crítico escribiendo la página Astro: {{e}}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python crear_nueva_pagina.py <nombre-de-la-pagina>")
        print("Ej:  python crear_nueva_pagina.py acerca-de")
        print("Ej:  python crear_nueva_pagina.py industrias/petroleo")
        sys.exit(1)
        
    page = sys.argv[1]
    create_new_page(page)

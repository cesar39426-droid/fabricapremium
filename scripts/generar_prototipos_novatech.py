import os
import json

def generate_prototypes():
    output_dir = r"c:\Users\PC23\creador de sitios\clientes\novatech-confort\prototipos"
    os.makedirs(output_dir, exist_ok=True)
    
    # Base structural template using GSAP, Tailwind (via CDN) and WebGL Shader placeholders
    template = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NovaTech Confort - {v_name}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Space+Grotesk:wght@500;700;800&display=swap');
        
        :root {{
            --primary: #2563EB;
            --secondary: #F59E0B;
            --bg-body: {v_bg};
            --text-base: {v_text};
            --shader-opacity: {v_opacity};
        }}
        
        body {{
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-body);
            color: var(--text-base);
            overflow-x: hidden;
            margin: 0;
            cursor: none;
        }}
        h1, h2, h3, .heading {{ font-family: 'Space Grotesk', sans-serif; }}
        
        /* Custom Cursor */
        #cursor-dot {{
            position: fixed; width: 8px; height: 8px; background: var(--primary);
            border-radius: 50%; pointer-events: none; z-index: 9999;
            transform: translate(-50%, -50%);
        }}
        #cursor-ring {{
            position: fixed; width: 40px; height: 40px; border: 1px solid rgba(37,99,235,0.4);
            border-radius: 50%; pointer-events: none; z-index: 9998;
            transform: translate(-50%, -50%); transition: width 0.2s, height 0.2s;
        }}
        
        /* 3D Tilt Card */
        .tilt-card {{
            transition: transform 0.1s; transform-style: preserve-3d;
            background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1);
            backdrop-filter: blur(10px); border-radius: 16px;
        }}
        
        /* Magnetic Button */
        .magnetic-btn {{
            display: inline-block; padding: 12px 24px; background: var(--primary);
            color: white; border-radius: 12px; font-weight: 600; text-decoration: none;
            transition: transform 0.2s;
        }}
        
        /* Shader Background Placeholder */
        #shader-bg {{
            position: absolute; top: 0; left: 0; width: 100%; height: 100%;
            z-index: -1; opacity: var(--shader-opacity);
            background: radial-gradient(circle at 50% 50%, rgba(37,99,235,var(--shader-opacity)), transparent 60%);
        }}
        
        .clip-reveal {{ clip-path: inset(0 100% 0 0); }}
        
        @media (max-width: 768px) {{
            body {{ cursor: auto; }}
            #cursor-dot, #cursor-ring, #shader-bg {{ display: none; }}
        }}
    </style>
</head>
<body>
    <div id="cursor-dot"></div>
    <div id="cursor-ring"></div>

    <!-- HERO SECTION -->
    <section class="relative min-h-screen flex items-center justify-center p-6 lg:p-24 overflow-hidden">
        <div id="shader-bg"></div>
        <div class="relative z-10 grid lg:grid-cols-2 gap-12 max-w-7xl mx-auto w-full">
            <div class="flex flex-col justify-center order-2 lg:order-1">
                <div class="inline-block px-4 py-1 rounded-full border border-blue-500/30 text-blue-500 text-sm font-bold mb-6 w-max">
                    • ECOSISTEMAS INTELIGENTES
                </div>
                <h1 class="text-5xl lg:text-7xl font-bold mb-6 leading-tight heading hover-skew">
                    Tecnología <span class="text-blue-600">inteligente</span> para un hogar más cómodo
                </h1>
                <p class="text-xl opacity-80 mb-8 max-w-xl">
                    Descubrí nuestra nueva línea de productos premium diseñados para unificar y simplificar cada rincón de tu hogar.
                </p>
                <div class="flex flex-wrap gap-4 mb-12">
                    <a href="#" class="magnetic-btn">Explorar Catálogo →</a>
                    <a href="#" class="magnetic-btn" style="background: transparent; border: 1px solid #2563EB; color: #2563EB;">Hablanos por WhatsApp</a>
                </div>
                
                <div class="grid grid-cols-2 lg:grid-cols-4 gap-6">
                    <div><div class="text-3xl font-bold text-amber-500 counter">500</div><div class="text-xs uppercase tracking-widest opacity-60">Hogares</div></div>
                    <div><div class="text-3xl font-bold text-amber-500 counter">18</div><div class="text-xs uppercase tracking-widest opacity-60">Meses gtía</div></div>
                    <div><div class="text-3xl font-bold text-amber-500 counter">24</div><div class="text-xs uppercase tracking-widest opacity-60">Hs entrega</div></div>
                    <div><div class="text-3xl font-bold text-amber-500 counter">4.9</div><div class="text-xs uppercase tracking-widest opacity-60">Rating</div></div>
                </div>
            </div>
            
            <div class="flex items-center justify-center order-1 lg:order-2 clip-reveal">
                <div class="w-full max-w-md aspect-square rounded-3xl overflow-hidden relative shadow-2xl tilt-card">
                    <!-- Placeholder Visual -->
                    <div class="absolute inset-0 bg-gradient-to-br from-blue-600/20 to-amber-500/20 flex items-center justify-center">
                        <span class="opacity-50">Visual Domótica</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- JS SYSTEMS -->
    <script>
        gsap.registerPlugin(ScrollTrigger);

        // 1. Cursor & Magnetic
        if(window.matchMedia('(pointer: fine)').matches) {{
            const dot = document.getElementById('cursor-dot');
            const ring = document.getElementById('cursor-ring');
            window.addEventListener('mousemove', e => {{
                gsap.to(dot, {{x: e.clientX, y: e.clientY, duration: 0.1}});
                gsap.to(ring, {{x: e.clientX, y: e.clientY, duration: 0.3}});
            }});
            
            document.querySelectorAll('.magnetic-btn').forEach(btn => {{
                btn.addEventListener('mousemove', e => {{
                    const rect = btn.getBoundingClientRect();
                    gsap.to(btn, {{x: (e.clientX - rect.left - rect.width/2)*0.3, y: (e.clientY - rect.top - rect.height/2)*0.3, duration: 0.2}});
                }});
                btn.addEventListener('mouseleave', () => gsap.to(btn, {{x: 0, y: 0, duration: 0.5, ease: 'elastic.out'}}));
            }});
            
            // Tilt 3D
            document.querySelectorAll('.tilt-card').forEach(card => {{
                card.addEventListener('mousemove', e => {{
                    const r = card.getBoundingClientRect();
                    const dx = (e.clientX - r.left - r.width/2) / (r.width/2);
                    const dy = (e.clientY - r.top - r.height/2) / (r.height/2);
                    gsap.to(card, {{rotateX: -dy*10, rotateY: dx*10, scale: 1.02, duration: 0.2, ease: "power2.out"}});
                }});
                card.addEventListener('mouseleave', () => gsap.to(card, {{rotateX: 0, rotateY: 0, scale: 1, duration: 0.5, ease: "power2.out"}}));
            }});
        }}
        
        // 2. Reveals
        gsap.to('.clip-reveal', {{
            clipPath: 'inset(0 0% 0 0)', duration: 1.5, ease: 'power4.inOut',
            scrollTrigger: {{ trigger: '.clip-reveal', start: 'top 80%' }}
        }});
        
        // 3. Counters
        document.querySelectorAll('.counter').forEach(el => {{
            const val = parseFloat(el.innerText);
            gsap.from(el, {{
                innerText: 0, duration: 2, ease: 'power2.out', snap: {{innerText: 1}},
                scrollTrigger: {{trigger: el, start: 'top 90%'}},
                onUpdate: function() {{ el.innerText = Math.round(this.targets()[0].innerText); }}
            }});
        }});
    </script>
</body>
</html>
"""

    variants = [
        {"name": "variante_A_moderno", "v_name": "Tech Moderno", "v_bg": "#F8FAFC", "v_text": "#0F172A", "v_opacity": "0.20"},
        {"name": "variante_B_dark", "v_name": "Dark Premium", "v_bg": "#0F172A", "v_text": "#F8FAFC", "v_opacity": "0.85"},
        {"name": "variante_C_calido", "v_name": "Cálido Accesible", "v_bg": "#FFFBEB", "v_text": "#1E293B", "v_opacity": "0.25"},
    ]
    
    for var in variants:
        html_content = template.format(**var)
        file_path = os.path.join(output_dir, var["name"] + ".html")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_content)
            
    print("Variantes generadas en clientes/novatech-confort/prototipos/")

if __name__ == "__main__":
    generate_prototypes()

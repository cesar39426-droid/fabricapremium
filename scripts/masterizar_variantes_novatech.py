import os

def generate_full_prototypes():
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
            backdrop-filter: blur(14px); border-radius: 16px; box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        }}
        
        /* Magnetic Button */
        .magnetic-btn {{
            display: inline-block; padding: 12px 24px; background: var(--primary);
            color: white; border-radius: 12px; font-weight: 600; text-decoration: none;
            transition: transform 0.2s;
        }}
        
        /* Shader Background Placeholder */
        #shader-bg {{
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            z-index: -1; opacity: var(--shader-opacity);
            background: radial-gradient(circle at 50% 50%, rgba(37,99,235,var(--shader-opacity)), transparent 60%);
            pointer-events: none;
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
    <div id="shader-bg"></div>

    <!-- HEADER NAV (Pill-Glass) -->
    <header class="fixed top-6 left-1/2 -translate-x-1/2 z-50 w-[92%] max-w-6xl header-nav">
        <div class="bg-gray-900/10 backdrop-blur-xl border border-gray-500/20 rounded-[60px] px-8 py-4 flex items-center justify-between shadow-2xl">
            <div class="text-xl font-bold heading text-blue-600">NovaTech</div>
            <nav class="hidden md:flex gap-8 items-center text-sm font-medium opacity-80">
                <a href="#inicio" class="hover:text-amber-500 transition-colors">Inicio</a>
                <a href="#servicios" class="hover:text-amber-500 transition-colors">Servicios</a>
                <a href="#contacto" class="magnetic-btn !py-2 !px-6 !rounded-full text-sm">Hablar Hoy</a>
            </nav>
        </div>
    </header>

    <!-- HERO SECTION -->
    <section id="inicio" class="relative min-h-screen flex items-center justify-center p-6 lg:p-24 overflow-hidden pt-32">
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
                    <a href="#servicios" class="magnetic-btn">Explorar Catálogo →</a>
                    <a href="#contacto" class="magnetic-btn" style="background: transparent; border: 1px solid #2563EB; color: #2563EB;">Hablanos por WhatsApp</a>
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
                    <div class="absolute inset-0 bg-gradient-to-br from-blue-600/30 to-amber-500/30 flex items-center justify-center border border-white/10 rounded-3xl">
                        <span class="opacity-50 font-medium">Visual Domótica / Ecosistema</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- SERVICIOS BENTO GRID -->
    <section id="servicios" class="py-32 px-6 lg:px-24 max-w-7xl mx-auto relative z-10">
        <div class="mb-16 text-center lg:text-left">
            <h2 class="text-4xl lg:text-5xl font-bold heading mb-4">Soluciones <span class="text-amber-500">Integrales</span></h2>
            <p class="text-lg opacity-70 max-w-2xl mx-auto lg:mx-0">Todo lo que necesitás para transformar tu hogar en un ecosistema inteligente.</p>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-3 md:grid-rows-2 gap-6 h-auto md:h-[600px] bento-wrapper">
            <!-- Box 1 Grandes (span 2 cols, 2 rows) -->
            <div class="tilt-card p-10 md:col-span-2 md:row-span-2 flex flex-col justify-end relative overflow-hidden bento-item">
                <div class="absolute top-0 right-0 w-64 h-64 bg-blue-500/10 rounded-full blur-3xl"></div>
                <div class="text-6xl mb-6">🖥️</div>
                <h3 class="text-3xl font-bold heading mb-4">Domótica Integrada</h3>
                <p class="opacity-70 max-w-md text-lg">Control unificado de clima, iluminación, persianas y seguridad desde una sola app. Compatible con Alexa, Google Home y Siri.</p>
                <div class="absolute top-6 right-6 px-4 py-1.5 bg-amber-500 text-black text-xs font-bold rounded-full uppercase tracking-wider">Más Solicitado</div>
            </div>
            <!-- Box 2 -->
            <div class="tilt-card p-8 flex flex-col justify-end relative overflow-hidden bento-item">
                <div class="text-4xl mb-4 relative z-10">🌡️</div>
                <h3 class="text-xl font-bold heading mb-3 relative z-10">Clima Inteligente</h3>
                <p class="text-sm opacity-70 relative z-10">Termostatos con aprendizaje adaptativo que reducen el consumo hasta un 35%.</p>
            </div>
            <!-- Box 3 -->
            <div class="tilt-card p-8 flex flex-col justify-end relative overflow-hidden bento-item">
                <div class="text-4xl mb-4 relative z-10">💡</div>
                <h3 class="text-xl font-bold heading mb-3 relative z-10">Iluminación Premium</h3>
                <p class="text-sm opacity-70 relative z-10">Sistemas LED con escenas programables y control por movimiento.</p>
            </div>
        </div>
    </section>

    <!-- CALL TO ACTION -->
    <section id="contacto" class="py-32 relative overflow-hidden">
        <div class="absolute inset-0 bg-blue-600/10 mix-blend-overlay"></div>
        <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full max-w-4xl h-96 bg-blue-500/20 blur-[120px] rounded-full pointer-events-none"></div>
        <div class="max-w-4xl mx-auto px-6 text-center relative z-10">
            <h2 class="text-4xl lg:text-6xl font-bold heading mb-6">¿Listo para <span class="text-blue-600">transformar</span> tu hogar?</h2>
            <p class="text-xl opacity-80 mb-10 max-w-2xl mx-auto">Diagnóstico inicial sin cargo. Hablemos sobre tu proyecto y descubrí el potencial de tu espacio residencial.</p>
            <div class="flex flex-col sm:flex-row justify-center gap-6">
                <a href="#" class="magnetic-btn !px-10 !py-5 text-lg shadow-xl shadow-blue-600/20">Quiero mi diagnóstico gratuito →</a>
                <a href="#" class="magnetic-btn !px-10 !py-5 text-lg" style="background: transparent; border: 1px solid rgba(255,255,255,0.2);">contacto@novatechconfort.demo</a>
            </div>
        </div>
    </section>

    <!-- FOOTER -->
    <footer class="py-12 border-t border-gray-500/20 px-6 lg:px-24 relative z-10">
        <div class="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center gap-6">
            <div class="text-2xl font-bold heading text-blue-600 opacity-80">NovaTech</div>
            <div class="flex gap-8 font-medium text-sm">
                <a href="#" class="opacity-60 hover:opacity-100 hover:text-amber-500 transition-colors">Servicios</a>
                <a href="#" class="opacity-60 hover:opacity-100 hover:text-amber-500 transition-colors">Proceso</a>
                <a href="#" class="opacity-60 hover:opacity-100 hover:text-amber-500 transition-colors">Precios</a>
            </div>
            <div class="flex gap-6 opacity-60 text-sm">
                <a href="#" class="hover:text-amber-500 transition-colors">Inst</a>
                <a href="#" class="hover:text-amber-500 transition-colors">Lkin</a>
                <a href="#" class="hover:text-amber-500 transition-colors">WApp</a>
            </div>
            <div class="opacity-40 text-xs">© 2026 NovaTech Confort. Todos los derechos reservados.</div>
        </div>
    </footer>

    <!-- GSAP / UI SCRIPTS -->
    <script>
        gsap.registerPlugin(ScrollTrigger);

        if(window.matchMedia('(pointer: fine)').matches) {{
            // 1. Ocultar cursor nativo y vincular custom cursor
            const dot = document.getElementById('cursor-dot');
            const ring = document.getElementById('cursor-ring');
            window.addEventListener('mousemove', e => {{
                gsap.to(dot, {{x: e.clientX, y: e.clientY, duration: 0.1}});
                gsap.to(ring, {{x: e.clientX, y: e.clientY, duration: 0.3}});
            }});
            
            // 2. Botones Magnéticos
            document.querySelectorAll('.magnetic-btn').forEach(btn => {{
                btn.addEventListener('mousemove', e => {{
                    const rect = btn.getBoundingClientRect();
                    gsap.to(btn, {{x: (e.clientX - rect.left - rect.width/2)*0.3, y: (e.clientY - rect.top - rect.height/2)*0.3, duration: 0.2}});
                }});
                btn.addEventListener('mouseleave', () => gsap.to(btn, {{x: 0, y: 0, duration: 0.5, ease: 'elastic.out'}}));
            }});
            
            // 3. Tarjetas 3D Tilt (Hero + Bento Grid)
            document.querySelectorAll('.tilt-card').forEach(card => {{
                card.addEventListener('mousemove', e => {{
                    const r = card.getBoundingClientRect();
                    const dx = (e.clientX - r.left - r.width/2) / (r.width/2);
                    const dy = (e.clientY - r.top - r.height/2) / (r.height/2);
                    gsap.to(card, {{rotateX: -dy*8, rotateY: dx*8, scale: 1.015, duration: 0.2, ease: "power2.out"}});
                }});
                card.addEventListener('mouseleave', () => gsap.to(card, {{rotateX: 0, rotateY: 0, scale: 1, duration: 0.5, ease: "power2.out"}}));
            }});
        }}
        
        // 4. Clip Reveal Imágenes
        gsap.to('.clip-reveal', {{
            clipPath: 'inset(0 0% 0 0)', duration: 1.5, ease: 'power4.inOut',
            scrollTrigger: {{ trigger: '.clip-reveal', start: 'top 80%' }}
        }});
        
        // 5. Contadores Matemáticos
        document.querySelectorAll('.counter').forEach(el => {{
            const val = parseFloat(el.innerText);
            gsap.from(el, {{
                innerText: 0, duration: 2, ease: 'power2.out', snap: {{innerText: 1}},
                scrollTrigger: {{trigger: el, start: 'top 90%'}},
                onUpdate: function() {{ el.innerText = Math.round(this.targets()[0].innerText); }}
            }});
        }});

        // 6. Header Dinámico (Aparece/Desaparece al Scrollear)
        let lastScrollY = window.scrollY;
        const header = document.querySelector('.header-nav');
        window.addEventListener('scroll', () => {{
            const currentScrollY = window.scrollY;
            if (currentScrollY > 100 && currentScrollY > lastScrollY) {{
                gsap.to(header, {{y: -150, duration: 0.4, ease: 'power2.in'}}); // Oculta
            }} else if (currentScrollY < lastScrollY) {{
                gsap.to(header, {{y: 0, duration: 0.4, ease: 'power2.out'}});   // Muestra
            }}
            lastScrollY = currentScrollY;
        }});

        // 7. Reveal Asimétrico de Bento Grid
        ScrollTrigger.batch(".bento-item", {{
            onEnter: batch => gsap.fromTo(batch, 
                {{opacity: 0, y: 60}}, 
                {{opacity: 1, y: 0, stagger: 0.15, duration: 0.8, ease: "back.out(1.2)", overwrite: true}}
            ),
            start: "top 85%"
        }});
    </script>
</body>
</html>
"""

    # Manteniendo la paleta única de cada Variante
    variants = [
        {"name": "variante_A_moderno", "v_name": "Tech Moderno", "v_bg": "#F8FAFC", "v_text": "#0F172A", "v_opacity": "0.15"},
        {"name": "variante_B_dark", "v_name": "Dark Premium", "v_bg": "#0F172A", "v_text": "#F8FAFC", "v_opacity": "0.85"},
        {"name": "variante_C_calido", "v_name": "Cálido Accesible", "v_bg": "#FFFBEB", "v_text": "#1E293B", "v_opacity": "0.20"},
    ]
    
    for var in variants:
        html_content = template.format(**var)
        file_path = os.path.join(output_dir, var["name"] + ".html")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_content)
            
    print("Las 3 Variantes HTML completas han sido masterizadas y grabadas localmente.")

if __name__ == "__main__":
    generate_full_prototypes()

import os
import sys
import shutil
import subprocess

def create_new_site(project_name):
    # Definir rutas base relativas al entorno
    script_dir = os.path.dirname(os.path.abspath(__file__))
    fabrica_root = os.path.dirname(script_dir)  # 'fabrica-premium'
    clients_dir = os.path.dirname(fabrica_root) # 'creador de sitios'
    
    target_dir = os.path.join(clients_dir, project_name)
    
    print(f"\n[1/4] Iniciando Protocolo Fábrica Premium para proyecto: {project_name}")
    print("---------------------------------------------------------")
    print(f"Directorio Origen: {fabrica_root}")
    print(f"Directorio Origen: {target_dir}")
    
    # 1. Validación e inyección
    if os.path.exists(target_dir):
        print(f"✖ Error: El proyecto '{project_name}' ya existe en {target_dir}.")
        print("Operación abortada para no sobreescribir datos del cliente.")
        sys.exit(1)
        
    print(f"[2/4] Transfiriendo Arquitectura de Inmersión y Componentes V2...")
    # 2. Ignorar peso muerto (carpetas Node, Git y Entornos Virutales/Temporales)
    def ignore_patterns(dir_path, contents):
        return [
            'node_modules', 
            '.git', 
            '.temp', 
            '.tmp', 
            '.env',
            'directivas', 
            'scripts'
        ]

    try:
        shutil.copytree(fabrica_root, target_dir, ignore=ignore_patterns)
        print("✔ Clonación estructural completada.")
    except Exception as e:
        print(f"✖ Error copiando framework de fábrica: {e}")
        sys.exit(1)
        
    print(f"[3/4] Inicializando Repositorio Limpio Git...")
    try:
        subprocess.run(["git", "init"], cwd=target_dir, check=True, stdout=subprocess.DEVNULL)
        print("✔ Git init ejecutado con éxito.")
    except Exception as e:
        print(f"⚠ Warning: Git no encontrado o fallo al inicializar repo local: {e}")
        
    print(f"[4/4] Instalando dependencias WebGL/UI nativas (npm install)...")
    print("      (Este paso puede demorar 1-2 minutos dependiendo de tu SSD/Red)")
    try:
        # Uso shell=True crucial en Windows para comandos binarios generados (.cmd)
        subprocess.run("npm install", shell=True, cwd=target_dir, check=True)
        print("✔ Hidratación NPM completada.")
    except Exception as e:
        print(f"✖ Error al intentar descargar Node Modules en el nuevo site: {e}")
        sys.exit(1)
        
    print("\n========================================================")
    print(f"✅ ¡FÁBRICA CREADA EXITOSAMENTE: {project_name}!")
    print(f"📍 Ruta: {target_dir}")
    print("✅ Todos los componentes inmersivos GSAP/Three.js ya están preinstalados.")
    print("🚀 Siguiente paso recomendado:")
    print(f"   cd '../{project_name}' && npm run dev")
    print("========================================================\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python crear_nuevo_sitio.py <nombre-del-cliente>")
        print("Ej:  python crear_nuevo_sitio.py acme-corporation")
        sys.exit(1)
        
    client_name = sys.argv[1]
    create_new_site(client_name)

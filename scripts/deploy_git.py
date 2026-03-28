import os
import subprocess
import argparse

def run_command(command, cwd=None):
    """Ejecuta un comando en shell y retorna su salida o lanza excepción en caso de error."""
    print(f"[*] Ejecutando: {command}")
    result = subprocess.run(command, shell=True, cwd=cwd, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"[!] Error ejecutando {command}:\n{result.stderr}")
        return False, result.stderr
    print(result.stdout)
    return True, result.stdout

def deploy_via_git(file_path, commit_message, repo_url=None):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # 1. Verificar si estamos en un repositorio Git
    success, output = run_command("git status", cwd=base_dir)
    if not success:
        print("[*] Repositorio no inicializado. Inicializando Git...")
        success, _ = run_command("git init", cwd=base_dir)
        if not success:
            return False
            
    # 2. Configurar remote si se proporciona
    if repo_url:
        print(f"[*] Configurando remoto 'origin' a {repo_url}...")
        # Intentamos obtener remotos
        success, remotes = run_command("git remote -v", cwd=base_dir)
        if "origin" in remotes:
            success, _ = run_command(f"git remote set-url origin {repo_url}", cwd=base_dir)
        else:
            success, _ = run_command(f"git remote add origin {repo_url}", cwd=base_dir)

    # 3. Preguntar por la rama actual (por defecto main/master)
    print(f"[*] Preparando archivo {file_path} para git add...")
    success, _ = run_command(f"git add \"{file_path}\"", cwd=base_dir)
    if not success:
        return False
        
    print(f"[*] Haciendo commit de los cambios...")
    success, _ = run_command(f"git commit -m \"{commit_message}\"", cwd=base_dir)
    if not success:
        # Podría ser que no haya cambios para commitear
        print("[!] Verifica si el archivo tenía modificaciones.")

    # 4. Push al repositorio remoto
    success, _ = run_command("git branch --show-current", cwd=base_dir)
    branch = output.strip() if success and output.strip() else "main"
    if not branch: branch = "main"

    print(f"[*] Haciendo push a origin/{branch}...")
    success, push_out = run_command(f"git push -u origin {branch}", cwd=base_dir)
    
    if success:
        print("✅ Push exitoso.")
        print("➡️ IMPORTANTE: Ve a tu panel de Hostinger (Avanzado > Git), enlaza el repositorio y pulsa 'Deploy'.")
    else:
        print("❌ Error en el Push. Por favor, asegúrate de que el repositorio remoto exista, que tengas credenciales locales configuradas en Git y que la URL sea correcta.")
        
    return success

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Despliega archivos por Git a un repositorio para Hostinger")
    parser.add_argument("file", help="Ruta o nombre del archivo a añadir (ej: dist/demo-fabrica.html)")
    parser.add_argument("--msg", default="Deploy para Hostinger", help="Mensaje del commit")
    parser.add_argument("--remote", default=None, help="URL del repositorio remoto (ej. https://github.com/usuario/repo.git)")
    args = parser.parse_args()
    
    deploy_via_git(args.file, args.msg, args.remote)

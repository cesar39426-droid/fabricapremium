import os
import ftplib
import argparse
from dotenv import load_dotenv

def upload_to_hostinger(file_path, dest_filename="index.html"):
    # Load .env explicitly if needed
    load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env'))
    
    host = os.environ.get("FTP_HOST")
    user = os.environ.get("FTP_USER")
    password = os.environ.get("FTP_PASSWORD")
    dest_path = os.environ.get("FTP_DEST_PATH", "public_html")
    
    if not all([host, user, password]):
        print("Error: Credenciales FTP no definidas.")
        print("Por favor configura FTP_HOST, FTP_USER, FTP_PASSWORD en el archivo .env")
        return False
        
    if not os.path.exists(file_path):
        print(f"Error: El archivo fuente no existe: {file_path}")
        return False
    
    try:
        print(f"Iniciando despliegue de '{file_path}' hacia '{host}' en '{dest_path}/{dest_filename}'...")
        ftp = ftplib.FTP(host)
        ftp.login(user=user, passwd=password)
        print("Conexión FTP éxitosa.")
        
        try:
            ftp.cwd(dest_path)
        except Exception as e:
            print(f"Error al acceder a la ruta destino {dest_path}: {e}")
            ftp.quit()
            return False
            
        with open(file_path, "rb") as file_to_upload:
            ftp.storbinary(f'STOR {dest_filename}', file_to_upload)
            
        print("¡Archivo subido exitosamente a Hostinger!")
        ftp.quit()
        return True
    except Exception as e:
        print(f"Fallo durante la operación FTP: {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Despliega un HTML a Hostinger")
    parser.add_argument("file", help="Ruta al archivo HTML a subir")
    parser.add_argument("--name", default="index.html", help="Nombre del archivo de destino")
    args = parser.parse_args()
    
    upload_to_hostinger(args.file, args.name)

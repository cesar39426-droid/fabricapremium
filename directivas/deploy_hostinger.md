# deploy_hostinger.md

## 🎯 Objetivo
Desplegar automáticamente un archivo HTML (ej. prototipos para clientes como Novatech) a un servidor en Hostinger mediante FTP.

## ⚙️ Procedimiento (SOP)
1. **Validar Archivo**: Confirmar que el archivo fuente existe.
2. **Cargar Credenciales**: Obtener credenciales FTP (HOST, USUARIO, CONTRASEÑA, RUTA_DESTINO) desde el archivo `.env`.
3. **Conexión FTP**: Conectar al servidor Hostinger usando FTP/ftplib en Python.
4. **Carga (Upload)**: Subir el archivo y renombrarlo como `index.html` (o el nombre adecuado según la ruta) en el servidor destino.
5. **Cierre**: Cerrar la conexión y confirmar el éxito.

## 🚨 Restricciones y Casos Borde
- Las credenciales FTP NUNCA deben estar harcodeadas en el script. Siempre usar `os.environ` o `dotenv`.
- Si las credenciales faltan en `.env`, el script debe imprimir un mensaje de error claro y salir sin lanzar una excepción cruda que confunda al usuario.
- En Hostinger, generalmente la ruta de despliegue es dentro de `public_html/`.

---
**Status**: [ACTIVE]
**Orquestador**: Agente de Despliegue

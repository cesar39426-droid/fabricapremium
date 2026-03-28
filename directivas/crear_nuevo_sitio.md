# Directiva: Creación de Nuevos Sitios (Clonación de Fábrica)

## 🎯 Objetivo General
Estandarizar y automatizar la generación de nuevos sitios web para clientes utilizando la estructura de alto rendimiento "Fábrica Premium" (Stack: Astro, React, Tailwind, GSAP, WebGL/Three.js) asegurando que todos los componentes UI interactivos de élite y las dependencias ya estén integradas desde el minuto cero.

## ⚙️ Bucle Central de Generación
Esta directiva se materializa en el script idempotente `scripts/crear_nuevo_sitio.py`.

El CLI automatizado hará lo siguiente:
1. Recibir el nombre del nuevo proyecto (ej. `acme-corp`).
2. Clonar la carpeta actual `fabrica-premium` hacia un nuevo directorio hermano dentro de `creador de sitios/`.
3. Ignorar estrictamente las carpetas temporales pesadas y privadas (`node_modules`, `.git`, `.tmp`, `.env`).
4. Inicializar un repositorio limpio de Git (`git init`) en el proyecto destino para independizarlo.
5. Ejecutar la instalación de los paquetes exactos (`npm install`) para hidratar las dependencias WebGL/UI necesarias.
6. Reemplazar referencias base del nombre en un archivo de configuración si es requerido.

## 🚨 Restricciones y Casos Borde (Trampas Conocidas)
- **Node Modules Blackhole:** El script NUNCA debe intentar copiar la carpeta `node_modules` de la fábrica. Copiar cientos de miles de archivos detendrá el disco y fallará la orquestación. Usa `shutil.copytree(ignore=shutil.ignore_patterns(...))` en Python.
- **Limpieza de Identidad:** La fábrica tiene el nombre base global `NubeN` quemado en sus componentes genéricos. Esta clonación asume el estado neutral de la fábrica, listo para que los Agentes inyecten el *Spec* de contenido del cliente final una vez se ha generado el nuevo entorno.
- **Entorno de Ejecución Local:** El script se ejecuta vía Powershell (Windows) por lo que debe utilizar formato de rutas universales de `os.path` y subprocesos adaptados a comandos agnósticos o de entorno (`npm.cmd` en Windows).

---
**Status:** [ACTIVE]
**Orquestador:** Antigravity (Python Automation)

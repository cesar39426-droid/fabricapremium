# despliegue_git_hostinger.md

## 🎯 Objetivo
Habilitar y documentar el flujo de publicación continua (CI/CD básico) vía Git hacia un repositorio remoto (ej. GitHub), para que Hostinger pueda tomar el código de allí y actualizar automáticamente el dominio (ej. gestionemocional.shop).

## ⚙️ Procedimiento (SOP)
1. **Inicialización**: Verificar si el repositorio Git local existe (`git status`). Si no, inicializarlo con `git init`.
2. **Ignorar Archivos Base**: Asegurar que existe un archivo `.gitignore` configurado para ignorar directorios como `node_modules/`, `.env`, y `.tmp/` garantizando que no se suban secretos ni archivos pesados.
3. **Staging y Commit**: Añadir los archivos deseados al área de staging (`git add <archivo/s>`) y realizar el commit con un mensaje descriptivo (`git commit -m "..."`).
4. **Vinculación Remota**: Agregar o actualizar el `remote origin` que apunta al repositorio en GitHub u otro proveedor (`git remote add origin <URL>` o `git remote set-url origin <URL>`).
5. **Push al Repositorio Remoto**: Enviar el código a la rama principal (usualmente `main` o `master`) usando `git push -u origin <rama>`.
6. **Despliegue Hostinger (Manual por el Usuario)**: El usuario accede a la sección "Avanzado > Git" de Hostinger, añade la URL del repositorio protegido (o público) y activa el Despliegue Automático (Webhook).

## 🚨 Restricciones y Casos Borde
- NUNCA subas el archivo `.env` o tokens harcodeados.
- Si el remoto ya existe pero el push es rechazado (`rejected`), el script/usuario debe realizar `git pull` antes de volver a intentar, o forzar si la rama local es la fuente de verdad y se asume el riesgo consciente.
- La rama a sincronizar en Hostinger debe coincidir exactamente con la rama push-eada (típicamente `main`).

---
**Status**: [ACTIVE]
**Orquestador**: Agente Arquitecto y Agente de Despliegue

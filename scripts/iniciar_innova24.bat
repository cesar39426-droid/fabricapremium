@echo off
setlocal EnableDelayedExpansion
title Innova24 Proposal Engine - Iniciando...
color 0B

echo ========================================================
echo   Innova24 Proposal Engine - Instalador Automatico
echo ========================================================
echo.

:: -------------------------------------------------------
:: 1. Verificar Node.js y version minima requerida
:: -------------------------------------------------------
echo [1/3] Verificando Node.js...
node -v >nul 2>&1
if %errorlevel% neq 0 (
    color 0C
    echo.
    echo [ERROR] No se detecto Node.js instalado.
    echo Por favor, descarga e instala Node.js desde: https://nodejs.org/
    echo.
    pause
    exit /b 1
)

:: Capturar version y verificar minimo (v18+)
for /f "tokens=1 delims=v" %%i in ('node -v') do set NODE_FULL=%%i
for /f "tokens=1 delims=." %%i in ("!NODE_FULL!") do set NODE_MAJOR=%%i

if !NODE_MAJOR! LSS 18 (
    color 0E
    echo.
    echo [ADVERTENCIA] Se detecto Node.js v!NODE_FULL!, pero se recomienda v18 o superior.
    echo La aplicacion puede no funcionar correctamente.
    echo.
    choice /C SN /M "Desea continuar de todas formas?"
    if !errorlevel! == 2 exit /b 1
)

echo Node.js v!NODE_FULL! detectado correctamente.
echo.

:: -------------------------------------------------------
:: 2. Verificar npm disponible
:: -------------------------------------------------------
npm -v >nul 2>&1
if %errorlevel% neq 0 (
    color 0C
    echo [ERROR] npm no esta disponible. Reinstala Node.js desde: https://nodejs.org/
    echo.
    pause
    exit /b 1
)

:: -------------------------------------------------------
:: 3. Verificar package.json antes de instalar
:: -------------------------------------------------------
if not exist "package.json" (
    color 0C
    echo [ERROR] No se encontro package.json en el directorio actual.
    echo Asegurate de ejecutar este script desde la carpeta raiz del proyecto.
    echo.
    echo Directorio actual: %CD%
    echo.
    pause
    exit /b 1
)

:: -------------------------------------------------------
:: 4. Instalar o verificar dependencias
:: -------------------------------------------------------
if exist "node_modules" (
    echo [2/3] Verificando integridad de dependencias...
    call npm install --prefer-offline >nul 2>&1
    if !errorlevel! neq 0 (
        color 0E
        echo [ADVERTENCIA] No se pudo verificar dependencias en modo offline.
        echo Intentando verificacion online...
        call npm install
        if !errorlevel! neq 0 (
            color 0C
            echo [ERROR] Fallo la instalacion de dependencias.
            pause
            exit /b 1
        )
    ) else (
        echo Dependencias verificadas correctamente.
    )
) else (
    echo [2/3] Instalando dependencias (esto puede tardar unos minutos)...
    call npm install
    if !errorlevel! neq 0 (
        color 0C
        echo.
        echo [ERROR] Hubo un problema al instalar las dependencias.
        echo Sugerencias:
        echo   - Verificar conexion a internet
        echo   - Ejecutar como Administrador
        echo   - Revisar que el antivirus no bloquee npm
        echo.
        pause
        exit /b 1
    )
    echo Dependencias instaladas correctamente.
)
echo.

:: -------------------------------------------------------
:: 5. Verificar archivo de entrada principal
:: -------------------------------------------------------
echo [3/3] Verificando archivos del proyecto...

:: Leer el campo "main" de package.json o asumir index.js
set ENTRY_FILE=index.js
for /f "tokens=2 delims=:, " %%i in ('findstr /i "\"main\"" package.json') do (
    set RAW=%%i
    set ENTRY_FILE=!RAW:"=!
)

:: Limpiar espacios en blanco posibles
set ENTRY_FILE=%ENTRY_FILE: =%

if not exist "!ENTRY_FILE!" (
    color 0C
    echo [ERROR] No se encontro el archivo de entrada definido: !ENTRY_FILE!
    echo.
    echo Buscando alternativas comunes...
    if exist "server.js" (
        set ENTRY_FILE=server.js
        echo Archivo alternativo encontrado: server.js
    ) else if exist "app.js" (
        set ENTRY_FILE=app.js
        echo Archivo alternativo encontrado: app.js
    ) else (
        echo Verificá que el proyecto este completo.
        echo.
        pause
        exit /b 1
    )
)

echo Archivo principal detectado: !ENTRY_FILE!
echo.

:: -------------------------------------------------------
:: 6. Arranque de la aplicacion
:: -------------------------------------------------------
color 0A
echo ========================================================
echo   Todo listo. Iniciando Innova24 Proposal Engine...
echo ========================================================
echo.
echo Presiona Ctrl+C para detener el servidor en cualquier momento.
echo.

:: Usar npm start si existe el script, sino node directo
findstr /i "\"start\"" package.json >nul 2>&1
if %errorlevel% == 0 (
    call npm start
) else (
    node !ENTRY_FILE!
)

if %errorlevel% neq 0 (
    color 0C
    echo.
    echo [ERROR] La aplicacion se cerro con un error (codigo: %errorlevel%).
    echo Revisa los logs anteriores para mas detalles.
    echo.
)

echo.
pause
endlocal

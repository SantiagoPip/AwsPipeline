# 📄 desplegar.ps1

# 1. Definir nombres de archivos
$ZIP_NAME = "deploy_package.zip"

echo "🧹 Limpiando archivos basura anteriores..."
if (Test-Path $ZIP_NAME) { Remove-Item $ZIP_NAME }

echo "📦 1. Copiando tu código al paquete..."
# Comprimimos tu main.py y la carpeta src
Compress-Archive -Path "main.py", "src" -DestinationPath $ZIP_NAME

echo "📚 2. Agregando Pandas y librerías del entorno virtual (.venv)..."
# Vamos a la carpeta donde pip instala las librerías en Windows y las metemos al ZIP
$VENV_LIBS = ".venv\Lib\site-packages\*"
Compress-Archive -Path $VENV_LIBS -Update -DestinationPath $ZIP_NAME

echo "🚀 3. ¡Paquete ZIP creado con éxito como '$ZIP_NAME'!"
echo "Este único archivo contiene tu código y todas sus dependencias listo para AWS Lambda."

@echo off
echo ===============================
echo Configurando el proyecto Python...

cd "python-3.12.5-embed-amd64"

echo Instalando paquétes necesarios

.\python -m pip install -r ..\requirements.txt

pause
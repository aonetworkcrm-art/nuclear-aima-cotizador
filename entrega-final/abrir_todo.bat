@echo off
title Nuclear AIMA · Paquete de Entrega · Ramón Orlando
color 0A

echo ======================================================
echo        NUCLEAR AIMA · PAQUETE DE ENTREGA
echo   Operacion "50 Años de Infinito para Ramon Orlando"
echo ======================================================
echo.

echo [1/4] Abriendo Propuesta Completa (PDF)...
start "" "%~dp01-propuesta-completa\propuesta-completa.pdf"

echo [2/4] Abriendo Presentacion Interactiva (HTML)...
start "" "%~dp02-presentacion\presentacion-deck.html"

echo [3/4] Abriendo Resumen Ejecutivo (PDF)...
start "" "%~dp03-resumen-ejecutivo\resumen-ejecutivo.pdf"

echo [4/4] Abriendo carpeta de Anexos Web...
start "" "%~dp04-anexos-web"

echo.
echo ======================================================
echo   Todos los documentos se estan abriendo.
echo   Presiona cualquier tecla para cerrar esta ventana.
echo ======================================================
pause >nul
exit

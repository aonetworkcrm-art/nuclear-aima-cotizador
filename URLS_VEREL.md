# URLs de Vercel — Proyecto Nuclear AIMA Route

## Producción (hoja de captura / propuesta)

- **Página principal:** https://nuclear-aima-route.vercel.app
- **Hoja de captura de ruta (SMAC):** https://nuclear-aima-route.vercel.app/hoja-captura-ruta.html
- **Herramienta de extracción de datos:** https://nuclear-aima-route.vercel.app/extraer-datos.html

## Notas

- El `vercel.json` redirige `/(.*)` a `/hoja-captura-ruta.html`, por lo que la raíz
  muestra la hoja de captura interactiva.
- Todos los archivos se sirven desde el repositorio; el archivo `extraer-datos.html`
  permite generar un archivo `.txt` y un archivo `.csv` (logeado en el navegador).
- Si Vercel crea una URL con un hash aleatorio en un nuevo despliegue, ese ID
  reemplaza temporalmente el dominio producción; usarlo hasta que se canonicalice
  el alias.

# sec-automation-utils

![CI](https://github.com/aka-met4ll0f/sec-automation-utils/actions/workflows/ci.yml/badge.svg)

## Descripción
Scripts de automatización de datos y generación de evidencias visuales.

## Autor
- Autor: **met4ll0f**
- GitHub: `https://github.com/aka-met4ll0f`

## Scripts incluidos
- `gen_users.py`: genera usuarios desde columna de nombres en CSV/XLSX.
- `web_screenshot_report.sh`: toma capturas de pantalla y genera índice HTML navegable.

## Requisitos
- Python 3.10+
- Dependencias: `pip install -r requirements.txt`
- Para screenshots: binario/comando `webscreenshot` disponible en PATH.

## Uso
1. Instala dependencias:
   - `pip install -r requirements.txt`
2. Genera usuarios desde Excel/CSV:
   - `python3 gen_users.py empleados.xlsx -c "Nombre" -o users.txt --ascii --lower --dedupe`
3. Genera el reporte de capturas web:
   - `chmod +x web_screenshot_report.sh`
   - `./web_screenshot_report.sh hosts.txt salida_screens`
4. Revisa archivos generados (`users.txt`, `skipped.txt`, `index.html`).

## Aviso legal
Usar solo con permisos del propietario de datos/sitios o en laboratorio/CTF. El creador no se hace responsable por el mal uso.

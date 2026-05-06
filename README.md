# data-automation-utils

![CI](https://github.com/aka-met4ll0f/data-automation-utils/actions/workflows/ci.yml/badge.svg)

Scripts de automatización de datos y generación de evidencias visuales.

- Autor: **met4ll0f**
- GitHub: `https://github.com/aka-met4ll0f`

## Scripts
- `gen_users.py`: genera usuarios desde columna de nombres en CSV/XLSX.
- `web_screenshot_report.sh`: toma screenshots y genera indice HTML navegable.

## Requisitos
- Python 3.10+
- Dependencias: `pip install -r requirements.txt`
- Para screenshots: binario/comando `webscreenshot` disponible en PATH.

## Uso paso a paso
1. Instala dependencias:
   - `pip install -r requirements.txt`
2. Generar usuarios desde Excel/CSV:
   - `python3 gen_users.py empleados.xlsx -c "Nombre" -o users.txt --ascii --lower --dedupe`
3. Generar reporte de capturas web:
   - `chmod +x web_screenshot_report.sh`
   - `./web_screenshot_report.sh hosts.txt salida_screens`
4. Revisa archivos generados (`users.txt`, `skipped.txt`, `index.html`).

## Disclaimer
Usar solo con permisos del propietario de datos/sitios o en laboratorio/CTF. El creador no se hace responsable por el mal uso.

# username-generator

![CI](https://github.com/aka-met4ll0f/username-generator/actions/workflows/ci.yml/badge.svg)
![Tipo](https://img.shields.io/badge/Tipo-Automation-orange)

## Descripción
Herramienta para generar usuarios desde archivos CSV/XLSX de forma consistente.

## Scripts incluidos
- `gen_users.py`: genera usuarios desde columna de nombres en CSV/XLSX.

## Resumen rápido
| Script | Entrada | Salida | Uso típico |
|---|---|---|---|
| `gen_users.py` | CSV/XLSX con columna de nombres | `users.txt` + `skipped.txt` | Normalización y generación de usuarios |

## Requisitos
- Python 3.10+
- Dependencias: `pip install -r requirements.txt`

## Uso
1. Instala dependencias:
   - `pip install -r requirements.txt`
2. Genera usuarios desde Excel/CSV:
   - `python3 gen_users.py empleados.xlsx -c "Nombre" -o users.txt --ascii --lower --dedupe`
3. Revisa archivos generados (`users.txt`, `skipped.txt`).

## Autor
- Autor: **met4ll0f**
- GitHub: `https://github.com/aka-met4ll0f`

## Aviso legal
Usar solo con permisos del propietario de datos/sitios o en laboratorio/CTF. El creador no se hace responsable por el mal uso.

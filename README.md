# username-generator

![CI](https://github.com/aka-met4ll0f/username-generator/actions/workflows/ci.yml/badge.svg)
![Type](https://img.shields.io/badge/Type-Automation-orange)

## Description
Tool to generate usernames from CSV/XLSX files in a consistent format.

## Included scripts
- `gen_users.py`: generates usernames from a name column in CSV/XLSX files.

## Quick summary
| Script | Input | Output | Typical use |
|---|---|---|---|
| `gen_users.py` | CSV/XLSX with name column | `users.txt` + `skipped.txt` | Username normalization and generation |

## Requirements
- Python 3.10+
- Dependencies: `pip install -r requirements.txt`

## Usage
1. Install dependencies:
   - `pip install -r requirements.txt`
2. Generate usernames from Excel/CSV:
   - `python3 gen_users.py employees.xlsx -c "Name" -o users.txt --ascii --lower --dedupe`
3. Review generated files (`users.txt`, `skipped.txt`).

## Author
- Author: **met4ll0f**
- GitHub: `https://github.com/aka-met4ll0f`

## Legal Notice
Use only with data/target owner permission or in a controlled lab/CTF. The creator is not responsible for misuse.

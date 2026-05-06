#!/usr/bin/env python3
import argparse
import re
import sys
import unicodedata
from pathlib import Path

import pandas as pd


BANNER = r"""
  ____ _____ _   _   _   _ ____  _____ ____  ____
 / ___| ____| \ | | | | | / ___|| ____|  _ \/ ___|
| |  _|  _| |  \| | | | | \___ \|  _| | |_) \___ \
| |_| | |___| |\  | | |_| |___) | |___|  _ < ___) |
 \____|_____|_| \_|  \___/|____/|_____|_| \_\____/
"""


def strip_accents(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))


def clean_name(raw: str, ascii_only: bool, to_lower: bool) -> str:
    if raw is None:
        return ""
    s = str(raw).strip()
    if not s or s.lower() == "nan":
        return ""
    s = re.sub(r"[^\w\s'\-áéíóúÁÉÍÓÚñÑ]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    if ascii_only:
        s = strip_accents(s)
    if to_lower:
        s = s.lower()
    return s


def username_from_name(full_name: str):
    parts = full_name.split()
    if len(parts) == 2:
        return f"{parts[0]}.{parts[1]}"
    if len(parts) == 3:
        return f"{parts[0]}.{parts[1]}"
    if len(parts) == 4:
        return f"{parts[0]}.{parts[2]}"
    return None


def read_table(input_path: Path) -> pd.DataFrame:
    ext = input_path.suffix.lower()
    if ext in [".xlsx", ".xls"]:
        return pd.read_excel(input_path, engine="openpyxl" if ext == ".xlsx" else None)
    if ext == ".csv":
        try:
            return pd.read_csv(input_path, encoding="utf-8")
        except UnicodeDecodeError:
            return pd.read_csv(input_path, encoding="latin-1")
    raise ValueError("Formato no soportado")


def main():
    print(BANNER)
    print("[DISCLAIMER] Uso autorizado de datos.")
    print("Autor: met4ll0f | https://github.com/aka-met4ll0f")
    ap = argparse.ArgumentParser(description="Genera usuarios nombre.apellido")
    ap.add_argument("input")
    ap.add_argument("-c", "--column", default="Nombre")
    ap.add_argument("-o", "--output", default="users.txt")
    ap.add_argument("--skipped", default="skipped.txt")
    ap.add_argument("--ascii", action="store_true")
    ap.add_argument("--lower", action="store_true")
    ap.add_argument("--dedupe", action="store_true")
    args = ap.parse_args()

    df = read_table(Path(args.input))
    if args.column not in df.columns:
        print(f"No existe columna: {args.column}", file=sys.stderr)
        sys.exit(1)

    users = []
    skipped = []
    for idx, raw in enumerate(df[args.column].tolist(), start=1):
        cleaned = clean_name(raw, ascii_only=args.ascii, to_lower=args.lower)
        if not cleaned:
            continue
        u = username_from_name(cleaned)
        if u is None:
            skipped.append(f"LINE {idx}: {cleaned}")
            continue
        users.append(u)

    if args.dedupe:
        users = sorted(set(users))

    Path(args.output).write_text("\n".join(users) + ("\n" if users else ""), encoding="utf-8")
    Path(args.skipped).write_text("\n".join(skipped) + ("\n" if skipped else ""), encoding="utf-8")
    print(f"[OK] Generados={len(users)} | Omitidos={len(skipped)}")


if __name__ == "__main__":
    main()

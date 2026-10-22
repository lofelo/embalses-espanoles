"""Leer un embalse o verificar los datos; solo necesita Python estándar."""
import argparse
import csv
import gzip
import hashlib
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
DATA_FILES = {
    "data/observations.csv.gz", "data/reservoirs.csv", "data/coverage.csv",
    "data/source_geometries.geojson.gz", "data/alcantara_effective_geometry.geojson.gz",
}


def verify():
    entries = {}
    for line in (ROOT / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
        digest, name = line.split("  ", 1)
        if name not in DATA_FILES or name in entries:
            raise ValueError("Inventario de hashes no válido.")
        h = hashlib.sha256()
        with (ROOT / name).open("rb") as f:
            for block in iter(lambda: f.read(1024 * 1024), b""):
                h.update(block)
        if h.hexdigest() != digest:
            raise ValueError(f"Hash incorrecto: {name}")
        entries[name] = digest
    if set(entries) != DATA_FILES:
        raise ValueError("Faltan archivos en SHA256SUMS.")
    print("Los cinco archivos de datos coinciden con sus hashes.")


def show(reservoir_id):
    with (ROOT / "data/reservoirs.csv").open(encoding="utf-8", newline="") as f:
        reservoir = next((r for r in csv.DictReader(f, delimiter=";")
                          if r["reservoir_id"] == reservoir_id), None)
    if reservoir is None:
        raise ValueError("Identificador no encontrado; consulta data/reservoirs.csv.")
    years = {}
    with gzip.open(ROOT / "data/observations.csv.gz", "rt", encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f, delimiter=";"):
            if row["reservoir_id"] != reservoir_id:
                continue
            year = int(row["year"])
            area = float(row["area_m2"]) / 10000
            filled = float(row["area_filled_m2"]) / 10000
            stats = years.setdefault(year, [0, area, area, filled, filled])
            stats[0] += 1
            stats[1], stats[2] = min(stats[1], area), max(stats[2], area)
            stats[3], stats[4] = min(stats[3], filled), max(stats[4], filled)
    print(f"{reservoir_id} — {reservoir['name']} ({reservoir['basin']})")
    print("Rangos entre observaciones retenidas, en ha; no son medias anuales.")
    print("Año   Filas   Área óptica (ha)       Área con relleno (ha)")
    for year, (n, low, high, filled_low, filled_high) in sorted(years.items()):
        print(f"{year}  {n:5d}   {low:8.2f}–{high:8.2f}   {filled_low:8.2f}–{filled_high:8.2f}")
    print(f"Total: {sum(stats[0] for stats in years.values())} observaciones.")


def main():
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reservoir_id", nargs="?", default="ES_RES_0528")
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    try:
        verify() if args.verify else show(args.reservoir_id)
        return 0
    except (OSError, ValueError, KeyError, csv.Error, EOFError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

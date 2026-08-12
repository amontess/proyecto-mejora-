"""Calcula el tiempo promedio por estación a partir de datos/tiempos.csv."""

import csv
from collections import defaultdict
from pathlib import Path


def promedio_por_estacion(ruta_csv: Path) -> dict[str, float]:
    totales: dict[str, float] = defaultdict(float)
    conteos: dict[str, int] = defaultdict(int)

    with ruta_csv.open(newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            estacion = (fila.get("estacion") or "").strip()
            tiempo_raw = (fila.get("tiempo_seg") or "").strip()
            if not estacion or not tiempo_raw:
                continue
            totales[estacion] += float(tiempo_raw)
            conteos[estacion] += 1

    return {
        estacion: totales[estacion] / conteos[estacion]
        for estacion in sorted(totales)
    }


def main() -> None:
    ruta = Path(__file__).resolve().parent / "datos" / "tiempos.csv"
    if not ruta.exists():
        raise SystemExit(f"No se encontró el archivo: {ruta}")

    promedios = promedio_por_estacion(ruta)
    if not promedios:
        print("No hay datos de tiempos para analizar.")
        return

    print("Tiempo promedio por estación (segundos):")
    for estacion, promedio in promedios.items():
        print(f"  {estacion}: {promedio:.2f}")


if __name__ == "__main__":
    main()

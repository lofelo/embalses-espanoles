# Superficie de agua en 318 embalses españoles

**2017–2024 · 234.512 observaciones · versión 0.1.0**

Estimaciones de superficie de agua obtenidas con el método óptico
Donchyts / Global Water Watch, usando Landsat y Sentinel-2 sobre una muestra
MITECO de **318 embalses con capacidad ≥5 hm³**.
Los ocho años están procesados para todos los embalses.

## Usar los datos

Los CSV usan UTF-8, separador `;` y superficies en **m²**. La clave de unión es
`reservoir_id`. No necesitas Earth Engine ni instalar paquetes de Python.

```sh
python example.py
python example.py --verify
```

La primera orden muestra las observaciones de un embalse por año y sus rangos
de superficie. La segunda comprueba los hashes de los archivos de datos.

| Archivo | Contenido |
| --- | --- |
| `data/observations.csv.gz` | Observaciones por embalse y fecha UTC; 234.512 filas. |
| `data/reservoirs.csv` | Nombres, demarcaciones, capacidades e identificadores de los 318 embalses. |
| `data/coverage.csv` | Recuentos y procedencia de las 2.544 combinaciones embalse/año. |
| `data/*.geojson.gz` | Polígonos fuente y geometría efectiva complementaria en CRS84: longitud, latitud. |

Consulta [FIELDS.md](FIELDS.md) para interpretar las columnas.

## Tener en cuenta

- Es una muestra seleccionada, no todos los embalses españoles. El criterio inicial es volumen de almacenamiento, no hectáreas.
- Una fila es un mosaico retenido por embalse y fecha, no una medición para cada día. Una fecha ausente no significa superficie cero.
- `area_filled_m2` incorpora relleno histórico JRC; algunas estimaciones dependen mucho de él. `p=101` es un valor especial del método, no confianza del modelo.
- Se comprobó la integridad y el procesamiento completo. No se ha realizado una validación externa independiente de la exactitud de estas superficies.

## Licencia y fuentes

Las aportaciones originales de este proyecto se ofrecen bajo **CC0 1.0**:
puedes reutilizarlas sin exigir permiso ni atribución. Los materiales y
derechos de terceros conservan sus condiciones; véase [SOURCES.md](SOURCES.md).

# Campos y unidades

CSV UTF-8, separado por `;`, con punto decimal. `1 ha = 10.000 m²`.
Los identificadores son texto. Las capacidades en hm³ son atributos de
inventario, no volúmenes estimados a partir del satélite.

## Observaciones

Una fila por (`reservoir_id`, `time_utc`).

| Campo | Significado |
| --- | --- |
| `reservoir_id` | Identificador del embalse; enlaza con el catálogo y los polígonos fuente. |
| `time_utc` | Fecha UTC del mosaico, a medianoche; no hora original de adquisición. |
| `year` | Año de la observación, 2017–2024. |
| `mission` | Misión retenida: `S2`, `L7` o `L8`. |
| `area_m2` | Superficie clasificada como agua en la observación óptica. |
| `area_filled_m2` | Superficie que añade relleno basado en ocurrencia histórica JRC. |
| `filled_fraction` | Fracción del área rellenada aportada por el relleno: `(area_filled_m2 - area_m2) / area_filled_m2`. |
| `p` | Mediana de ocurrencia JRC en bordes usada para rellenar; **101 indica que falta esa mediana**. No es una probabilidad de exactitud. |
| `ndwi_threshold` | Umbral por observación del índice verde/SWIR, MNDWI, llamado `ndwi` en el método. |
| `quality_score` | Score de selección basado en el percentil 75 de la banda verde. No es confianza calibrada. |
| `scale` | Escala de cómputo en metros, fija por embalse; entre 10 y 58,70 m. |
| `geometry_delivery` | Variante de transporte de la geometría; Alcántara se procesó mediante un asset. |
| `geometry_json_sha256` | Identidad de la geometría efectiva según el hash de producción. |
| `source_geometry_json_sha256` | Identidad de la geometría anterior al transporte. |
| `geometry_asset_id` | Asset de Alcántara; vacío en los otros embalses. No garantiza acceso público al asset. |
| `computation_transport` | Cálculo interactivo, ventanas o exportación anual de tabla. |

No se ha añadido interpolación, agregación anual ni filtrado posterior.
Se conservan los casos con mucho relleno, las áreas muy pequeñas y los
2.163 valores `p=101`. La ausencia de fila no equivale a agua cero.

## Catálogo y cobertura

`reservoirs.csv` contiene `reservoir_id`, `name` (nombre), `basin`
(demarcación), `miteco_code`, `capacity_hm3` (capacidad), `geometry_quality`
(QA de la geometría) y `observation_count` (filas del embalse).

`coverage.csv` contiene `reservoir_id`, `year`, `processing_complete`,
`observation_count`, `first_observation_utc`, `last_observation_utc`,
`computation_transport` y `source_raw_sha256`. El hash identifica el raw anual
de producción, conservado en el archivo de auditoría del proyecto.
La primera y última observación no significan cobertura diaria.

## Geometrías

Los polígonos fuente son los del benchmark MITECO reproyectados a CRS84,
sin nueva simplificación. Para **Alcántara (`ES_RES_0528`)** se proporciona
además el objeto GeoJSON `Polygon` efectivo, con los mismos 43.709 vértices
y desplazamiento máximo medido de 0,00577 m tras el transporte. Este objeto
se identifica por su archivo; no tiene una propiedad `reservoir_id`.

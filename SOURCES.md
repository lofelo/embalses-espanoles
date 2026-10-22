# Fuentes y atribuciones

Las aportaciones propias al conjunto, la documentación y el ejemplo se
dedican a **CC0 1.0** ([LICENSE](LICENSE)). Esa dedicación solo alcanza los
derechos propios y no sustituye los de las fuentes siguientes.

- **MITECO:** geometrías y atributos del Inventario de Presas y Embalses; entidades oficiales para seleccionar la muestra. Fuente: © Ministerio para la Transición Ecológica y el Reto Demográfico. [Inventario y condiciones](https://www.miteco.gob.es/es/cartografia-y-sig/ide/descargas/agua/inventario-presas-embalses.html). Fuente publicada con actualización 31/12/2021; benchmark congelado el 11/07/2026. Se reproyectaron y seleccionaron geometrías; no se insinúa respaldo institucional.
- **Landsat / USGS:** Collection 2 TOA, misiones L7 y L8. [Datos de dominio público y reconocimiento USGS](https://www.usgs.gov/centers/eros/data-citation).
- **Copernicus Sentinel-2:** Contains modified Copernicus Sentinel data 2017–2024. [Condiciones](https://sentinels.copernicus.eu/documents/247904/690755/Sentinel_Data_Legal_Notice).
- **EC JRC / Google:** Global Surface Water v1.4 para el relleno. Pekel et al. (2016), [doi:10.1038/nature20584](https://doi.org/10.1038/nature20584). [Catálogo](https://developers.google.com/earth-engine/datasets/catalog/JRC_GSW1_4_GlobalSurfaceWater).
- **Método Donchyts / GWW:** Donchyts et al. (2022), [doi:10.1038/s41598-022-17074-6](https://doi.org/10.1038/s41598-022-17074-6). Ejecución local basada en `eepackages` v0.28.0, implementación original de Gennadii Donchyts bajo MIT. El conjunto contiene esta ejecución sobre geometrías MITECO, no una descarga de series de la aplicación GWW.
- **EarthEnv:** Wilson y Jetz (2016), [doi:10.1371/journal.pbio.1002415](https://doi.org/10.1371/journal.pbio.1002415). La [climatología de nubes](https://www.earthenv.org/cloud), CC BY-NC 4.0, se referencia mediante `users/gena/MODCF_meanannual` para seleccionar imágenes. Aquí no se redistribuye ese raster ni se le aplica CC0. La identidad y licencia exactas de ese asset y el alcance de posibles derechos sobre resultados derivados no están confirmados; no se afirma que NC se extienda automáticamente a toda la tabla.

## Procedencia de esta versión

La muestra congelada tiene 318 embalses, a partir de capacidad ≥5 hm³,
geometría utilizable y enlace con datos oficiales con cobertura en ≥7 de
los 8 años. Los 318 tienen el periodo satelital 2017–2024 procesado.

La escala es `max(10, sqrt(area_geometría_m2)/200)`. Se aplica selección de
calidad, MNDWI con Canny/Otsu y relleno JRC; no se generan medias anuales.
Alcántara tiene 1.200 observaciones: seis años compuestos por ventanas y dos
exportaciones anuales (2020 y 2022), descargadas y verificadas.

Las observaciones conservan exactamente el CSV integrado original al
descomprimir. SHA-256 de ese CSV:
`9d3d262e8b8eb7ad3decc77cd5e062f8f80928acf512dc88d1c010a20a7fd8c4`.
Los hashes de los archivos distribuidos están en `SHA256SUMS`.

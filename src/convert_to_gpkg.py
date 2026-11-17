import geopandas as gpd

# Convert the flood zone data from GeoJSON to GPKG format for efficient storage and processing
flood = gpd.read_file("data/raw/flood_zones/flood_zones.geojson")
flood.to_file(
    "data/processed/flood_zones/flood_zones.gpkg",
    driver="GPKG"
)
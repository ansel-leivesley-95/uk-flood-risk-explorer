import geopandas as gpd

flood = gpd.read_file("data/raw/flood_zones/flood_zones.geojson")

flood.to_file(
    "data/processed/flood_zones/flood_zones.gpkg",
    driver="GPKG"
)
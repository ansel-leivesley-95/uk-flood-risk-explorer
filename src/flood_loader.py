import geopandas as gpd


def load_flood_zones():
    flood_zones = gpd.read_file("data/raw/flood_zones/flood_zones.geojson")
    return flood_zones
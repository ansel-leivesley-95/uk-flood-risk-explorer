import os
import geopandas as gpd
from shapely.geometry import Point

from src.geocode import location_to_coords


def get_local_flood_zones(location_name: str, radius_km: int = 50):
    safe_name = (location_name.strip().lower().replace(" ", "_"))

    output_dir = "data/processed/flood_zones"
    os.makedirs(output_dir, exist_ok=True)
    output_file = (
        f"{output_dir}/{safe_name}.geojson"
    )

    if os.path.exists(output_file):
        print(f"Loading cached dataset: {location_name}")
        return gpd.read_file(output_file)

    print(f"Creating dataset: {location_name}")

    lat, lon = location_to_coords(location_name)
    flood = gpd.read_file("data/raw/flood_zones/flood_zones.geojson")

    centre = gpd.GeoDataFrame(
        geometry=[Point(lon, lat)],
        crs="EPSG:4326"
    )

    flood = flood.to_crs("EPSG:3857")
    centre = centre.to_crs("EPSG:3857")
    buffer = centre.buffer(radius_km * 1000)

    flood_local = flood[
        flood.intersects(
            buffer.iloc[0]
        )
    ]

    flood_local = flood_local.to_crs(
        "EPSG:4326"
    )

    flood_local.to_file(
        output_file,
        driver="GeoJSON"
    )

    return flood_local
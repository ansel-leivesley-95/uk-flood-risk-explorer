import os
import geopandas as gpd
from shapely.geometry import Point

from src.geocode import location_to_coords


def get_local_flood_zones(location_name: str, radius_km: int = 30):
    lat, lon = location_to_coords(location_name)
    output_dir = (
        "data/processed/flood_zones"
    )
    os.makedirs(
        output_dir,
        exist_ok=True
    )
    cache_name = (
        f"{lat:.2f}_{lon:.2f}_{radius_km}km"
        .replace(".", "_")
        .replace("-", "m")
    )
    output_file = (f"{output_dir}/{cache_name}.gpkg")

    if os.path.exists(output_file):
        print(f"Loading cached dataset: {location_name}")
        return gpd.read_file(output_file)

    print(f"Creating dataset: {location_name}")

    lat, lon = location_to_coords(location_name)
    flood = gpd.read_file("data/raw/flood_zones/flood_zones.gpkg")

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
        driver="GPKG"
    )

    return flood_local
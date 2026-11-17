import os
import geopandas as gpd

from shapely.geometry import Point
from src.geocode import location_to_coords

def get_local_flood_zones(location_name: str, radius_km: int = 30):
    """
    Retrieves flood zone data for a specified location within a given radius.
    """

    # Get the coordinates of the specified location
    lat, lon = location_to_coords(location_name)
    output_dir = (
        "data/processed/flood_zones"
    )

    # Create the output directory if it doesn't exist
    os.makedirs(
        output_dir,
        exist_ok=True
    )

    # Create a cache name based on the location's coordinates and the specified radius
    cache_name = (
        f"{lat:.2f}_{lon:.2f}_{radius_km}km"
        .replace(".", "_")
        .replace("-", "m")
    )
    output_file = (f"{output_dir}/{cache_name}.gpkg")

    # Check if the flood zone data for the specified location and radius already exists in the cache
    if os.path.exists(output_file):
        print(f"Loading cached dataset: {location_name}")
        return gpd.read_file(output_file)

    print(f"Creating dataset: {location_name}")

    # Get the coordinates of the specified location
    lat, lon = location_to_coords(location_name)
    flood = gpd.read_file("data/raw/flood_zones/flood_zones.gpkg")

    # Create a GeoDataFrame for the specified location's coordinates
    centre = gpd.GeoDataFrame(
        geometry=[Point(lon, lat)],
        crs="EPSG:4326"
    )

    # Transform the flood zone data and the location's coordinates to a projected coordinate system (EPSG:3857) for accurate distance calculations
    flood = flood.to_crs("EPSG:3857")
    centre = centre.to_crs("EPSG:3857")
    buffer = centre.buffer(radius_km * 1000)

    # Filter the flood zone data to include only those features that intersect with the buffer around the specified location
    flood_local = flood[
        flood.intersects(
            buffer.iloc[0]
        )
    ]

    # Transform the filtered flood zone data back to the geographic coordinate system (EPSG:4326) for further processing and visualisation
    flood_local = flood_local.to_crs(
        "EPSG:4326"
    )

    # Save the filtered flood zone data to a GeoPackage file for caching and future use
    flood_local.to_file(
        output_file,
        driver="GPKG"
    )

    return flood_local
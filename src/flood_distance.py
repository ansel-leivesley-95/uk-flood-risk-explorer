from shapely.geometry import Point
import geopandas as gpd

def nearest_flood_zone_distance(
        lat,
        lon,
        flood_zones
):
    """
    Calculate the distance from a point to the nearest flood zone.
    """
    
    # Create a GeoDataFrame for the specified point using its latitude and longitude
    point = gpd.GeoDataFrame(geometry=[Point(lon, lat)], crs="EPSG:4326")
    point = point.to_crs(epsg=3857)

    # Transform the flood zone geometries to the same projected coordinate system (EPSG:3857) 
    # for accurate distance calculations
    zones = flood_zones.to_crs(epsg=3857)

    # Calculate the distance from the specified point to each flood zone and find the minimum distance
    distance = zones.distance(point.geometry.iloc[0]).min()

    return round(distance, 1)
from shapely.geometry import Point
import geopandas as gpd

def nearest_flood_zone_distance(
        lat,
        lon,
        flood_zones
):
    point = gpd.GeoDataFrame(geometry=[Point(lon, lat)], crs="EPSG:4326")
    point = point.to_crs(epsg=3857)

    zones = flood_zones.to_crs(epsg=3857)

    distance = zones.distance(point.geometry.iloc[0]).min()

    return round(distance, 1)
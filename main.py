from src.geocode import location_to_coords
from src.preprocess_flood_zones import get_local_flood_zones
from src.map_builder import create_map
from src.flood_analyser import assess_flood_risk
from src.flood_distance import nearest_flood_zone_distance


def main():
    location = input("\nEnter a UK location: ").strip()
    lat, lon = location_to_coords(location)

    print(f"\nLatitude : {lat}")
    print(f"Longitude: {lon}")

    flood_zones = get_local_flood_zones(location_name=location, radius_km=50)
    risk = assess_flood_risk(lat=lat, lon=lon, flood_zones=flood_zones)

    distance = nearest_flood_zone_distance(lat=lat, lon=lon, flood_zones=flood_zones)

    print("\nFlood Risk Assessment:")
    print("-" * 20)
    print(f"In Flood Zone: {risk['in_flood_zone']}")
    print(f"Risk Level: {risk['risk']}")
    print(f"Flood Zone: {risk['zone']}")
    print(f"Distance to Nearest Flood Zone: {distance} meters")
    print(f"Flood Source: {risk['source']}")
    
    print(f"\nLoaded {len(flood_zones):,} flood features")

    output_file = create_map(
        lat=lat,
        lon=lon,
        location=location,
        flood_zones=flood_zones,
        risk = risk
    )

    print(f"\nMap saved to: {output_file}")
    print("\nOpening map in browser...")

if __name__ == "__main__":
    main()
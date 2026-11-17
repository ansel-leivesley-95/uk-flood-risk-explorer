# Import all necessary modules and functions from the various source files in the src directory
from src.geocode import location_to_coords
from src.preprocess_flood_zones import get_local_flood_zones
from src.map_builder import create_map
from src.flood_analyser import assess_flood_risk
from src.flood_distance import nearest_flood_zone_distance
from src.report_generator import generate_report


def main():
    """
    Main function to run the flood risk assessment tool, which prompts the user for a UK location, 
    retrieves flood zone data, assesses flood risk, generates a report, and creates an interactive map.
    """
    # Prompt the user for a UK location and retrieve its coordinates
    location = input("\nEnter a UK location: ").strip()
    lat, lon = location_to_coords(location)

    print(f"\nLatitude : {lat}")
    print(f"Longitude: {lon}")

    # Retrieve local flood zones within a 50 km radius of the specified location
    flood_zones = get_local_flood_zones(location_name=location, radius_km=50)
    # Assess the flood risk for the specified location based on the retrieved flood zones
    risk = assess_flood_risk(lat=lat, lon=lon, flood_zones=flood_zones)

    # Calculate the distance to the nearest flood zone from the specified location
    distance = nearest_flood_zone_distance(lat=lat, lon=lon, flood_zones=flood_zones)

    # Generate a PDF report summarizing the flood risk assessment and save it to a file
    report_file = generate_report(
        location=location,
        lat=lat,
        lon=lon,
        risk=risk,
        distance=distance
    )

    # Print the path to the saved PDF report
    print(f"PDF report saved to: {report_file}")

    # Print the flood risk assessment results to the console
    print("\nFlood Risk Assessment:")
    print("-" * 20)
    print(f"In Flood Zone: {risk['in_flood_zone']}")
    print(f"Risk Level: {risk['risk']}")
    print(f"Flood Zone: {risk['zone']}")
    print(f"Distance to Nearest Flood Zone: {distance} meters")
    print(f"Flood Source: {risk['source']}")
    
    print(f"\nLoaded {len(flood_zones):,} flood features")

    # Create an interactive map visualizing the flood zones and the specified location, and save it to a file
    output_file = create_map(
        lat=lat,
        lon=lon,
        location=location,
        risk = risk,
        distance = distance,
        flood_zones=flood_zones
    )

    print(f"\nMap saved to: {output_file}")
    print("\nOpening map in browser...")

# Run the main function if script is executed directly
if __name__ == "__main__":
    main()
from shapely.geometry import Point

def assess_flood_risk(lat: float, lon: float, flood_zones) -> dict:
    """
    Assess the flood risk for a given geographic location based on its latitude and longitude,
    and the provided flood zone data.
    """

    # Create a Point object representing the specified geographic location using its latitude and longitude
    location = Point(lon, lat)
    matches = flood_zones[flood_zones.contains(location)]

    # If there are no flood zones that contain the specified location, 
    # return a dictionary indicating that the location is not in a flood zone, 
    # with a low risk level and no associated flood zone or source information
    if len(matches) == 0:
        return {
            "in_flood_zone": False,
            "risk": "Low",
            "zone": None,
            "source": None
        }
    # If the specified location is contained within a flood zone, 
    # check if it is in a high-risk flood zone (FZ3).
    if (
        matches["flood_zone"]
        .eq("FZ3")
        .any()
    ):

        row = matches[
            matches["flood_zone"] == "FZ3"
        ].iloc[0]

        return {
            "in_flood_zone": True,
            "risk": "High",
            "zone": "FZ3",
            "source": row["flood_source"]
        }

    row = matches.iloc[0]

    return {
        "in_flood_zone": True,
        "risk": "Moderate",
        "zone": row["flood_zone"],
        "source": row["flood_source"]
    }
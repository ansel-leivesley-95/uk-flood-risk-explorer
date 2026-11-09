from shapely.geometry import Point

def assess_flood_risk(lat: float, lon: float, flood_zones) -> dict:
    location = Point(lon, lat)

    matches = flood_zones[flood_zones.contains(location)]

    if len(matches) == 0:

        return {
            "in_flood_zone": False,
            "risk": "Low",
            "zone": None,
            "source": None
        }

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
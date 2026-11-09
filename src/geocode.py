from geopy.geocoders import Nominatim

def location_to_coords(location: str) -> tuple[float, float]:
    geolocator = Nominatim(
        user_agent="uk_flood_risk_explorer"
    )

    result = geolocator.geocode(
        f"{location}, United Kingdom"
    )

    if result is None:
        raise ValueError(
            f"Could not locate '{location}'"
        )

    return (
        result.latitude,
        result.longitude
    )
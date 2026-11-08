from geopy.geocoders import Nominatim

def postcode_to_coords(postcode: str) -> tuple:
    geolocator = Nominatim(user_agent="uk_flood_risk_explorer")

    location = geolocator.geocode(f"{postcode}, United Kingdom")

    if location is None:
        raise ValueError(f"Could not find coordinates for postcode: {postcode}")

    return (location.latitude, location.longitude)
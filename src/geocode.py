from geopy.geocoders import Nominatim

def location_to_coords(location: str) -> tuple[float, float]:
    """
    Convert a location name to geographic coordinates (latitude and longitude) using the 
    Nominatim geocoding service.
    """

    # Initialise the Nominatim geocoder with a user agent to identify the application making requests
    geolocator = Nominatim(
        user_agent="uk_flood_risk_explorer"
    )

    # Use the geocoder to retrieve the geographic coordinates for the specified location, appending ", 
    # United Kingdom" to ensure accurate results within the UK
    result = geolocator.geocode(
        f"{location}, United Kingdom"
    )

    # If the geocoding service does not return a result, raise a ValueError indicating that the 
    # location could not be found
    if result is None:
        raise ValueError(
            f"Could not locate '{location}'"
        )

    return (result.latitude, result.longitude)
from geocode import postcode_to_coords
from map_builder import create_map


postcode = "NE1 4LP"

lat, lon = postcode_to_coords(
    postcode
)

print(f"Postcode: {postcode}")
print(f"Latitude: {lat}")
print(f"Longitude: {lon}")

create_map(
    lat,
    lon,
    postcode
)
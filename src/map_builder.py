import folium
import webbrowser
from pathlib import Path


def create_map(
    lat,
    lon,
    location,
    flood_zones=None
):

    m = folium.Map(
        location=[lat, lon],
        zoom_start=11
    )

    folium.Marker(
        [lat, lon],
        popup=location,
        tooltip=location
    ).add_to(m)

    if flood_zones is not None:

        folium.GeoJson(
            flood_zones,
            name="Flood Zones"
        ).add_to(m)

    folium.LayerControl().add_to(m)

    output_file = Path(
        "outputs/map.html"
    )

    m.save(output_file)

    webbrowser.open(
        output_file.resolve().as_uri()
    )

    return output_file
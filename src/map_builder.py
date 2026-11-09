import folium
import webbrowser
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
carto_key = os.getenv("CARTO_API_KEY")


def create_map(
    lat,
    lon,
    location,
    flood_zones=None,
    risk=None
):

    m = folium.Map(
        location=[lat, lon],
        zoom_start=11,
        tiles=f"https://basemaps.cartocdn.com/rastertiles/voyager/{{z}}/{{x}}/{{y}}.png?key={carto_key}",
        attr="© CARTO"
    )

    colour = "green"
    if risk:
        if risk["risk"] == "Moderate":
            colour = "orange"
        if risk["risk"] == "High":
            colour = "red"

    folium.Marker(
        [lat, lon],
        popup=location,
        tooltip=location,
        icon=folium.Icon(
            color=colour
        )
    ).add_to(m)

    if flood_zones is not None:
        def style_function(feature):

            zone = feature["properties"]["flood_zone"]

            if zone == "FZ3":

                return {
                    "fillColor": "red",
                    "color": "red",
                    "weight": 1,
                    "fillOpacity": 0.5
                }

            return {
                "fillColor": "orange",
                "color": "orange",
                "weight": 1,
                "fillOpacity": 0.5
            }


        folium.GeoJson(
            flood_zones,
            name="Flood Zones",
            style_function=style_function
        ).add_to(m)

    folium.LayerControl().add_to(m)
    output_file = Path(
        "outputs/map.html"
    )

    m.save(output_file)
    webbrowser.open(output_file.resolve().as_uri())
    return output_file
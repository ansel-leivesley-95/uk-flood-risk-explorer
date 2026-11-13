import folium
import webbrowser
import os

from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

carto_key = os.getenv(
    "CARTO_API_KEY"
)


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

    risk_level = "Unknown"

    if risk is not None:

        risk_level = risk["risk"]

        if risk_level == "Moderate":
            colour = "orange"

        if risk_level == "High":
            colour = "red"

    folium.Marker(
        [lat, lon],

        popup=folium.Popup(

            f"""
            <b>{location}</b><br>
            Risk: {risk_level}
            """,

            max_width=300

        ),

        tooltip=location,

        icon=folium.Icon(
            color=colour
        )

    ).add_to(m)

    def style_function(feature):

        zone = feature["properties"][
            "flood_zone"
        ]

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

    if flood_zones is not None:

        folium.GeoJson(

            flood_zones,

            name="Flood Zones",

            style_function=style_function,

            tooltip=folium.GeoJsonTooltip(

                fields=[
                    "flood_zone",
                    "flood_source"
                ],

                aliases=[
                    "Zone",
                    "Source"
                ]

            )

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
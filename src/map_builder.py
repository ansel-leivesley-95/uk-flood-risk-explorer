import os
import webbrowser
from pathlib import Path

import folium
from dotenv import load_dotenv
from shapely import distance

load_dotenv()

CARTO_API_KEY = os.getenv("CARTO_API_KEY")


def create_map(
    lat: float,
    lon: float,
    location: str,
    flood_zones=None,
    risk: dict | None = None,
    distance: float | None = None
) -> Path:
    """
    Generate an interactive flood risk map.

    Parameters
    ----------
    lat : float
        Latitude of assessment location.

    lon : float
        Longitude of assessment location.

    location : str
        User-entered location.

    flood_zones : GeoDataFrame, optional
        Flood polygons.

    risk : dict, optional
        Flood risk assessment output.

    distance : float, optional
        Distance to nearest flood zone (m).

    Returns
    -------
    Path
        Location of saved HTML map.
    """

    # Initialise default values for risk assessment and marker color
    risk_level = "Unknown"
    flood_zone = "N/A"
    flood_source = "N/A"

    marker_colour = "green"

    if risk:
        # Extract risk assessment details from the provided risk dictionary
        risk_level = risk["risk"]
        flood_zone = (
            risk["zone"]
            if risk["zone"]
            else "None"
        )
        # Extract flood source information, defaulting to "None" if not available
        flood_source = (
            risk["source"]
            if risk["source"]
            else "None"
        )

        # Determine marker color based on the assessed risk level
        if risk_level == "Moderate":
            marker_colour = "orange"
        # Determine marker color for high risk level
        elif risk_level == "High":
            marker_colour = "red"

    # Create a Folium map centered on the specified latitude and longitude, with a zoom level of 11 and 
    # a custom basemap from CARTO
    m = folium.Map(
        location=[lat, lon],
        zoom_start=11,
        control_scale=True,
        tiles=(
            f"https://basemaps.cartocdn.com/"
            f"rastertiles/voyager/"
            f"{{z}}/{{x}}/{{y}}.png"
            f"?key={CARTO_API_KEY}"
        ),
        attr="© CARTO"
    )

    # Create an HTML popup for the marker, displaying the location name, risk level, flood zone, flood source, 
    # and distance to the nearest flood zone
    popup_html = f"""
    <div style="
        width:280px;
        font-family:Arial;
    ">

    <h3 style="
        margin-bottom:10px;
        color:#003366;
    ">
    Flood Risk Assessment
    </h3>

    <b>Location</b><br>
    {location}<br><br>

    <b>Risk Level</b><br>
    {risk_level}<br><br>

    <b>Flood Zone</b><br>
    {flood_zone}<br><br>

    <b>Flood Source</b><br>
    {flood_source}<br><br>

    <b>Nearest Flood Zone</b><br>
    {"Unknown" if distance is None else f"{distance:.1f} m"}

    </div>
    """
    
    # Add a marker to the map at the specified latitude and longitude, with a popup displaying the risk assessment details,
    # a tooltip showing the location and risk level, and a colored icon based on the assessed risk level
    folium.CircleMarker(
        location=[lat, lon],
        radius=12,
        color="black",
        weight=2,
        fill=True,
        fill_color=marker_colour,
        fill_opacity=0.95,
        popup=folium.Popup(
            popup_html,
            max_width=350
        ),
        tooltip="Click for assessment details"
    ).add_to(m)

    def style_function(feature):
        """
        Style flood polygons according to
        flood zone classification.

        FZ3 = High Risk
        FZ2 = Medium Risk
        """

        zone = feature["properties"]["flood_zone"]

        if zone == "FZ3":

            return {
                "fillColor": "#d73027",
                "color": "#990000",
                "weight": 2,
                "fillOpacity": 0.45
            }

        return {
            "fillColor": "#fdae61",
            "color": "#cc6600",
            "weight": 2,
            "fillOpacity": 0.35
        }


    if flood_zones is not None:
        folium.GeoJson(
            flood_zones,
            name="Flood Zones",
            style_function=style_function,

            highlight_function=lambda feature: {
                "weight": 4,
                "fillOpacity": 0.7
            },

            tooltip=folium.GeoJsonTooltip(
                fields=[
                    "flood_zone",
                    "flood_source"
                ],
                aliases=[
                    "Flood Zone",
                    "Flood Source"
                ],
                localize=True,
                sticky=False,
                labels=True
            )
        ).add_to(m)

    legend_html = """
    <div style="
    position: fixed;
    bottom: 40px;
    left: 40px;
    z-index: 9999;

    background-color: white;
    padding: 15px;

    border: 2px solid #555;
    border-radius: 8px;

    font-size: 14px;
    font-family: Arial;

    box-shadow: 2px 2px 6px rgba(0,0,0,0.3);
    ">

    <b>Flood Risk Legend</b>

    <hr>

    <div>
    <span style="
    background:#d73027;
    width:14px;
    height:14px;
    display:inline-block;
    margin-right:5px;
    "></span>

    Flood Zone 3
    </div>

    <div>
    <span style="
    background:#fdae61;
    width:14px;
    height:14px;
    display:inline-block;
    margin-right:5px;
    "></span>

    Flood Zone 2
    </div>

    <div>
    <span style="
    background:green;
    width:14px;
    height:14px;
    display:inline-block;
    margin-right:5px;
    "></span>

    Assessment Location
    </div>

    </div>
    """
    # Add the legend HTML to the map as a child element, ensuring it is displayed on the map interface
    m.get_root().html.add_child(
        folium.Element(
            legend_html
        )
    )
    # Save the generated map to an HTML file in the "outputs" directory, creating the directory if it doesn't exist
    output_file = Path(
        "outputs/map.html"
    )

    # Save the generated map to an HTML file in the "outputs" directory
    m.save(output_file)
    # Open the saved HTML map in the default web browser for immediate viewing
    webbrowser.open(
        output_file.resolve().as_uri()
    )

    return output_file
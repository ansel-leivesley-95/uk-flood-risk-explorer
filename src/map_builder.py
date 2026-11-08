import folium
import webbrowser


def create_map(lat, lon, postcode):

    m = folium.Map(
        location=[lat, lon],
        zoom_start=13
    )

    folium.Marker(
        [lat, lon],
        popup=postcode
    ).add_to(m)

    output = "outputs/map.html"

    m.save(output)

    webbrowser.open(output)
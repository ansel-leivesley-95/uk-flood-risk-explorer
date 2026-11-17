from pathlib import Path
from datetime import datetime

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    Table,
    TableStyle
)

from reportlab.lib import colors

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def generate_report(
    location,
    lat,
    lon,
    risk,
    distance
):
    """
    Generate a professional flood risk
    assessment report.
    """

    safe_name = (
        location.lower()
        .replace(" ", "_")
    )

    output_file = (
        Path("outputs")
        / f"{safe_name}_flood_report.pdf"
    )

    doc = SimpleDocTemplate(
        str(output_file)
    )

    styles = getSampleStyleSheet()

    content = []

    # -----------------------------------
    # COVER PAGE
    # -----------------------------------

    content.append(
        Paragraph(
            "UK FLOOD RISK EXPLORER",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            "Flood Risk Assessment Report",
            styles["Heading1"]
        )
    )

    content.append(
        Spacer(1, 30)
    )

    content.append(
        Paragraph(
            f"<b>Location:</b> {location}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"<b>Assessment Date:</b> "
            f"{datetime.now():%d %B %Y %H:%M}",
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 150)
    )

    content.append(
        Paragraph(
            "Generated using UK Flood Risk Explorer",
            styles["Italic"]
        )
    )

    content.append(
        PageBreak()
    )

    # -----------------------------------
    # ASSESSMENT SUMMARY
    # -----------------------------------

    content.append(
        Paragraph(
            "Assessment Summary",
            styles["Heading1"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    table_data = [

        ["Parameter", "Result"],

        ["Location", location],

        ["Latitude", f"{lat:.5f}"],

        ["Longitude", f"{lon:.5f}"],

        ["Risk Level", risk["risk"]],

        ["Flood Zone", str(risk["zone"])],

        ["Flood Source", str(risk["source"])],

        ["Nearest Flood Zone",
         f"{distance:.1f} m"]

    ]

    table = Table(
        table_data,
        colWidths=[150, 250]
    )

    table.setStyle(
        TableStyle([

            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.darkblue
            ),

            (
                "TEXTCOLOR",
                (0, 0),
                (-1, 0),
                colors.white
            ),

            (
                "GRID",
                (0, 0),
                (-1, -1),
                1,
                colors.black
            ),

            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                "Helvetica-Bold"
            ),

        ])
    )

    content.append(
        table
    )

    content.append(
        Spacer(1, 20)
    )

    # -----------------------------------
    # EXECUTIVE SUMMARY
    # -----------------------------------

    content.append(
        Paragraph(
            "Executive Summary",
            styles["Heading2"]
        )
    )

    if risk["risk"] == "High":

        summary = f"""
        The assessment location lies within
        a mapped Flood Zone 3 area.

        The site has been classified as
        High Flood Risk.

        Further detailed investigation
        is recommended.
        """

    elif risk["risk"] == "Moderate":

        summary = f"""
        The assessment location lies within
        Flood Zone 2.

        The site has been classified as
        Moderate Flood Risk.

        Site-specific assessment may be
        appropriate depending on the
        proposed development.
        """

    else:

        summary = f"""
        The assessment location lies
        outside mapped Flood Zone 2
        and Flood Zone 3 extents.

        The nearest mapped flood area
        is approximately
        {distance:.1f} metres from
        the assessment location.

        Overall flood risk has been
        classified as Low.
        """

    content.append(
        Paragraph(
            summary,
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    # -----------------------------------
    # METHODOLOGY
    # -----------------------------------

    content.append(
        Paragraph(
            "Methodology",
            styles["Heading2"]
        )
    )

    methodology = """
    1. User location geocoded using
       OpenStreetMap Nominatim.

    2. Environment Agency flood data
       loaded and processed.

    3. Spatial intersection analysis
       performed.

    4. Distance to nearest flood zone
       calculated.

    5. Flood risk classification
       generated.
    """

    content.append(
        Paragraph(
            methodology,
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    # -----------------------------------
    # DATA SOURCES
    # -----------------------------------

    content.append(
        Paragraph(
            "Data Sources",
            styles["Heading2"]
        )
    )

    data_sources = """
    • UK Flood Zone Dataset

    • OpenStreetMap

    • Nominatim Geocoding Service
    """

    content.append(
        Paragraph(
            data_sources,
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    # -----------------------------------
    # DISCLAIMER
    # -----------------------------------

    content.append(
        Paragraph(
            "Disclaimer",
            styles["Heading2"]
        )
    )

    disclaimer = """
    This report provides an indicative
    flood risk assessment based upon
    publicly available datasets.

    The report should not be considered
    a substitute for a professional flood
    risk assessment undertaken by a
    qualified specialist.
    """

    content.append(
        Paragraph(
            disclaimer,
            styles["BodyText"]
        )
    )

    doc.build(content)

    return output_file
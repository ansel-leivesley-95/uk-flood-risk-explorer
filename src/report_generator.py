from pathlib import Path
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer)
from reportlab.lib.styles import (getSampleStyleSheet)

def generate_report(location, lat, lon, risk, distance):
    """
    Generates a flood risk assessment report for a given location.
    """

    # Create a safe filename for the report and ensure saved in a suitable location
    safe_name = (location.lower().replace(" ", "_"))
    output_file = (Path("outputs")/ f"{safe_name}_flood_report.pdf")

    # Create the PDF report
    pdf = SimpleDocTemplate(str(output_file))
    # Get the default styles
    styles = getSampleStyleSheet()

    # Add content to the report, including the location, coordinates, risk level, and distance to nearest flood zone
    # Adding a title, ensuring consistent spacing and formatting, and using the appropriate styles for each section
    content = [Paragraph(f"Flood Risk Assessment Report for {location}", styles["Title"]),
        Spacer(1, 12),
        Paragraph(
            f"Location: {location}",
            styles["BodyText"]
        ),
        Paragraph(
            f"Latitude: {lat}",
            styles["BodyText"]
        ),
        Paragraph(
            f"Longitude: {lon}",
            styles["BodyText"]
        ),
        Paragraph(
            f"Risk Level: {risk['risk']}",
            styles["BodyText"]
        ),
        Paragraph(
            f"In Flood Zone: {risk['in_flood_zone']}",
            styles["BodyText"]
        ),
        Paragraph(
            f"Flood Source: {risk['source']}",
            styles["BodyText"]
        ),
        Paragraph(
            f"Distance to Nearest Flood Zone: {distance} metres",
            styles["BodyText"]
        )
    ]
    
    # Build the PDF report and save it to the specified output file
    pdf.build(content)
    return output_file
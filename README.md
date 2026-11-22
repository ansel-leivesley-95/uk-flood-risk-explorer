# UK Flood Risk Explorer

A Python-based GIS pipeline for assessing flood risk across the United Kingdom using geospatial analysis, flood zone datasets and automated reporting.

The application enables users to enter a UK location or postcode, assess local flood risk, visualise flood extents on an interactive map and generate professional PDF flood risk assessment reports.

---

## Overview

UK Flood Risk Explorer combines geocoding, spatial analysis, automated data processing and interactive mapping to provide rapid flood-risk screening for a specified location.

The pipeline:

1. Converts a location or postcode into geographic coordinates.
2. Retrieves a local subset of national flood zone data.
3. Performs point-in-polygon flood risk analysis.
4. Calculates the distance to the nearest flood zone.
5. Generates an interactive web map.
6. Produces a professional PDF flood risk assessment report.

---

## Key Features

### Location Geocoding

Convert UK place names and postcodes into latitude and longitude coordinates using OpenStreetMap Nominatim.

Example inputs:

- Newcastle Upon Tyne
- Edinburgh
- Bristol
- UK Postcode

---

### Flood Dataset Processing

The application automatically:

- Loads flood zone data
- Creates local subsets of national datasets
- Caches processed datasets for future use
- Reuses cached datasets on subsequent runs

This significantly improves performance when analysing the same locations repeatedly.

---

### Flood Zone Classification

Perform spatial analysis to determine whether an assessment location falls within:

- Flood Zone 2 (Medium Probability)
- Flood Zone 3 (High Probability)

Risk levels are automatically assigned.

---

### Distance Analysis

For locations outside mapped flood zones, the application calculates:

- Distance to the nearest flood zone
- Flood source information
- Risk classification

---

### Interactive Mapping

Generate interactive web maps containing:

- Assessment location
- Flood Zone 2 polygons
- Flood Zone 3 polygons
- Dynamic scale bar
- Interactive legend
- Polygon inspection tools
- Risk-based styling

Maps are automatically opened in the default web browser.

---

### Automated Reporting

Generate professional PDF reports containing:

- Assessment metadata
- Geographic coordinates
- Flood risk classification
- Flood zone information
- Distance analysis
- Executive summary
- Methodology
- Data sources
- Disclaimer

Reports are automatically exported to the outputs directory.

---

## Workflow

```text
Location / Postcode
          │
          ▼
      Geocoding
          │
          ▼
Coordinate Extraction
          │
          ▼
Cached Dataset Lookup
          │
          ▼
Spatial Analysis
          │
          ▼
Flood Risk Assessment
          │
          ▼
Distance Analysis
          │
    ┌─────┴─────┐
    ▼           ▼
Interactive    PDF
    Map       Report
```

---

## Example Output

```text
Enter a UK location:

Example UK Postcode

Latitude : 54.xxxxx
Longitude: -1.xxxxx

Loading cached dataset

Flood Risk Assessment
---------------------

In Flood Zone: False
Risk Level: Low
Flood Zone: None
Flood Source: None
Distance to Nearest Flood Zone: 300 m

Map saved to outputs/map.html

PDF report saved successfully
```

---

## Repository Structure

```text
UK-Flood-Risk-Explorer/

├── data/
│   ├── raw/
│   └── processed/
│
├── outputs/
│   ├── map.html
│   └── flood_report.pdf
│
├── src/
│   ├── flood_analyser.py
│   ├── flood_distance.py
│   ├── geocode.py
│   ├── map_builder.py
│   ├── preprocess_flood_zones.py
│   ├── report_generator.py
│   └── convert_to_gpkg.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Technologies Used

### GIS and Spatial Analysis

- GeoPandas
- Shapely
- PyProj

### Mapping

- Folium
- CARTO Basemaps

### Data Processing

- Pandas

### Geocoding

- Geopy
- OpenStreetMap Nominatim

### Reporting

- ReportLab

---

## Current Capabilities

- Location geocoding
- Postcode geocoding
- Flood dataset preprocessing
- Local dataset caching
- Flood zone intersection analysis
- Distance-to-flood-zone analysis
- Interactive web mapping
- Automated PDF reporting

---

## Planned Next Steps of Repo

- Embedded map figures within PDF reports
- Enhanced flood risk scoring
- River proximity assessment
- Surface water flood-risk analysis
- Multi-hazard environmental screening
---

## Disclaimer

This application provides an indicative flood-risk assessment using publicly available datasets.

Results should not be considered a substitute for a detailed professional flood-risk assessment undertaken by qualified specialists.

---

## Licence

MIT Licence.
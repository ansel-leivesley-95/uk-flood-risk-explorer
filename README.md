# UK Flood Risk Explorer

An open-source Python GIS application for assessing flood risk across the United Kingdom using publicly available flood zone datasets and geospatial analysis.

The tool allows users to enter a location, automatically geocode it, retrieve local flood zone information, assess flood risk, and generate an interactive web map displaying the results.

---

## Features

### Location Geocoding

Convert UK place names and postcodes into geographic coordinates using OpenStreetMap Nominatim services.

Examples:

- Newcastle Upon Tyne
- Edinburgh
- Bristol
- NE1 4LP

---

### Flood Dataset Processing

The application uses official flood zone data and automatically:

- Loads the national flood dataset
- Clips the dataset around a user-defined location
- Creates localised datasets for faster processing
- Caches processed data for future use

This significantly improves performance when analysing multiple locations.

---

### Flood Risk Assessment

Performs geospatial point-in-polygon analysis to determine whether a location lies within:

- Flood Zone 2 (Medium Risk)
- Flood Zone 3 (High Risk)

Risk classifications are automatically returned to the user.

---

### Interactive Mapping

Generate interactive web maps showing:

- User location
- Flood zone polygons
- Risk classification
- Flood sources

Maps are exported as HTML and automatically opened in the default web browser.

---

## Project Workflow

```text
User Location
      ↓
Geocoding
      ↓
Coordinate Extraction
      ↓
Load Cached Dataset
      ↓
(Generate Local Dataset if Needed)
      ↓
Flood Zone Analysis
      ↓
Risk Classification
      ↓
Interactive Map
```

---

## Repository Structure

```text
UK-Flood-Risk-Explorer/
│
├── data/
│   ├── raw/
│   │   └── flood_zones/
│   │
│   └── processed/
│       └── flood_zones/
│
├── outputs/
│
├── src/
│   ├── flood_analyser.py
│   ├── flood_loader.py
│   ├── geocode.py
│   ├── map_builder.py
│   ├── preprocess_flood_zones.py
│   └── __init__.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Technologies Used

### GIS

- GeoPandas
- Shapely
- PyProj

### Mapping

- Folium

### Data Processing

- Pandas

### Geocoding

- Geopy
- OpenStreetMap Nominatim

### Environment

- Python
- Virtual Environments

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/uk-flood-risk-explorer.git
cd uk-flood-risk-explorer
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate:

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the application:

```bash
python main.py
```

Enter a UK location:

```text
Enter a UK location:
Newcastle Upon Tyne
```

Example output:

```text
Latitude : 54.9738
Longitude: -1.6131

Flood Risk Assessment
--------------------

In Flood Zone : False
Risk Level    : Low
Flood Zone    : None
```

An interactive map will automatically be generated and opened in your web browser.

---

## Data Sources

This project uses publicly available open datasets including:

- UK Flood Zone Data
- OpenStreetMap
- Nominatim Geocoding Service

All data remains the property of their respective providers.

---

## Current Capabilities

- [x] Location geocoding
- [x] Interactive web mapping
- [x] Flood zone dataset loading
- [x] Local dataset caching
- [x] Flood risk assessment
- [x] Flood Zone 2 and 3 visualisation

---

## Future Development

Planned enhancements:

- Distance to nearest flood zone
- Automated flood assessment reports
- Streamlit web application
- Downloadable PDF reports
- Additional environmental hazard layers
- Surface water flood risk assessment
- River network analysis
- Web deployment

---

## Example Application

This project demonstrates practical skills in:

- Geographic Information Systems (GIS)
- Geospatial data engineering
- Environmental risk assessment
- Python software development
- Spatial analysis
- Open-source geospatial workflows

---

## Licence

This project is released under the MIT Licence.

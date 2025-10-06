# NASA API Tester

Due to the wall of political change being build, some of the NASA public APIs are not available  
A Python script to test the availability and response times of various NASA APIs.

## Features

- Tests 12 different NASA APIs
- Response time tracking
- Results saved to JSON file
- 10-second timeout for each request

## Installation

1. Install the required dependency:
```bash
pip install -r requirements.txt
```

## Usage

Run the script:
```bash
python nasa_api_tester.py
```

## APIs Tested

1. **CMR API** - Common Metadata Repository for Earth science data
2. **GIBS WMTS** - Global Imagery Browse Services Web Map Tile Service
3. **NASA POWER API** - Prediction of Worldwide Energy Resources
4. **AppEEARS API** - Application for Extracting and Exploring Analysis Ready Samples
5. **NASA Open APIs - APOD** - Astronomy Picture of the Day
6. **NASA Open APIs - EPIC** - Earth Polychromatic Imaging Camera
7. **NASA Open APIs - Earth** - Earth imagery and assets
8. **EONET** - Earth Observatory Natural Event Tracker
9. **Earthdata Search** - Earthdata Search API health check

## Output

The script will:
- Show response times for each API
- Print a summary of active vs inactive APIs
- Save detailed results to `nasa_api_status.json`

## Notes

06.10.2025 test result

Active APIs (7/12):
CMR API - Active (0.98s response time)
GIBS WMTS GetCapabilities - Active (1.26s response time)
NASA POWER API - Active (1.86s response time)
AppEEARS API - Active (0.95s response time)
NASA Open APIs - APOD - Active (1.44s response time)
EONET (Natural Events) - Active (14.35s response time)
Earthdata Search - Active (1.95s response time)
Inactive APIs (5/12):
NASA Open APIs - EPIC - HTTP 503 error
NASA Open APIs - Earth - Timeout
SEDAC Main Website - Timeout
SEDAC GPW v4 Service Info - Timeout
SEDAC Data Catalog - Timeout

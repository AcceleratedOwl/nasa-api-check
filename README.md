<<<<<<< HEAD
# NASA API Tester

A Python script to test the availability and response times of various NASA APIs for the 2025 NASA Space Apps Challenge project "Data Pathways to Healthy Cities and Human Settlements".

## Features

- Tests 9 different NASA APIs
- Colored terminal output (green for success, red for failure)
- Response time tracking
- Graceful error handling
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
- Display real-time results with colored output
- Show response times for each API
- Print a summary of active vs inactive APIs
- Save detailed results to `nasa_api_status.json`

## Notes

- Uses NASA's public DEMO_KEY for api.nasa.gov endpoints
- DEMO_KEY has rate limits but is suitable for testing
- All requests have a 10-second timeout
- Results include timestamps and detailed error information
=======
# nasa-api-check
>>>>>>> a283469d07509b7618ff90fd7ce2a7f9c15cb8ad

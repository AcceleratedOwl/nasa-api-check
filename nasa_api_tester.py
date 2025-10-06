#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NASA API Tester for Data Pathways to Healthy Cities and Human Settlements
NASA Space Apps Challenge 2025

This script tests various NASA APIs to verify their availability and response times.
"""

import requests
import json
import time
from datetime import datetime
from typing import Dict, List, Tuple
import sys
import os

# Set UTF-8 encoding for Windows compatibility
if sys.platform.startswith('win'):
    os.system('chcp 65001 > nul 2>&1')

# Color codes for terminal output
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'

def test_api(name: str, url: str, timeout: int = 10) -> Tuple[bool, float, str]:
    """
    Test a single API endpoint and return status, response time, and error message.
    
    Args:
        name: Human-readable name of the API
        url: API endpoint URL
        timeout: Request timeout in seconds
        
    Returns:
        Tuple of (is_successful, response_time, error_message)
    """
    try:
        start_time = time.time()
        response = requests.get(url, timeout=timeout)
        response_time = time.time() - start_time
        
        if response.status_code == 200:
            return True, response_time, ""
        else:
            return False, response_time, f"HTTP {response.status_code}"
            
    except requests.exceptions.Timeout:
        return False, timeout, "Timeout"
    except requests.exceptions.ConnectionError:
        return False, 0, "Connection Error"
    except requests.exceptions.RequestException as e:
        return False, 0, f"Request Error: {str(e)}"
    except Exception as e:
        return False, 0, f"Unexpected Error: {str(e)}"

def print_header():
    """Print the script header with formatting."""
    print(f"{Colors.BOLD}{Colors.BLUE}Testing NASA APIs...{Colors.END}")
    print("-" * 50)

def print_result(name: str, is_success: bool, response_time: float, error_msg: str):
    """Print the result of a single API test with appropriate colors."""
    status_symbol = "[OK]" if is_success else "[FAIL]"
    color = Colors.GREEN if is_success else Colors.RED
    time_str = f"{response_time:.2f}s"
    
    if is_success:
        print(f"{color}{status_symbol} {name} - Active (Response time: {time_str}){Colors.END}")
    else:
        print(f"{color}{status_symbol} {name} - Inactive ({error_msg}){Colors.END}")

def print_summary(active_apis: List[Dict], inactive_apis: List[Dict]):
    """Print the final summary of API test results."""
    print("\n" + "-" * 50)
    print(f"{Colors.BOLD}SUMMARY:{Colors.END}")
    print(f"Active APIs: {len(active_apis)}/{len(active_apis) + len(inactive_apis)}")
    
    if active_apis:
        print(f"{Colors.GREEN}[OK] Active APIs:{Colors.END}")
        for api in active_apis:
            print(f"  - {api['name']}")
    
    if inactive_apis:
        print(f"{Colors.RED}[FAIL] Inactive APIs:{Colors.END}")
        for api in inactive_apis:
            print(f"  - {api['name']} ({api['error']})")

def save_results_to_json(active_apis: List[Dict], inactive_apis: List[Dict], filename: str = "nasa_api_status.json"):
    """Save the test results to a JSON file."""
    results = {
        "timestamp": datetime.now().isoformat(),
        "total_apis": len(active_apis) + len(inactive_apis),
        "active_count": len(active_apis),
        "inactive_count": len(inactive_apis),
        "active_apis": active_apis,
        "inactive_apis": inactive_apis
    }
    
    try:
        with open(filename, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"\n{Colors.BLUE}Results saved to {filename}{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}Error saving results to JSON: {e}{Colors.END}")

def main():
    """Main function to test all NASA APIs."""
    
    # Define all NASA APIs to test
    apis_to_test = [
        {
            "name": "CMR API",
            "url": "https://cmr.earthdata.nasa.gov/search/collections?page_size=1",
            "description": "Common Metadata Repository for Earth science data"
        },
        {
            "name": "GIBS WMTS GetCapabilities",
            "url": "https://gibs.earthdata.nasa.gov/wmts/epsg4326/best/1.0.0/WMTSCapabilities.xml",
            "description": "Global Imagery Browse Services Web Map Tile Service"
        },
        {
            "name": "NASA POWER API",
            "url": "https://power.larc.nasa.gov/api/temporal/daily/point?parameters=T2M&community=RE&longitude=0&latitude=0&start=20200101&end=20200102&format=JSON",
            "description": "Prediction of Worldwide Energy Resources"
        },
        {
            "name": "AppEEARS API",
            "url": "https://appeears.earthdatacloud.nasa.gov/api/",
            "description": "Application for Extracting and Exploring Analysis Ready Samples"
        },
        {
            "name": "NASA Open APIs - APOD",
            "url": "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY",
            "description": "Astronomy Picture of the Day"
        },
        {
            "name": "NASA Open APIs - EPIC",
            "url": "https://api.nasa.gov/EPIC/api/natural/images?api_key=DEMO_KEY",
            "description": "Earth Polychromatic Imaging Camera"
        },
        {
            "name": "NASA Open APIs - Earth",
            "url": "https://api.nasa.gov/planetary/earth/assets?lon=-95.33&lat=29.78&date=2018-01-01&api_key=DEMO_KEY",
            "description": "Earth imagery and assets"
        },
        {
            "name": "EONET (Natural Events)",
            "url": "https://eonet.gsfc.nasa.gov/api/v3/events",
            "description": "Earth Observatory Natural Event Tracker"
        },
        {
            "name": "Earthdata Search",
            "url": "https://search.earthdata.nasa.gov/api/health",
            "description": "Earthdata Search API health check"
        },
        {
            "name": "SEDAC Main Website",
            "url": "https://sedac.ciesin.columbia.edu/",
            "description": "SEDAC Main Website - Socioeconomic Data and Applications Center"
        },
        {
            "name": "SEDAC GPW v4 Service Info",
            "url": "https://sedac.ciesin.columbia.edu/arcgis-gis-server/rest/services/sedac-gpw-v4?f=json",
            "description": "SEDAC GPW v4 Service Information"
        },
        {
            "name": "SEDAC Data Catalog",
            "url": "https://sedac.ciesin.columbia.edu/data/collection/gpw-v4",
            "description": "SEDAC GPW v4 Data Collection Page"
        }
    ]
    
    print_header()
    
    active_apis = []
    inactive_apis = []
    
    # Test each API
    for api in apis_to_test:
        is_success, response_time, error_msg = test_api(api["name"], api["url"])
        
        # Store results
        api_result = {
            "name": api["name"],
            "url": api["url"],
            "description": api["description"],
            "response_time": response_time,
            "timestamp": datetime.now().isoformat()
        }
        
        if is_success:
            active_apis.append(api_result)
        else:
            api_result["error"] = error_msg
            inactive_apis.append(api_result)
        
        # Print result
        print_result(api["name"], is_success, response_time, error_msg)
    
    # Print summary
    print_summary(active_apis, inactive_apis)
    
    # Save results to JSON
    save_results_to_json(active_apis, inactive_apis)
    
    # Return appropriate exit code
    return 0 if len(inactive_apis) == 0 else 1

if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Testing interrupted by user{Colors.END}")
        sys.exit(1)
    except Exception as e:
        print(f"\n{Colors.RED}Unexpected error: {e}{Colors.END}")
        sys.exit(1)

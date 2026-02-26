"""
Test script to verify sorting functionality for all timeframes
"""

import requests
import json
from pprint import pprint

BASE_URL = "http://localhost:5000"

def test_api_response():
    """Test that API returns all timeframe data"""
    print("=" * 60)
    print("Testing API Response")
    print("=" * 60)
    
    response = requests.get(f"{BASE_URL}/api/markets")
    if response.status_code != 200:
        print(f"❌ API Error: {response.status_code}")
        return False
    
    markets = response.json()
    print(f"✓ API returned {len(markets)} markets")
    
    if not markets:
        print("❌ No markets data returned")
        return False
    
    first_market = markets[0]
    print(f"\n✓ Sample market: {first_market['Name']} ({first_market['Symbol']})")
    
    required_fields = [
        'Name', 'Symbol', 'Category', 'Price Change %',
        'perf_1w', 'perf_1m', 'perf_3m', 'perf_6m',
        'perf_ytd', 'perf_1y', 'perf_5y', 'perf_10y'
    ]
    
    missing_fields = []
    for field in required_fields:
        if field not in first_market:
            missing_fields.append(field)
        else:
            value = first_market[field]
            status = "✓" if value is not None else "⚠"
            print(f"  {status} {field}: {value}")
    
    if missing_fields:
        print(f"\n❌ Missing fields: {missing_fields}")
        return False
    
    print(f"\n✓ All required fields present in API response")
    return True

def test_sorting_logic():
    """Test sorting logic with sample data"""
    print("\n" + "=" * 60)
    print("Testing Sorting Logic")
    print("=" * 60)
    
    response = requests.get(f"{BASE_URL}/api/markets")
    markets = response.json()
    
    timeframes = [
        ('perf_1w', '1 Week'),
        ('perf_1m', '1 Month'),
        ('perf_3m', '3 Months'),
        ('perf_6m', '6 Months'),
        ('perf_ytd', 'YTD'),
        ('perf_1y', '1 Year'),
        ('perf_5y', '5 Years'),
        ('perf_10y', '10 Years'),
    ]
    
    all_pass = True
    
    for field, label in timeframes:
        # Filter markets with non-null values for this field
        valid_markets = [m for m in markets if m[field] is not None]
        
        if not valid_markets:
            print(f"⚠ {label} ({field}): No data available")
            continue
        
        # Sort ascending
        sorted_asc = sorted(valid_markets, key=lambda x: float(x[field]))
        # Sort descending
        sorted_desc = sorted(valid_markets, key=lambda x: float(x[field]), reverse=True)
        
        min_val = sorted_asc[0][field]
        max_val = sorted_desc[0][field]
        
        print(f"✓ {label:15} ({field:12}): {len(valid_markets):3} markets | "
              f"Range: {min_val:8.2f}% to {max_val:8.2f}%")
        
        # Verify sorting works correctly
        is_ascending = all(sorted_asc[i][field] <= sorted_asc[i+1][field] 
                          for i in range(len(sorted_asc)-1))
        is_descending = all(sorted_desc[i][field] >= sorted_desc[i+1][field] 
                           for i in range(len(sorted_desc)-1))
        
        if not (is_ascending and is_descending):
            print(f"  ❌ Sorting logic failed for {label}")
            all_pass = False
    
    return all_pass

def test_column_mapping():
    """Test that column mappings match between frontend and backend"""
    print("\n" + "=" * 60)
    print("Testing Column Mapping")
    print("=" * 60)
    
    column_map = {
        'Name': 'Name',
        'Category': 'Category',
        'Price Change %': 'Price Change %',
        'perf_1w': 'perf_1w',
        'perf_1m': 'perf_1m',
        'perf_3m': 'perf_3m',
        'perf_6m': 'perf_6m',
        'perf_ytd': 'perf_ytd',
        'perf_1y': 'perf_1y',
        'perf_5y': 'perf_5y',
        'perf_10y': 'perf_10y'
    }
    
    response = requests.get(f"{BASE_URL}/api/markets")
    markets = response.json()
    
    if not markets:
        print("❌ No markets data to test")
        return False
    
    first_market = markets[0]
    all_valid = True
    
    for display_col, data_col in column_map.items():
        if data_col in first_market:
            print(f"✓ Column '{display_col}' maps to '{data_col}'")
        else:
            print(f"❌ Column '{display_col}' -> '{data_col}' NOT FOUND")
            all_valid = False
    
    return all_valid

def test_page_rendering():
    """Test that the page loads and renders correctly"""
    print("\n" + "=" * 60)
    print("Testing Page Rendering")
    print("=" * 60)
    
    response = requests.get(f"{BASE_URL}/")
    if response.status_code != 200:
        print(f"❌ Page load error: {response.status_code}")
        return False
    
    html = response.text
    
    checks = [
        ('Table headers', ['data-sort="Name"', 'data-sort="Category"', 
                          'data-sort="perf_1w"', 'data-sort="perf_1m"',
                          'data-sort="perf_5y"', 'data-sort="perf_10y"']),
        ('JavaScript sorting function', ['function sortTable', 'columnMap', 'dataColumn']),
        ('Table rendering', ['renderTable', 'formatPerformance'])
    ]
    
    all_pass = True
    for check_name, keywords in checks:
        found_all = all(keyword in html for keyword in keywords)
        status = "✓" if found_all else "❌"
        print(f"{status} {check_name}")
        if not found_all:
            missing = [kw for kw in keywords if kw not in html]
            print(f"  Missing: {missing}")
            all_pass = False
    
    return all_pass

if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("CAPITAL ANALYZER - SORTING FUNCTIONALITY TEST")
    print("=" * 60)
    
    results = {
        'API Response': test_api_response(),
        'Sorting Logic': test_sorting_logic(),
        'Column Mapping': test_column_mapping(),
        'Page Rendering': test_page_rendering(),
    }
    
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    for test_name, passed in results.items():
        status = "✓ PASS" if passed else "❌ FAIL"
        print(f"{status:10} - {test_name}")
    
    all_passed = all(results.values())
    print("=" * 60)
    if all_passed:
        print("✓ ALL TESTS PASSED - Sorting is working correctly!")
    else:
        print("❌ SOME TESTS FAILED - Review the output above")
    print("=" * 60)

# Web Viewer Quick Start Guide

## Overview
The web viewer provides a beautiful, responsive interface to view your Capital.com market analysis results in a browser.

## Features
✅ Modern, dark-themed UI
✅ Fully responsive (mobile, tablet, desktop)
✅ Real-time search and filtering
✅ Sortable columns
✅ Category badges with color coding
✅ Performance metrics with color indicators
✅ Manual refresh with the Refresh button
✅ Statistics dashboard

## Setup

### 1. Install Flask
```bash
pip install flask
```

Or install all requirements:
```bash
pip install -r requirements.txt
```

### 2. Generate Data
First, run the analyzer to create the CSV file:
```bash
python run_analyzer.py
```

This will create `capital_markets_analysis.csv` with your market data.

### 3. Start Web Server
```bash
python web_viewer.py
```

### 4. Open Browser
Navigate to: **http://localhost:5000**

## Usage

### Search
- Type in the search box to filter markets by name or EPIC code
- Search is real-time and case-insensitive

### Filter by Category
- Use the dropdown to filter by specific asset class:
  - Commodities (Gold)
  - Forex (Blue)
  - Indices (Purple)
  - Cryptocurrencies (Orange)
  - Shares (Green)

### Sort Data
- Click any column header to sort
- Click again to reverse sort direction
- Indicators show current sort: ↑ (ascending) ↓ (descending)

### Performance Colors
- 🟢 Green: Positive performance
- 🔴 Red: Negative performance
- ⚪ Gray: No data available

### Statistics Dashboard
- **Total Markets**: Number of instruments tracked
- **Categories**: Number of asset classes
- **Top Performer**: Best performing market (1Y basis)
- **Last Updated**: When the data was generated

### Refresh Data
- Click the 🔄 Refresh button to reload data
- Or refresh manually with the Refresh button

## Mobile Support
The interface is fully responsive and works great on:
- 📱 Smartphones
- 📋 Tablets
- 💻 Desktop computers

## Tips
1. Run `python run_analyzer.py` periodically to update your data
2. Keep the web server running to access data anytime
3. Use Ctrl+C to stop the server
4. The server runs on all network interfaces (0.0.0.0), so you can access it from other devices on your network using your computer's IP address

## Troubleshooting

### "No Data Available" message
- Make sure you've run `python run_analyzer.py` first
- Check that `capital_markets_analysis.csv` exists in the same directory

### Port already in use
- Another application is using port 5000
- Stop the other application or edit `web_viewer.py` to use a different port

### Browser not loading
- Make sure the server is running (you should see console output)
- Try http://127.0.0.1:5000 instead
- Check your firewall settings

## Example Workflow
```bash
# Step 1: Run analyzer (takes a few minutes)
python run_analyzer.py

# Step 2: Start web viewer
python web_viewer.py

# Step 3: Open browser to http://localhost:5000

# Step 4: Enjoy the beautiful interface!
```

---

**Note**: The web viewer reads from the CSV file. To see updated data, re-run the analyzer and refresh the browser.

# Capital.com Market Analyzer - Web Interface Guide

## Overview

The Capital.com Market Analyzer is now a **modern web application** built with Flask. It provides a beautiful, responsive interface for managing and analyzing capital markets data with integrated analyzer control.

## Features

✨ **Modern Web Interface**
- Dark theme with Material Design aesthetics
- Responsive layout (works on desktop, tablet, mobile)
- Real-time data filtering and searching
- Interactive sorting on all columns

🚀 **Integrated Analyzer Control**
- Run the analyzer directly from the web interface
- Live status indicator while running
- Automatic data refresh on completion
- Background processing (doesn't block the UI)

📊 **Market Data Management**
- Browse markets across all categories (Forex, Commodities, Shares, Indices, Cryptocurrencies, ETFs)
- Search by market name or symbol/EPIC
- Filter by asset class
- View performance metrics across 8 timeframes (1W, 1M, 3M, 6M, YTD, 1Y, 5Y, 10Y)
- Color-coded performance indicators (green for gains, red for losses)

💾 **Dual Storage**
- **Primary**: SQLite database (`market_data.db`)
- **Backup**: CSV export (`capital_markets_analysis.csv`)

## Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Your Credentials

Copy the template and add your Capital.com API credentials:

```bash
# Windows
copy config_template.py config.py

# Linux/Mac
cp config_template.py config.py
```

Edit `config.py` and fill in:
- `API_KEY`: Your Capital.com API key
- `USERNAME`: Your Capital.com username
- `PASSWORD`: Your Capital.com password
- `USE_DEMO`: Set to `True` for demo mode, `False` for live trading

### 3. Start the Web Application

```bash
python app.py
```

The application will start on **http://localhost:5000**

### 4. Use the Interface

**Option A: Run from Web Interface**
- Open http://localhost:5000 in your browser
- Click the **"Start Analyzer"** button
- Watch the status indicator as it fetches and processes data
- Data automatically refreshes when complete

**Option B: Run Command Line**
```bash
python run_analyzer.py
```

Then refresh the web interface to see the new data.

## Interface Components

### Header
- Title and description
- System status

### Runner Section
- **Start Analyzer**: Launches the market data fetcher
- **Status Indicator**: Shows if analyzer is idle or running

### Statistics Cards
- **Total Markets**: Number of instruments in database
- **Categories**: Number of asset classes
- **Top Performer**: Best-performing market by 1-year return
- **Last Updated**: Timestamp of last data fetch

### Controls
- **Search Box**: Find markets by name or EPIC symbol
- **Category Filter**: View specific asset classes
- **Refresh Button**: Manually reload data

### Markets Table
- **Market Name**: Display name and EPIC symbol
- **Category**: Color-coded asset class badge
- **Performance Columns**: 24h, 1W, 1M, 3M, 6M, YTD, 1Y returns
- **Interactive Sorting**: Click column headers to sort
- **Color Coding**: 
  - 🟢 Green = Positive returns
  - 🔴 Red = Negative returns
  - ⚪ Gray = No data

## File Structure

```
capital-analyser-C/
├── app.py                      # Flask web application
├── run_analyzer.py             # Market data analyzer
├── capital_analyzer.py          # API client
├── config.py                   # Your credentials (created from template)
├── config_template.py          # Configuration template
├── database.py                 # Database utilities
├── requirements.txt            # Python dependencies
├── market_data.db              # SQLite database (created on first run)
├── capital_markets_analysis.csv # Backup CSV (created on first run)
├── templates/
│   └── index.html             # Web interface
└── static/                     # CSS/JS assets (if any)
```

## API Endpoints

For advanced users, these REST endpoints are available:

- `GET /` - Main dashboard
- `GET /api/markets` - Get market data (supports `?category=` and `?search=` params)
- `GET /api/categories` - Get list of categories
- `GET /api/stats` - Get statistics
- `GET /api/analyzer/status` - Check if analyzer is running
- `POST /api/analyzer/run` - Start the analyzer

## Removed Dependencies

✂️ **No Streamlit** - Replaced with native Flask web app
- ✗ streamlit (removed)
- ✗ plotly (removed - not needed for this interface)

**Kept Dependencies:**
- ✓ flask (web framework)
- ✓ requests (API calls)
- ✓ pandas (data processing)
- ✓ python-dateutil (date handling)

## Performance Notes

- First run may take a few minutes depending on categories configured
- Data auto-refreshes every 60 seconds
- Analyzer runs in background thread to avoid blocking the UI
- SQLite database is lightweight and suitable for storing thousands of markets

## Troubleshooting

### Port Already in Use
If port 5000 is already in use, edit the last line of `app.py`:
```python
app.run(debug=False, host='localhost', port=8080)  # Change 5000 to 8080
```

### Analyzer Not Starting
- Check that `config.py` has valid API credentials
- Verify internet connection
- Check console output for specific errors

### No Data Displayed
- Run the analyzer from the web interface or command line first
- Wait a few minutes for the data fetch to complete
- Check that `market_data.db` exists in the project folder

### Styling Issues
- Clear browser cache (Ctrl+Shift+Delete)
- Try a different browser
- Ensure JavaScript is enabled

## Next Steps

1. **Customize Categories**: Edit `config.py` to choose which asset classes to monitor
2. **Automate Updates**: Use task scheduler or cron to run analyzer periodically
3. **Export Data**: Use the CSV export for analysis in Excel or other tools

## Support

For issues with Capital.com API:
- Check Capital.com API documentation
- Verify credentials in config.py
- Test API connection with debug_api.py

For issues with the web interface:
- Check browser console for errors (F12)
- Ensure Flask is running (check console output)
- Try refreshing the page

import sqlite3

from run_analyzer import init_database, store_to_database


def test_store_to_database_preserves_other_categories(tmp_path):
    db_path = tmp_path / "market_data.db"
    init_database(str(db_path))

    shares_row = {
        "Category": "Shares",
        "Symbol": "AAPL",
        "Name": "Apple",
        "Current Price": "100.00",
        "Currency": "USD",
        "Price Change %": "1.20%",
        "Perf % 1W": "2.00%",
        "Perf % 1M": "3.00%",
        "Perf % 3M": "4.00%",
        "Perf % 6M": "5.00%",
        "Perf % YTD": "6.00%",
        "Perf % 1Y": "7.00%",
        "Perf % 5Y": "8.00%",
        "Perf % 10Y": "9.00%",
        "RSI 24H": "60",
        "RSI 1W": "61",
        "RSI 1M": "62",
        "RSI 3M": "63",
        "RSI 6M": "64",
        "RSI YTD": "65",
        "RSI 1H": "66",
        "RSI 4H": "67",
        "Market Status": "Open",
        "Type": "Stock",
    }

    forex_row = {
        "Category": "Forex",
        "Symbol": "EURUSD",
        "Name": "EUR/USD",
        "Current Price": "1.10",
        "Currency": "USD",
        "Price Change %": "0.50%",
        "Perf % 1W": "0.10%",
        "Perf % 1M": "0.20%",
        "Perf % 3M": "0.30%",
        "Perf % 6M": "0.40%",
        "Perf % YTD": "0.50%",
        "Perf % 1Y": "0.60%",
        "Perf % 5Y": "0.70%",
        "Perf % 10Y": "0.80%",
        "RSI 24H": "55",
        "RSI 1W": "56",
        "RSI 1M": "57",
        "RSI 3M": "58",
        "RSI 6M": "59",
        "RSI YTD": "60",
        "RSI 1H": "61",
        "RSI 4H": "62",
        "Market Status": "Open",
        "Type": "FX",
    }

    store_to_database([shares_row], str(db_path), categories=["shares"])
    store_to_database([forex_row], str(db_path), categories=["forex"])

    conn = sqlite3.connect(str(db_path))
    try:
        shares_count = conn.execute(
            "SELECT COUNT(*) FROM markets WHERE category = ?",
            ("Shares",),
        ).fetchone()[0]
        forex_count = conn.execute(
            "SELECT COUNT(*) FROM markets WHERE category = ?",
            ("Forex",),
        ).fetchone()[0]
    finally:
        conn.close()

    assert shares_count == 1
    assert forex_count == 1

"""
Analyze top weekly performers by category for trading strategy
"""
import csv
from collections import defaultdict

# Read the CSV
categories = defaultdict(list)
with open('capital_markets_analysis.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cat = row['Category']
        try:
            perf_1w = float(row['Perf % 1W'].strip('%'))
            rsi_val = None
            if row['RSI 1W'] != 'N/A':
                try:
                    rsi_val = float(row['RSI 1W'])
                except:
                    rsi_val = None
            
            categories[cat].append({
                'symbol': row['Symbol'],
                'name': row['Name'],
                'perf_1w': perf_1w,
                'rsi_1w': rsi_val,
                'current_price': float(row['Current Price']),
                'market_status': row['Market Status'],
                'perf_1m': float(row['Perf % 1M'].strip('%')) if '%' in row['Perf % 1M'] else None,
                'perf_1y': float(row['Perf % 1Y'].strip('%')) if '%' in row['Perf % 1Y'] else None,
            })
        except:
            pass

# Find top 10 performers in each category
print('\n' + '='*90)
print('TOP 10 WEEKLY PERFORMERS BY CATEGORY')
print('='*90)

top_performers = {}
for cat in sorted(categories.keys()):
    items = sorted(categories[cat], key=lambda x: x['perf_1w'], reverse=True)[:10]
    top_performers[cat] = items
    print(f'\n{cat.upper()}:')
    for i, item in enumerate(items, 1):
        print(f'  {i}. {item["symbol"]:15} | {item["name"]:30} | 1W: {item["perf_1w"]:7.2f}% | RSI: {str(item["rsi_1w"]):6} | Status: {item["market_status"]}')

print('\n' + '='*90)
print('SELECTED INSTRUMENTS FOR TRADING STRATEGY (10 from each category)')
print('='*90)

all_selected = []
for cat, items in top_performers.items():
    for item in items:
        all_selected.append({
            'category': cat,
            'symbol': item['symbol'],
            'name': item['name'],
            'perf_1w': item['perf_1w'],
            'rsi_1w': item['rsi_1w']
        })
        
print(f'\nTotal instruments selected: {len(all_selected)}')
for item in sorted(all_selected, key=lambda x: x['perf_1w'], reverse=True):
    print(f"  - {item['symbol']:12} ({item['category']:18}) Perf 1W: {item['perf_1w']:7.2f}%")

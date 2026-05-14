"""
Trading Strategy Trade Logger & Performance Tracker
Helps track your 51%+ win rate strategy results
"""

import csv
import os
from datetime import datetime
from pathlib import Path

class TradeLogger:
    """Log and track trades from the 51%+ win rate momentum strategy"""
    
    def __init__(self, log_file='trades.csv'):
        self.log_file = log_file
        self.trades = []
        self._load_trades()
    
    def _load_trades(self):
        """Load existing trades from CSV"""
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r') as f:
                reader = csv.DictReader(f)
                self.trades = list(reader) if reader is not None else []
    
    def log_trade(self, symbol, entry_price, entry_time, position_size, stop_loss, target_1, target_2):
        """Log a new trade entry"""
        trade = {
            'trade_id': len(self.trades) + 1,
            'date': datetime.now().strftime('%Y-%m-%d'),
            'symbol': symbol,
            'entry_price': entry_price,
            'entry_time': entry_time,
            'position_size': position_size,
            'stop_loss': stop_loss,
            'target_1': target_1,
            'target_2': target_2,
            'exit_price': '',
            'exit_time': '',
            'profit_loss': '',
            'profit_loss_percent': '',
            'status': 'OPEN',
            'notes': ''
        }
        self.trades.append(trade)
        self._save_trades()
        print(f"✓ Trade #{trade['trade_id']} logged: {symbol} @ {entry_price}")
        return trade['trade_id']
    
    def close_trade(self, trade_id, exit_price, exit_time, notes=''):
        """Close a trade and calculate P&L"""
        if trade_id > len(self.trades):
            print("❌ Invalid trade ID")
            return None
        
        trade = self.trades[trade_id - 1]
        entry = float(trade['entry_price'])
        size = float(trade['position_size'])
        
        profit_loss = (float(exit_price) - entry) * size / entry if entry != 0 else 0
        profit_loss_percent = ((float(exit_price) - entry) / entry) * 100 if entry != 0 else 0
        
        trade['exit_price'] = exit_price
        trade['exit_time'] = exit_time
        trade['profit_loss'] = f"${profit_loss:.2f}"
        trade['profit_loss_percent'] = f"{profit_loss_percent:.2f}%"
        trade['status'] = 'CLOSED'
        trade['notes'] = notes
        
        self._save_trades()
        status = "WIN ✓" if profit_loss_percent > 0 else "LOSS ✗"
        print(f"✓ Trade #{trade_id} closed: {status} {profit_loss_percent:+.2f}%")
        return trade
    
    def _save_trades(self):
        """Save trades to CSV"""
        if not self.trades:
            return
        
        keys = self.trades[0].keys()
        with open(self.log_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(self.trades)
    
    def get_performance_stats(self):
        """Calculate and return performance statistics"""
        closed_trades = [t for t in self.trades if t['status'] == 'CLOSED']
        
        if not closed_trades:
            return None
        
        wins = 0
        losses = 0
        total_profit = 0
        
        for trade in closed_trades:
            try:
                pnl_str = trade['profit_loss_percent'].strip('%')
                pnl = float(pnl_str)
                total_profit += pnl
                
                if pnl > 0:
                    wins += 1
                else:
                    losses += 1
            except:
                pass
        
        total_trades = wins + losses
        win_rate = (wins / total_trades * 100) if total_trades > 0 else 0
        avg_profit = total_profit / total_trades if total_trades > 0 else 0
        
        return {
            'total_trades': total_trades,
            'wins': wins,
            'losses': losses,
            'win_rate': win_rate,
            'total_profit_percent': total_profit,
            'avg_profit_percent': avg_profit
        }
    
    def print_summary(self):
        """Print performance summary"""
        stats = self.get_performance_stats()
        
        if not stats:
            print("No closed trades yet. Start trading!")
            return
        
        print("\n" + "="*70)
        print("TRADING PERFORMANCE SUMMARY")
        print("="*70)
        print(f"Total Trades: {stats['total_trades']}")
        print(f"Wins: {stats['wins']} ({stats['win_rate']:.1f}%)")
        print(f"Losses: {stats['losses']} ({100-stats['win_rate']:.1f}%)")
        print(f"Total Profit/Loss: {stats['total_profit_percent']:+.2f}%")
        print(f"Average Per Trade: {stats['avg_profit_percent']:+.2f}%")
        
        target_met = "✓ TARGET MET" if stats['win_rate'] >= 51 else "✗ Target not met yet"
        print(f"\n51% Win Rate Target: {target_met}")
        print("="*70 + "\n")
    
    def print_recent_trades(self, count=5):
        """Print recent trades"""
        closed = [t for t in self.trades if t['status'] == 'CLOSED']
        recent = closed[-count:]
        
        print("\n" + "="*100)
        print("RECENT TRADES")
        print("="*100)
        print(f"{'ID':<4} {'Symbol':<10} {'Entry':<10} {'Exit':<10} {'P&L':<12} {'Status':<8}")
        print("-"*100)
        
        for trade in recent:
            status = "WIN ✓" if float(trade['profit_loss_percent'].strip('%')) > 0 else "LOSS ✗"
            print(f"{trade['trade_id']:<4} {trade['symbol']:<10} ${trade['entry_price']:<9} ${trade['exit_price']:<9} {trade['profit_loss_percent']:<12} {status:<8}")
        
        print("="*100 + "\n")


def interactive_trade_logger():
    """Interactive trade logging interface"""
    logger = TradeLogger()
    
    print("\n" + "="*70)
    print("TRADING STRATEGY - INTERACTIVE TRADE LOGGER")
    print("="*70)
    print("Commands:")
    print("  'new'    - Log a new trade entry")
    print("  'close'  - Close an open trade")
    print("  'view'   - View recent trades")
    print("  'stats'  - View performance statistics")
    print("  'list'   - List all trades")
    print("  'quit'   - Exit")
    print("="*70 + "\n")
    
    while True:
        cmd = input("Enter command: ").strip().lower()
        
        if cmd == 'quit':
            print("Goodbye!")
            break
        
        elif cmd == 'new':
            symbol = input("Symbol (e.g., OSMOUSD): ").strip().upper()
            entry_price = input("Entry Price: ").strip()
            entry_time = input("Entry Time (HH:MM GMT): ").strip()
            position_size = input("Position Size ($): ").strip()
            stop_loss = input("Stop Loss Price: ").strip()
            target_1 = input("Target 1 Price (+2%): ").strip()
            target_2 = input("Target 2 Price (+4%): ").strip()
            
            try:
                trade_id = logger.log_trade(symbol, entry_price, entry_time, position_size, stop_loss, target_1, target_2)
            except Exception as e:
                print(f"❌ Error logging trade: {e}")
        
        elif cmd == 'close':
            trade_id = int(input("Trade ID to close: ").strip())
            exit_price = input("Exit Price: ").strip()
            exit_time = input("Exit Time (HH:MM GMT): ").strip()
            notes = input("Notes (optional): ").strip()
            
            try:
                logger.close_trade(trade_id, exit_price, exit_time, notes)
            except Exception as e:
                print(f"❌ Error closing trade: {e}")
        
        elif cmd == 'view':
            logger.print_recent_trades(5)
        
        elif cmd == 'stats':
            logger.print_summary()
        
        elif cmd == 'list':
            print("\nAll Trades:")
            print(f"{'ID':<4} {'Symbol':<10} {'Date':<12} {'Status':<8} {'P&L':<12}")
            print("-"*50)
            for trade in logger.trades:
                pnl = trade['profit_loss_percent'] if trade['status'] == 'CLOSED' else 'OPEN'
                print(f"{trade['trade_id']:<4} {trade['symbol']:<10} {trade['date']:<12} {trade['status']:<8} {pnl:<12}")
        
        else:
            print("Unknown command. Try 'new', 'close', 'view', 'stats', 'list', or 'quit'")
        
        print()


if __name__ == '__main__':
    # Uncomment one of these to use:
    
    # Option 1: Interactive mode (recommended for daily use)
    interactive_trade_logger()
    
    # Option 2: One-time logging (for scripting)
    # logger = TradeLogger()
    # logger.log_trade('OSMOUSD', '10.50', '10:30 GMT', 10000, 10.29, 10.71, 10.92)
    # logger.close_trade(1, '10.81', '14:15 GMT', 'Closed at target 2')
    # logger.print_summary()

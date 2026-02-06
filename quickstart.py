#!/usr/bin/env python3
"""
Capital.com Market Analyzer - Quick Start
This script helps set up and run the application
"""

import os
import sys
import subprocess

def check_requirements():
    """Check if all requirements are installed"""
    try:
        import flask
        import requests
        import pandas
        import dateutil
        print("✓ All dependencies installed")
        return True
    except ImportError as e:
        print(f"✗ Missing dependency: {e}")
        print("\nInstall dependencies with:")
        print("  pip install -r requirements.txt")
        return False

def check_config():
    """Check if config.py exists"""
    if os.path.exists('config.py'):
        print("✓ config.py found")
        return True
    else:
        print("✗ config.py not found")
        print("\nCreate it with:")
        print("  copy config_template.py config.py")
        print("\nThen edit config.py with your Capital.com API credentials")
        return False

def check_database():
    """Check if database exists"""
    if os.path.exists('market_data.db'):
        print("✓ market_data.db found")
        return True
    else:
        print("⚠ market_data.db not found (will be created on first run)")
        return True

def main():
    """Main setup check"""
    print("\n" + "="*60)
    print("Capital.com Market Analyzer - Setup Check")
    print("="*60 + "\n")
    
    checks = [
        ("Dependencies", check_requirements),
        ("Configuration", check_config),
        ("Database", check_database),
    ]
    
    all_ok = True
    for name, check in checks:
        print(f"\n{name}:")
        if not check():
            all_ok = False
    
    print("\n" + "="*60)
    if all_ok or all_ok == None:
        print("✓ Setup complete! Ready to run.")
        print("\nStart the application with:")
        print("  python app.py")
        print("\nThen open http://localhost:5000 in your browser")
    else:
        print("⚠ Please complete the setup above")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()

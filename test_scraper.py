import sys, os
sys.path.append(os.path.abspath("scripts"))
from scripts.yahoo_scraper import fetch_yahoo_headlines

# Pick a recent date where news is definitely available
symbol = "TSLA"
test_date = "2022-01-27"  # Example date around earnings

headlines = fetch_yahoo_headlines(symbol, test_date)

print(f"Headlines for {symbol} on {test_date}:")
for h in headlines:
    print("-", h)

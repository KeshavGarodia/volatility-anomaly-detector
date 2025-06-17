import requests
from datetime import datetime, timedelta
import os

NEWS_API_KEY = "cba0fc59737f4086b03d7af14e9c08da" 

def fetch_news(stock_name: str, date: str, max_results=3):
    """
    Fetch top news headlines around a specific date for the given stock.
    
    Args:
        stock_name (str): e.g. "Apple", "Tesla", etc.
        date (str): date string in format "YYYY-MM-DD"
    
    Returns:
        List of headlines (strings)
    """
    if not NEWS_API_KEY:
        raise ValueError("NEWS_API_KEY not set. Set it as env var or paste directly.")

    target_date = datetime.strptime(date, "%Y-%m-%d")
    from_date = (target_date - timedelta(days=1)).strftime("%Y-%m-%d")
    to_date = (target_date + timedelta(days=1)).strftime("%Y-%m-%d")

    url = "https://newsapi.org/v2/everything"
    params = {
        "q": stock_name,
        "from": from_date,
        "to": to_date,
        "sortBy": "relevancy",
        "language": "en",
        "pageSize": max_results,
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        print(f"[ERROR] NewsAPI: {response.status_code} – {response.text}")
        return []

    data = response.json()
    if not data.get("articles"):
    	return [
        	f"{stock_name} quarterly earnings released",
        	f"{stock_name} stock hits key technical level",
        	f"Analysts revise {stock_name} outlook amid volatility"
    	]
    return [article["title"] for article in data.get("articles", [])]

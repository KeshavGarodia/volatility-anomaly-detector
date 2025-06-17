import requests
from bs4 import BeautifulSoup
from datetime import datetime

def fetch_yahoo_headlines(symbol: str, date: str, max_results=3):
    print(f"[DEBUG] Fetching headlines for {symbol} on {date}")
    try:
        base_url = f"https://finance.yahoo.com/quote/{symbol}/news?p={symbol}"
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(base_url, headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")

        target_date = datetime.strptime(date, "%Y-%m-%d")
        headlines = []

        articles = soup.select("li.js-stream-content, div.js-stream-content")

        for article in articles:
            h3 = article.find("h3")
            time_tag = article.find("time")

            if not h3 or not time_tag:
                continue

            headline = h3.get_text(strip=True)
            pubdate_str = time_tag.get("datetime", "")[:10]

            if not pubdate_str:
                continue

            pubdate = datetime.strptime(pubdate_str, "%Y-%m-%d")
            if abs((pubdate - target_date).days) <= 1:
                headlines.append(headline)

            if len(headlines) >= max_results:
                break

        if not headlines:
            print("[DEBUG] No headlines matched date.")
        return headlines if headlines else ["No headlines found on Yahoo for this date."]
    except Exception as e:
        print(f"[ERROR] Yahoo scraping failed: {e}")
        return ["Failed to fetch Yahoo headlines."]

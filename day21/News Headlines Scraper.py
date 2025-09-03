# Day 21 — News Headlines Scraper (Hacker News)
# pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

def fetch_headlines(url="https://news.ycombinator.com", top_n=10):
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
    except Exception as e:
        print(f"❌ Network error: {e}")
        return []

    soup = BeautifulSoup(resp.text, "html.parser")
    links = soup.select("a.titlelink")  # HN selector
    headlines = [a.get_text(strip=True) for a in links[:top_n]]
    return headlines

if __name__ == "__main__":
    print("🗞 Top Hacker News Headlines:")
    headlines = fetch_headlines(top_n=10)
    if not headlines:
        print("No headlines found.")
    for i, h in enumerate(headlines, 1):
        print(f"{i}. {h}")

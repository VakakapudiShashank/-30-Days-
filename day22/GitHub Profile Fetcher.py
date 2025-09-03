# Day 22 — GitHub Profile Fetcher
# pip install requests

import requests

def fetch_github_user(username: str):
    url = f"https://api.github.com/users/{username}"
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 404:
            print("❌ User not found.")
            return
        r.raise_for_status()
        data = r.json()
        print("\n👤 GitHub Profile")
        print(f"Name:           {data.get('name')}")
        print(f"Username:       {data.get('login')}")
        print(f"Bio:            {data.get('bio')}")
        print(f"Public Repos:   {data.get('public_repos')}")
        print(f"Followers:      {data.get('followers')}")
        print(f"Following:      {data.get('following')}")
        print(f"Location:       {data.get('location')}")
        print(f"Created At:     {data.get('created_at')}")
        print(f"Profile URL:    {data.get('html_url')}")
    except Exception as e:
        print(f"⚠ API error: {e}")

if __name__ == "__main__":
    username = input("Enter GitHub username: ").strip()
    if username:
        fetch_github_user(username)

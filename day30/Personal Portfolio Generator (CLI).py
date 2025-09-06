# Day 30 — Final Project: Personal Portfolio Generator
# Generates a static HTML portfolio page and opens it in your browser.

import json
import os
import webbrowser
from pathlib import Path
from datetime import datetime

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{name} — Portfolio</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://cdn.simplecss.org/simple.min.css">
</head>
<body>
<header>
  <h1>{name}</h1>
  <p>{role}</p>
</header>
<main>
  <section>
    <h2>About</h2>
    <p>{about}</p>
  </section>
  <section>
    <h2>Skills</h2>
    <ul>
      {skills_list}
    </ul>
  </section>
  <section>
    <h2>Projects</h2>
    {projects_list}
  </section>
</main>
<footer>
  <p>Generated on {date}. Connect: <a href="{github}" target="_blank">GitHub</a> | <a href="{linkedin}" target="_blank">LinkedIn</a></p>
</footer>
</body>
</html>
"""

def build_html(data):
    skills_list = "\n      ".join(f"<li>{s}</li>" for s in data.get("skills", []))
    projects_list = "\n".join(
        f"""<article>
          <h3>{p.get('title')}</h3>
          <p>{p.get('description')}</p>
          {'<p><a href="'+p.get('link')+'" target="_blank">Live / Repo</a></p>' if p.get('link') else ''}
        </article>"""
        for p in data.get("projects", [])
    )
    html = TEMPLATE.format(
        name=data.get("name", "Your Name"),
        role=data.get("role", "Your Role"),
        about=data.get("about", "Short bio..."),
        skills_list=skills_list,
        projects_list=projects_list,
        date=datetime.now().strftime("%Y-%m-%d"),
        github=data.get("github", "#"),
        linkedin=data.get("linkedin", "#")
    )
    return html

def load_or_prompt(config_file="portfolio.json"):
    if os.path.exists(config_file):
        with open(config_file, "r", encoding="utf-8") as f:
            print(f"✅ Loaded config from {config_file}")
            return json.load(f)
    print("No config found. Let's create one quickly.")
    name = input("Name: ").strip()
    role = input("Role (e.g., Python Developer): ").strip()
    about = input("About (short): ").strip()
    skills = input("Skills (comma separated): ").strip().split(",")
    github = input("GitHub URL: ").strip()
    linkedin = input("LinkedIn URL: ").strip()
    projects = []
    while True:
        add = input("Add a project? (y/n): ").strip().lower()
        if add != "y":
            break
        title = input("  Project Title: ").strip()
        desc = input("  Description: ").strip()
        link = input("  Link (optional): ").strip()
        projects.append({"title": title, "description": desc, "link": link})
    data = {
        "name": name, "role": role, "about": about,
        "skills": [s.strip() for s in skills if s.strip()],
        "github": github, "linkedin": linkedin,
        "projects": projects
    }
    with open(config_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"💾 Saved config to {config_file}")
    return data

def generate_portfolio(output_file="portfolio.html"):
    data = load_or_prompt()
    html = build_html(data)
    Path(output_file).write_text(html, encoding="utf-8")
    print(f"✅ Portfolio generated: {output_file}")
    webbrowser.open("file://" + str(Path(output_file).resolve()))

if __name__ == "__main__":
    generate_portfolio()

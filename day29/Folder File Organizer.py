# Day 29 — Folder File Organizer
# Usage: python day29_folder_organizer.py /path/to/folder

import os
import shutil
import sys
from pathlib import Path

EXT_MAP = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg", ".webp"],
    "Docs": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx", ".csv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Video": [".mp4", ".mkv", ".mov", ".avi"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp", ".rs", ".ts"]
}

def category_for(ext):
    for cat, exts in EXT_MAP.items():
        if ext.lower() in exts:
            return cat
    return "Others"

def organize(folder):
    p = Path(folder)
    if not p.exists() or not p.is_dir():
        print("❌ Invalid folder.")
        return

    for item in p.iterdir():
        if item.is_file():
            ext = item.suffix
            cat = category_for(ext)
            dest = p / cat
            dest.mkdir(exist_ok=True)
            try:
                shutil.move(str(item), str(dest / item.name))
                print(f"➡ Moved: {item.name} -> {cat}/")
            except Exception as e:
                print(f"⚠ Could not move {item.name}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python day29_folder_organizer.py <folder-path>")
    else:
        organize(sys.argv[1])

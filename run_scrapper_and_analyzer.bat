@echo off
cd /d "C:\path\to\your\directory"
call .venv\Scripts\activate
python scraper.py
python analyze.py

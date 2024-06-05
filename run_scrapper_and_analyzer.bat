@echo off
cd /d "C:\path\to\your\directory"
call .venv\Scripts\activate
python scrapper.py
python analyze.py
@echo off
start cmd /c python facebook_apisscrape_start.py
timeout /t 3 /nobreak
start cmd /c python facebook_apis.py
timeout /t 3 /nobreak
start facebook-dashboard/dashboard-v1.html
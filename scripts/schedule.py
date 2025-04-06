import lxml
import requests
from bs4 import BeautifulSoup
import re
import time

link = f"https://www.cricbuzz.com/cricket-schedule/upcoming-series/international"
source = requests.get(link).text
page = BeautifulSoup(source, "lxml")

# Find all match containers
match_containers = page.find_all("div", class_="cb-col-100 cb-col")

matches = []

# Iterate through each match container
for container in match_containers:
    # Extract match details
    date = container.find("div", class_="cb-lv-grn-strip text-bold")
    match_info = container.find("div", class_="cb-col-100 cb-col")
    
    if date and match_info:
        match_date = date.text.strip()
        match_details = match_info.text.strip()
        matches.append(f"{match_date} - {match_details}")

print(f"Upcoming Matches: {matches}")
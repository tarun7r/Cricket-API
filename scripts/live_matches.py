import lxml
import requests
from bs4 import BeautifulSoup
import re
import time



link = f"https://www.cricbuzz.com/cricket-match/live-scores"
source = requests.get(link).text
page = BeautifulSoup(source, "lxml")

page = page.find("div",class_="cb-col cb-col-100 cb-bg-white")
matches = page.find_all("div",class_="cb-scr-wll-chvrn cb-lv-scrs-col")

live_matches = []

for i in range(len(matches)):
    live_matches.append(matches[i].text.strip())

print(live_matches)
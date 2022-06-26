import lxml
import requests
from bs4 import BeautifulSoup
import re
import time



link = f"https://www.cricbuzz.com/cricket-schedule/upcoming-series/international"
source = requests.get(link).text
page = BeautifulSoup(source, "lxml")

page = page.find_all("div",class_="cb-col-100 cb-col")




first = page[0].find_all("div",class_="cb-col-100 cb-col")

matches = []

for i in range(len(first)):
    matches.append(first[i].text)




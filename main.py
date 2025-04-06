from flask import Flask, jsonify
import lxml
import requests
from bs4 import BeautifulSoup
import re
import time
from flask import Response
import json
from googlesearch import search #pip install googlesearch-python
from flask import render_template

app = Flask(__name__)


@app.route('/players/<player_name>', methods=['GET'])
def get_player(player_name):
    query = f"{player_name} cricbuzz"
    profile_link = None
    try:
        results = search(query, num_results=5)
        for link in results:
            if "cricbuzz.com/profiles/" in link:
                profile_link = link
                print(f"Found profile: {profile_link}")
                break
                
        if not profile_link:
            return {"error": "No player profile found"}
    except Exception as e:
        return {"error": f"Search failed: {str(e)}"}
    
    # Get player profile page
    c = requests.get(profile_link).text
    cric = BeautifulSoup(c, "lxml")
    profile = cric.find("div", id="playerProfile")
    pc = profile.find("div", class_="cb-col cb-col-100 cb-bg-white")
    
    # Name, country and image
    name = pc.find("h1", class_="cb-font-40").text
    country = pc.find("h3", class_="cb-font-18 text-gray").text
    image_url = None
    images = pc.findAll('img')
    for image in images:
        image_url = image['src']
        break  # Just get the first image

    # Personal information and rankings
    personal = cric.find_all("div", class_="cb-col cb-col-60 cb-lst-itm-sm")
    role = personal[2].text.strip()
    
    icc = cric.find_all("div", class_="cb-col cb-col-25 cb-plyr-rank text-right")
    # Batting rankings
    tb = icc[0].text.strip()   # Test batting
    ob = icc[1].text.strip()   # ODI batting
    twb = icc[2].text.strip()  # T20 batting
    
    # Bowling rankings
    tbw = icc[3].text.strip()  # Test bowling
    obw = icc[4].text.strip()  # ODI bowling
    twbw = icc[5].text.strip() # T20 bowling

    # Summary of the stats
    summary = cric.find_all("div", class_="cb-plyr-tbl")
    batting = summary[0]
    bowling = summary[1]

    # Batting statistics
    bat_rows = batting.find("tbody").find_all("tr")
    batting_stats = {}
    for row in bat_rows:
        cols = row.find_all("td")
        format_name = cols[0].text.strip().lower()  # e.g., "Test", "ODI", "T20"
        batting_stats[format_name] = {
            "matches": cols[1].text.strip(),
            "runs": cols[3].text.strip(),
            "highest_score": cols[5].text.strip(),
            "average": cols[6].text.strip(),
            "strike_rate": cols[7].text.strip(),
            "hundreds": cols[12].text.strip(),
            "fifties": cols[11].text.strip(),
        }

    # Bowling statistics
    bowl_rows = bowling.find("tbody").find_all("tr")
    bowling_stats = {}
    for row in bowl_rows:
        cols = row.find_all("td")
        format_name = cols[0].text.strip().lower()  # e.g., "Test", "ODI", "T20"
        bowling_stats[format_name] = {
            "balls": cols[3].text.strip(),
            "runs": cols[4].text.strip(),
            "wickets": cols[5].text.strip(),
            "best_bowling_innings": cols[9].text.strip(),
            "economy": cols[7].text.strip(),
            "five_wickets": cols[11].text.strip(),
        }

    # Create player stats dictionary
    player_data = {
        "name": name,
        "country": country,
        "image": image_url,
        "role": role,
        "rankings": {
            "batting": {
                "test": tb,
                "odi": ob,
                "t20": twb
            },
            "bowling": {
                "test": tbw,
                "odi": obw,
                "t20": twbw
            }
        },
        "batting_stats": batting_stats,
        "bowling_stats": bowling_stats
    }

    return jsonify(player_data)


@app.route('/schedule')
def schedule():
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
    
    return jsonify(matches)


@app.route('/live')
def live_matches():
    link = f"https://www.cricbuzz.com/cricket-match/live-scores"
    source = requests.get(link).text
    page = BeautifulSoup(source, "lxml")

    page = page.find("div",class_="cb-col cb-col-100 cb-bg-white")
    matches = page.find_all("div",class_="cb-scr-wll-chvrn cb-lv-scrs-col")

    live_matches = []

    for i in range(len(matches)):
        live_matches.append(matches[i].text.strip())
    
    
    return jsonify(live_matches)

@app.route('/')
def website():
    return render_template('index.html')

if __name__ =="__main__":
    app.run(debug=True)

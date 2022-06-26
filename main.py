from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import re





app = Flask(__name__)

@app.route('/')
def index():
    return "Hey there! Welcome to the Cricket API"

@app.route('/players/<player_name>', methods=['GET'])
def get_player(player_name):

    source = requests.get(f"https://www.google.com/search?q={player_name}%20cricbuzz").text

    page = BeautifulSoup(source, "lxml")
    page = page.find("div",class_="kCrYT")
    link = page.find("a", href=re.compile(r"[/]([a-z]|[A-Z])\w+")).attrs["href"]
    c =  requests.get(link[7:]).text
    cric = BeautifulSoup(c, "lxml")

    profile = cric.find("div",id="playerProfile")
    pc = profile.find("div",class_="cb-col cb-col-100 cb-bg-white")

    #name country and image
    name = pc.find("h1",class_="cb-font-40").text  #1
    country = pc.find("h3",class_="cb-font-18 text-gray").text #2
    images = pc.findAll('img')
    for image in images:
        i = image['src']    #3

    #personal information and rankings
    personal =cric.find_all("div",class_="cb-col cb-col-60 cb-lst-itm-sm")
    role = personal[2].text.strip()  #5
    icc = cric.find_all("div",class_="cb-col cb-col-25 cb-plyr-rank text-right")
    tb = icc[0].text.strip()  #6
    ob = icc[1].text.strip()  #7
    twb = icc[2].text.strip() #8

    tbw=icc[3].text.strip()  #9
    obw=icc[4].text.strip()  #10
    twbw=icc[5].text.strip() #11


    #summary of the stata
    summary  = cric.find_all("div",class_="cb-plyr-tbl")
    batting =summary[0]
    bowling =summary[1]

    cat = cric.find_all("td",class_="cb-col-8")


    batstat = batting.find_all("td",class_="text-right")
    #test
    testmatches = batstat[0].text
    testruns = batstat[3].text
    tesths = batstat[4].text
    testavg = batstat[5].text
    testsr = batstat[7].text              
    test100 = batstat[8].text
    test50 = batstat[10].text

    #odii
    odimatches = batstat[13].text
    odiruns = batstat[16].text
    odihs = batstat[17].text
    odiavg = batstat[18].text
    odisr = batstat[20].text
    odi100 = batstat[21].text      
    odi50 = batstat[23].text

    #t20
    tmatches = batstat[26].text
    truns = batstat[29].text
    ths = batstat[30].text
    tavg = batstat[31].text         
    tsr = batstat[33].text
    t100 = batstat[34].text
    t50 = batstat[36].text


    bowstat = bowling.find_all("td",class_="text-right")

    testballs = bowstat[2].text
    testbruns = bowstat[3].text
    testwickets = bowstat[4].text
    testbbi = bowstat[5].text
    testbbm = bowstat[6].text
    testecon = bowstat[7].text
    test5w = bowstat[10].text

    odiballs = bowstat[14].text
    odibruns = bowstat[15].text
    odiwickets = bowstat[16].text
    odibbi = bowstat[17].text
    odiecon = bowstat[19].text
    odi5w = bowstat[22].text

    tballs = bowstat[26].text
    tbruns = bowstat[27].text
    twickets = bowstat[28].text
    tbbi = bowstat[29].text
    tecon = bowstat[31].text
    t5w = bowstat[34].text

    data1 = [ {"Player Name": name, "Country": country , "Role":  role , "Batting Career Summary 1": { "Mode1": cat[0].text, "Matches": testmatches, "Runs": testruns ,"HS": tesths, "Avg": testavg ,"SR":testsr ,"100s": test100 ,"50s": test50 }}]
    data2 = [ { "Batting Career Summary2": { "Mode2": cat[1].text, "Matches": odimatches, "Runs": odiruns ,"HS": odihs, "Avg": odiavg ,"SR":odisr ,"100s": odi100 ,"50s": odi50}}]
    data3 = [ { "Batting Career Summary3": { "Mode2": cat[1].text, "Matches": tmatches, "Runs": truns ,"HS": ths, "Avg": tavg ,"SR":tsr ,"100s": t100 ,"50s": t50}}]
    data4 = [ { "Bowling Career Summary1": { "Mode3": cat[2].text, "Matches": testballs, "Runs": testbruns ,"Wickets": testwickets, "BBI": testbbi, "BBM": testbbm, "Econ": testecon, "5W": test5w}}]
    data5 = [ { "Bowling Career Summary2": { "Mode3": cat[2].text, "Matches": odiballs, "Runs": odibruns ,"Wickets": odiwickets, "BBI": odibbi, "BBM": odiecon, "Econ": odiecon, "5W": odi5w}}]
    data6 = [ { "Bowling Career Summary3": { "Mode3": cat[2].text, "Matches": tballs, "Runs": tbruns ,"Wickets": twickets, "BBI": tbbi, "BBM": tecon, "Econ": tecon, "5W": t5w}}]
    return jsonify (data1, data2, data3, data4, data5, data6) 



        
@app.route('/schedule')
def schedule():
    link = f"https://www.cricbuzz.com/cricket-schedule/upcoming-series/international"
    source = requests.get(link).text
    page = BeautifulSoup(source, "lxml")
    page = page.find_all("div",class_="cb-col-100 cb-col")
    first = page[0].find_all("div",class_="cb-col-100 cb-col")
    matches = []
    for i in range(len(first)):
        matches.append(first[i].text)
    
    
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
        live_matches.append(matches[i].text)
    
    
    return jsonify(live_matches)





if __name__ =="__main__":
    app.run(host='0.0.0.0',port=8080)

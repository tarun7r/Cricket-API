import lxml
import requests
from bs4 import BeautifulSoup
import re
import time

msg = input()
source = requests.get(f"https://www.google.com/search?q={msg}%20cricbuzz").text


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


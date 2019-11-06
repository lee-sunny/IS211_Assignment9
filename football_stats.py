#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
IS211_Assignment9
Sunah Lee
football_stats.py
"""

#Part I CBS Football Stats
import urllib
import urllib.request
from bs4 import BeautifulSoup

#Load URL
def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

soup = make_soup("https://www.cbssports.com/nfl/stats/playersort/nfl/year-2019-season-regular-category-touchdowns")

#parse URL using BeautifulSoup
#output the list of top 20 players including the player's position, team, and total number of touchdowns

def main():
    stats = soup.find_all("table", attrs={"class": "data"})[0].find_all('tr', attrs={"valign": "top"})
    counter = 0
    for stat in stats:
        player = stat.find_all('td')[0].find_all('a')[0].contents[0]
        position = stat.find_all('td')[1].contents[0]
        team = stat.find_all('td')[2].find_all('a')[0].contents[0]
        touchdown = stat.find_all('td')[6].contents[0]
        counter += 1
        print(player, position, team, touchdown)
        if counter >= 20:
            break

if __name__ == '__main__':
    main()

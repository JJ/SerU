import requests
from bs4 import BeautifulSoup
import json
import sys

# Obtain the news objects.

news_channel = requests.get("https://canal.ugr.es/agenda/semana/")
news_channel_soup = BeautifulSoup(news_channel.content, "html.parser")

titles = []
hrefs = []
times = []

raw_titles_hrefs = news_channel_soup.find_all(class_="title-evento-semana text-bold")
raw_times = news_channel_soup.find_all(class_="event-schedule-detail text-medium text-color-dark-grey")

for element in raw_times:
    print(element)

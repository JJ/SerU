# -*- coding: utf-8 -*-
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
    times.append(element.get_text().lstrip())

for element in raw_titles_hrefs:
    hrefs.append(str(element.get('href')).lstrip())
    titles.append(str(element.get_text()).lstrip())

'''
The definition of the JSON object would be:
{
    title: title of the event,
    date: date of the event,
    href: hyperlink of the event,
};
'''

number_of_elements = len(titles)
data = []
for i in range(number_of_elements):
    obj = {"title":titles[i], "date":times[i], "href":hrefs[i]}
    data.append(obj)

json_obj = json.dumps(data, ensure_ascii=False)

sys.stdout.write(json_obj)
sys.stdout.flush()
sys.exit(0)

# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json
import sys

'''
The definition of the JSON object would be:
{
    title: title of the event,
    date: date of the event,
    href: hyperlink of the event,
};
'''

# Link used for requests.
EVENTS_LINK = "https://canal.ugr.es/agenda/semana/"

# Returns a tuple with the titles, hrefs and dates.
def obtainRawElements():

    # Obtain the news objects.
    news_channel = requests.get(EVENTS_LINK)
    news_channel_soup = BeautifulSoup(news_channel.content, "html.parser")

    raw_titles_hrefs = news_channel_soup.find_all(class_="title-evento-semana text-bold")
    raw_times = news_channel_soup.find_all(class_="event-schedule-detail text-medium text-color-dark-grey")

    titles = []
    hrefs = []
    times = []

    for element in raw_times:
        times.append(element.get_text().lstrip())

    for element in raw_titles_hrefs:
        hrefs.append(str(element.get('href')).lstrip())
        titles.append(str(element.get_text()).lstrip())

    return (titles, times, hrefs)

# Creates JSON object and returns it.
def createJSON(titles, times, hrefs):

    number_of_elements = len(titles)
    data = []
    for i in range(number_of_elements):
        obj = {"title":titles[i], "date":times[i], "href":hrefs[i]}
        data.append(obj)

    json_obj = json.dumps(data, ensure_ascii=False)

    return (json_obj)

# Main function of the script.
def main():
    (titl,hr,tim) = obtainRawElements()
    json_obj = createJSON(titl,hr,tim)

    sys.stdout.write(json_obj)
    sys.stdout.flush()
    sys.exit(0)

# Calls main.
main()

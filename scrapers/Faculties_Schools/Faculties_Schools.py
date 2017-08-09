# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json
import sys

'''
The definition of the JSON object would be:
{
    name: faculty/school name,
    href: faculty/school hyperlink,
};
'''

REQUEST_LINK_FACULTIES = "https://www.ugr.es/pages/centros/facultades"
UNIVERSITY_LINK = 'https://www.ugr.es'
REQUEST_LINK_SCHOOLS = "https://www.ugr.es/pages/centros/escuelas"

# Obtain faculties names and hrefs

faculties_page = requests.get(REQUEST_LINK_FACULTIES)
faculties_soup = BeautifulSoup(faculties_page.content, 'html.parser')
faculty_obj_list = faculties_soup.find_all(class_='wikilink2')
faculties = []
faculties_href = []
for obj in faculty_obj_list:
    faculties_href.append(UNIVERSITY_LINK + obj.get('href').lstrip())
    faculties.append(obj.get_text().lstrip())

# Obtain schools names and hrefs

schools_page = requests.get(REQUEST_LINK_SCHOOLS)
schools_soup = BeautifulSoup(schools_page.content, 'html.parser')
schools_obj_list = schools_soup.find_all(class_="wikilink2")
schools = []
schools_href = []
for obj in schools_obj_list:
    schools.append(obj.get_text().lstrip())
    schools_href.append(UNIVERSITY_LINK + obj.get('href').lstrip())

faculties_and_schools = faculties + schools
faculties_and_schools_href = faculties_href + schools_href
data = []

number_of_elements = len(faculties_and_schools)
for i in range(number_of_elements):
    obj = {"name":faculties_and_schools[i], "href":faculties_and_schools_href[i]}
    data.append(obj)

json_object = json.dumps(data, ensure_ascii=False)

# Would be changed soon

sys.stdout.write(json_object)
sys.stdout.flush()
sys.exit(0)

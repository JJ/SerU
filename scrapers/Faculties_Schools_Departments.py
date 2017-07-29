import requests
from bs4 import BeautifulSoup

faculties_page = requests.get("https://www.ugr.es/pages/centros/facultades")
faculties_soup = BeautifulSoup(faculties_page.content, 'html.parser')
faculty_obj_list = faculties_soup.find_all(class_='wikilink2')
faculties = []
for obj in faculty_obj_list:
    faculties.append(obj.get_text())

import requests
from bs4 import BeautifulSoup
import json
import sys

# Obtain the news objects.

noticias_canal = requests.get("https://canal.ugr.es/agenda/semana/")
noticias_canal_soup = BeautifulSoup(noticias_canal.content, "html.parser")

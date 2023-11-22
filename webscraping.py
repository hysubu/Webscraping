from bs4 import BeautifulSoup
import requests

req = requests.get('https://www.projectpro.io/article/web-scraping-projects-ideas/475')
print(req.content)
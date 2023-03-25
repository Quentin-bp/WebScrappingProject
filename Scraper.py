
from bs4 import BeautifulSoup
import requests


class Scraper:
    def __init__(self, link):
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
        }
        self.link = link
        self.req = requests.get(self.link, headers)
        

    def loadScraper(self):
        return BeautifulSoup(self.req.content, 'html.parser')
        #self.browser.get(self.link)

    def getDataFromPath(self, nameElement, classNames):
        
        soup = self.loadScraper()

        data = soup.find(nameElement, {"class": classNames})
        #data = soup.find('table', {"class":"wikitable"})

        return data

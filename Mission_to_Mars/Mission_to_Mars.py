from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "C:/Drivers/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_articles():
    browser = init_browser()
    news_articles={}

    # Nasa Mars news site
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # get news titles
    news_articles = soup.find('div', class_='content_title').get_text()
    
    return news_articles

    # get news paragraphs
    #news_p = x.find_all('y')[0].text

  
    # Close the browser after scraping
    #browser.quit()

if __name__== '__main__':
    scrape_articles()
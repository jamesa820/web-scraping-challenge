from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "C:/Drivers/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_title():
    browser = init_browser()
    news_title={}

def scrape_paragraph():
    browser=init_browser()
    new_p ={}
    
    # Nasa Mars news site
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # get news titles and paragraphs
    news_title = soup.find('div',class='content_title').get_text()
    news_p = soup.find('div', class = 'article_teaser_body')
    
    # Close the browser after scraping
    browser.quit()
   
    return news_title

    if __name__== '__main__': scrape_title()
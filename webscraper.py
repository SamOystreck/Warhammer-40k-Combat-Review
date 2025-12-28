from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Code currently not functional
#Wahapedia injects the headers we are attempting to scrape but pulls information from
#a Factions.csv file that we ARE able to scrape

#To-do : Find out how to identify this (How to see that a webpage is injecting content
# that we are looking for), as well as how to find the information that we can actually use

load_dotenv()

driver = webdriver.Chrome()
driver.get(os.getenv("SITE_INIT"))

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "FactionHeader"))
)

raw_init_html = driver.page_source
clean_init_html = BeautifulSoup(raw_init_html, "lxml")

divs = clean_init_html.find_all("div", class_="FactionHeader")
print(divs)
factions = []


driver.quit()

#Need to make a list of all the pages to scrape (all faction pages) from https://wahapedia.ru/wh40k10ed/the-rules/quick-start-guide/

#Then from each faction page we need to make a list of all model pages to scrape

#Finally we need to scrape each of these pages
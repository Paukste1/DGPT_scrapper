import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome("C:/Users/User/OneDrive - Vilnius University/Desktop/Vytautas/DGPT_scrapper/chromedriver-win64/chromedriver.exe")
driver.get("https://www.pdga.com/tour/event/77761")
results = []
content = driver.page_source
soup = BeautifulSoup(content)

for element in soup.findAll(attrs="player"):
    name = element.find("tooltip tooltipstered")
    if name not in results:
        results.append(name.text)
print(results)
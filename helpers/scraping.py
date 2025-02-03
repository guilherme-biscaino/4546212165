from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import pandas as pd
import pyshorteners
import datetime


def scrape(item):
    service = Service()
    short = pyshorteners.Shortener()

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(service=service, options=options)

    url = f'https://www.google.com/search?q={item}&tbm=shop'

    driver.get(url)
    item_price = driver.find_elements(By.CLASS_NAME, 'a8Pemb')[:5]  
    item_link = driver.find_elements(By.XPATH, "//a[contains(@class, 'shntl')]")[:10:2]
    item_price = [element.text for element in item_price]
    print("encurtando links")
    item_link = [short.tinyurl.short(element.get_attribute('href')) for element in item_link]

    frame = {'price': item_price, 'link': item_link}
    print(pd.DataFrame(frame))

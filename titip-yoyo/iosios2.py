from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import requests
import json
 
def iniFunctionIos():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    #options.add_argument("--start-maximized")
    #options.add_argument('--log-level=3')

    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s, options=options)
    driver.maximize_window()
    driver.get('https://developer.apple.com/news/releases/')
    time.sleep(10)
  
    element = driver.find_element(By.XPATH, "/html/body/main/section/section[2]/section/article[1]/section")
    # get the text of the element
    tios = element.text
    print(tios)
   

iniFunctionIos()
     

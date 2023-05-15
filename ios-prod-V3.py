from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import requests
import json
import numpy as np

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
  
    elements = driver.find_elements(By.XPATH, "/html/body/main/section/section[2]/section") 
    release_dates = np.array([element.text for element in elements])

    print("Release dates:")
    x = -1
    y = -1
    for date in release_dates:
        x+=1
        strings=date.split("\n")
        for string in strings:
            y+=1
            if "iOS" in string:
                break

    print(x, y)
    release=release_dates[x]
    releases=release.split("\n")
    version_name=releases[y]
    version_date=releases[y+1]

    print("New Beta Release : ", version_name, "dirilis pada", version_date)
    url = "https://hooks.slack.com/services/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"
    payload = {
        "text": f"New Beta Release : {version_name, version_date}"
    }
    # Convert the payload to JSON format 
    payload_json = json.dumps(payload)
    # Send the Slack API request
    response = requests.post(url, data=payload_json)
    # # Print the response status code and text
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

iniFunctionIos()

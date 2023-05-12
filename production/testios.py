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
  
    try:
        element = driver.find_element(By.XPATH, "/html/body/main/section/section[2]/section/article[1]/section/section[2]/a/h2")
        element2 = driver.find_element(By.XPATH, "/html/body/main/section/section[2]/section/article[1]/section/section[2]/div/p")
        # get the text of the element
        tt = element.text
        tt2 = element2.text
        print(tt, tt2)
        # Set the incoming webhook URL and message text
        url = "https://hooks.slack.com/services/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"
        #text = f"{tt}"
        # Set the payload for the Slack API request
        payload = {
            "text": f"Versi Cek Beta IOS, {tt, tt2}",  
        }
        # Convert the payload to JSON format
        payload_json = json.dumps(payload)
        # Send the Slack API request
        response = requests.post(url, data=payload_json)
        # # Print the response status code and text
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")

    except:
        print("Gagal Melakukan pengecekan")
        url = "https://hooks.slack.com/services/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"
        #text = f"{tt}"
        # Set the payload for the Slack API request
        payload = {
            "text": f"Gagal Melakukan Pengecekan Ios-Beta Version",  
        }
        # Convert the payload to JSON format
        payload_json = json.dumps(payload)
        # Send the Slack API request
        response = requests.post(url, data=payload_json)
        # # Print the response status code and text
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")


iniFunctionIos()


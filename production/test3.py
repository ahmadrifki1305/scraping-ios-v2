from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import requests
import json

def siniFunctionUang():

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s, options=options)
    driver.maximize_window()
    driver.get('https://www.tencentcloud.com/account/login?s_url=https%3A%2F%2Fconsole.tencentcloud.com%2Fdeveloper%2Fsecurity');
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys("koanbacom@gmail.com");
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Mangga&besar47");
    time.sleep(3)
    driver.find_element(By.XPATH, "//div[@class='intl-account-actions-horizontal']").click();
    time.sleep(10)
    driver.get('https://console.tencentcloud.com/expense/recharge');
    time.sleep(10)

    try:
        element = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/span")
        uang = element.text
        print(uang)
        url = "https://hooks.slack.com/services/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"
        payload = {
            "text": f"{uang}",  
        }
        # Convert the payload to JSON format
        payload_json = json.dumps(payload)
        # Send the Slack API request
        response = requests.post(url, data=payload_json)
            # # Print the response status code and text
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Text: {response.text}") 
    except:
        print("Gagal Melakukan pengecekan sisa Uang")
        url = "https://hooks.slack.com/services/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"
        #text = f"{tt}"
        # Set the payload for the Slack API request
        payload = {
            "text": f"Gagal Melakukan Pengecekan diTencent Website",  
        }
        # Convert the payload to JSON format
        payload_json = json.dumps(payload)
        # Send the Slack API request
        response = requests.post(url, data=payload_json)
        # # Print the response status code and text
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
 
   

siniFunctionUang()

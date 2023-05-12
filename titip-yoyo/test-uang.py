from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import requests
import json
 

def iniFunctionTest5():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    #options.add_argument("--start-maximized")
    #options.add_argument('--log-level=3')

    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s, options=options)
    driver.maximize_window()
    driver.get('https://www.tencentcloud.com/account/login?s_url=https%3A%2F%2Fconsole.tencentcloud.com%2Fdeveloper%2Fsecurity')
    username = driver.find_element(By.XPATH, "//input[@name='username']")
    username.send_keys("koanbacom@gmail.com")
    time.sleep(3)
    password = driver.find_element(By.XPATH, "//input[@name='password']")
    password.send_keys("Mangga&besar47")
    time.sleep(3)
    submit_button = driver.find_element(By.XPATH, "//div[@class='intl-account-actions-horizontal']")
    submit_button.click()
    time.sleep(10)
    driver.get('https://console.tencentcloud.com/mps')
    time.sleep(10)


    try:
        element = driver.find_element(By.CSS_SELECTOR, "/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/span")
        # get the text of the element
        tt = element.text
        print(tt)
        # Set the incoming webhook URL and message text
        url = "https://hooks.slack.com/services/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"
        #text = f"{tt}"
        # Set the payload for the Slack API request
        payload = {
            "text": f"{tt}",  
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
            "text": f"Gagal Melakukan Pengecekan diTencent Website",  
        }
        # Convert the payload to JSON format
        payload_json = json.dumps(payload)
        # Send the Slack API request
        response = requests.post(url, data=payload_json)
        # # Print the response status code and text
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")

    # close the browser
    #driver.quit()

    # print the text of the element


    #  while True:
    #      # code to execute continuously
    #     if user_input == 'exit':
    #          break

#iniFunctionTest5()
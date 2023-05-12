import requests

URL = "https://console.tencentcloud.com/mps"
page = requests.get(URL)

print(page.text)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--headless")  # Run Chrome in headless mode (without GUI)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

url = "https://developer.apple.com/news/releases/"
driver.get(url)

elements = driver.find_elements(By.XPATH, "/html/body/main/section/section[2]//*[contains(text(), 'iOS')]")
release_dates = [element.text for element in elements]

hot_ios = release_dates[0]
print (hot_ios)
driver.quit()

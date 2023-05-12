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

# Find the element that contains the top iOS version
top_version_element = driver.find_element(By.XPATH, "/html/body/main/section/section[2]//*[contains(text(), 'iOS')][1]")

# Extract the text of the top version
top_version = top_version_element.text
print("Top iOS version:", top_version)

# Find the release date element relative to the top version element
release_date_element = top_version_element.find_element(By.XPATH, "./ancestor::article/following-sibling::article//p[contains(@class, 'article-date')]")

# Extract the text of the release date
release_date = release_date_element.text
print("Release date of the top iOS version:", release_date)

driver.quit()

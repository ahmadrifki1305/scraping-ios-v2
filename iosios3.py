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

# Get top iOS version
elements_ios = driver.find_elements(By.XPATH, "/html/body/main/section/section[2]//*[contains(text(), 'iOS')]")
iOS_versions = [element.text for element in elements_ios]

if len(iOS_versions) > 0:
    top_version = iOS_versions[0]
    print("Top iOS version:", top_version)
else:
    print("No iOS versions found.")

# Get release dates
elements_dates = driver.find_elements(By.XPATH, "/html/body/main/section/section[2]/section/article[1]/section/section[2]/div/p")
release_dates = [element.text for element in elements_dates]

print("Release dates:")
for date in release_dates:
    print(date)

driver.quit()
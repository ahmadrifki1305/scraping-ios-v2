
from selenium import webdriver
import time
  
# Main Function
if __name__ == '__main__':
  
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument('--log-level=3')
   

    # Provide the path of chromedriver present on your system.
    driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver/chromedriver",
                              chrome_options=options)
    driver.set_window_size(1920,1080)
  
    # Send a get request to the url
    driver.get('https://www.tencentcloud.com/account/login?s_url=https%3A%2F%2Fconsole.tencentcloud.com%2Fdeveloper%2Fsecurity')
    #username = driver.find_element_by_xpath(("//input[@name='username']").send_keys("koanbacom@gmail.com"))
    time.sleep(2)
    #driver.quit()
    print("Done")



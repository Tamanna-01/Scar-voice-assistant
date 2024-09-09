# # from selenium import webdriver
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By


# class infow():
#     def __init__(self):
#         chrome_driver_path = 'C:/Users/Tamanna/Desktop/Temp/Python/Projects/Scar/chromedriver.exe'
#         service = Service(chrome_driver_path)
#         self.driver = webdriver.Chrome(service=service)


#     def get_info(self, query):
#         self.query = query
#         self.driver.get(url="https://www.wikipedia.org")
#         search = self.driver.find_element(by=By.XPATH, value='//*[@id="searchInput"]')
#         search.click()
#         search.send_keys(query)
#         enter = self.driver.find_element(by=By.XPATH, value='//*[@id="search-form"]/fieldset/button')
#         enter.click()
# # make the bot speak the first passage from the wikipedia page

# # assist = infow()
# # assist.get_info("shawn mendes")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class Infow():
    def __init__(self):
        options=webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        chrome_driver_path = 'C:/Users/Tamanna/Desktop/Temp/Python/Projects/Scar/chromedriver.exe'
        service = Service(chrome_driver_path)
        self.driver = webdriver.Chrome(options=options,service=service)
        self.driver._is_remote = True  # Prevent WebDriver from closing after script execution


    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org")
        search = self.driver.find_element(by=By.XPATH, value='//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element(by=By.XPATH, value='//*[@id="search-form"]/fieldset/button')
        enter.click()

# Create an instance of the class
# assist = Infow()
# assist.get_info("shawn mendes")

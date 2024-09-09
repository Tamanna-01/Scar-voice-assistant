# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By


# class music():
#     def __init__(self):
#         options=webdriver.ChromeOptions()
#         options.add_experimental_option("detach", True)
#         chrome_driver_path = 'C:/Users/Tamanna/Desktop/Temp/Python/Projects/Scar/chromedriver.exe'
#         service = Service(chrome_driver_path)
#         self.driver = webdriver.Chrome(service=service)
    
#     def play(self, query):
#         self.query = query
#         self.driver.get(url="https://www.youtube.com/results?search_query="+query)
#         video = self.driver.find_element(by=By.XPATH, value='//*[@id="dismissible"]') #fix the xpath
#         video.click()

# assist = music()
# assist.play("believer")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class music():
    def __init__(self):
        chrome_driver_path = 'C:/Users/Tamanna/Desktop/Temp/Python/Projects/Scar/chromedriver.exe'
        service = Service(chrome_driver_path)
        self.driver = webdriver.Chrome(service=service)
    
    def play(self, query):
        self.query = query
        self.driver.get("https://www.youtube.com/results?search_query=" + query)
        try:
            video = self.driver.find_element(By.XPATH, '//ytd-video-renderer[1]//a[@id="video-title"]')
            video.click()
            input("Press Enter to close the browser window...")
        except Exception as e:
            print("Error:", e)

# assist = music()
# assist.play("believer")

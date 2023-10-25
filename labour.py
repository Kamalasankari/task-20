import urllib3
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import requests
import os
import urllib


class Guvi:
   def __init__(self):
       self.url = "https://labour.gov.in/"
       self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

   def click_documents_button(self):
       try:
           sleep(4)
           self.driver.maximize_window()
           sleep(4)
           self.driver.get(self.url)
           sleep(4)
           a = ActionChains(self.driver)
           m = self.driver.find_element(by=By.LINK_TEXT, value="Documents")
           sleep(4)
           # hover over element
           a.move_to_element(m).perform()
           # identify sub menu element
           self.driver.find_element(by=By.LINK_TEXT, value="Monthly Progress Report").click()
           sleep(4)
           self.driver.find_element(by=By.LINK_TEXT, value="Download(475.77 KB)").click()
           sleep(4)
           self.driver.switch_to.alert.accept()
           sleep(4)
           self.driver.switch_to.window(self.driver.window_handles[1])
           #print(self.driver.current_url)
           url1 = self.driver.current_url
           response = requests.get(url1)
           with open('Document.pdf', 'wb') as f:
               f.write(response.content)
           f.close()
           self.driver.close()
           self.driver.switch_to.window(self.driver.window_handles[0])
           # a1 = ActionChains(self.driver)
           # sleep(4)
           # m1 = self.driver.find_element(by=By.LINK_TEXT, value="Media")
           # sleep(4)
           # # hover over element
           # a1.move_to_element(m1).perform()
           # # identify sub menu element
           # self.driver.find_element(by=By.LINK_TEXT, value="Photo Gallery").click()
           # sleep(4)

       except NoSuchElementException as selenium_error:
           print(selenium_error)
       finally:
           print("Reports saved in Document.pdf")

   def click_media_button(self):
       # sleep(4)
       # self.driver.maximize_window()
       # sleep(4)
       # self.driver.get(self.url)
       # sleep(4)
       a1 = ActionChains(self.driver)
       sleep(4)
       m1 = self.driver.find_element(by=By.LINK_TEXT, value="Media")
       sleep(4)
       # hover over element
       a1.move_to_element(m1).perform()
       # identify sub menu element
       self.driver.find_element(by=By.LINK_TEXT, value="Photo Gallery").click()
       sleep(4)
       # Directory
       self.directory = "Photo Gallery"
       # Parent Directory path
       self.parent_dir = "C:\\Users\\msori\\PycharmProjects\\pythonProject\\workspace\\task 20"


       path = os.path.join(self.parent_dir, self.directory)

       try:
           src= []
           os.makedirs(path, exist_ok =True)
           #print(self.driver.title)
           images = self.driver.find_elements(by=By.XPATH, value="//div[@class='field-content']//img")


           for image in images:
               src.append(image.get_attribute('src'))
           #print(src)
           for i in range(10):
               urllib.request.urlretrieve(str(src[i]), "Photo Gallery/image{}.jpg".format(i))
       except OSError as error:
           print("Directory '%s' can not be created")
       finally:
           print("10 images from the webpage is downloaded in the folder Photo Gallery")
           self.driver.close()



labor = Guvi()
labor.click_documents_button()
labor.click_media_button()
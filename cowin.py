from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class Guvi:
   def __init__(self):
       self.url = "https://www.cowin.gov.in/"
       self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

   def click_faq_button(self):

       self.driver.maximize_window()
       self.driver.get(self.url)
       sleep(4)
       self.driver.find_element(by=By.LINK_TEXT, value="FAQ").click()
       sleep(4)
       self.driver.find_element(by=By.XPATH, value='//*[@id="navbar"]/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a').click()
       all_tab = self.driver.window_handles
       curr_tab = self.driver.current_window_handle
       print(curr_tab)

       for i in all_tab:
           if i is all_tab[0]:
               print("cowin frame id is", all_tab[0])
           if i is all_tab[1]:
               print("cowin_faq frame id is", all_tab[1])
               #self.driver.close()
           if i is all_tab[2]:
               print("cowin_partners frame id is", all_tab[2])
           if i != curr_tab:

               self.driver.switch_to.window(i)
               sleep(4)
               self.driver.close()
       self.driver.switch_to.window(curr_tab)
       sleep(4)
       self.driver.close()

cowin = Guvi()
cowin.click_faq_button()



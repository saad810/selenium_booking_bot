# booking class insatanse
import booking.constants as const
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class Booking(webdriver.Edge):
    # constructor
    def __init__(self,driver_path = r"C:\selenium\edge\msedgedriver", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        
        os.environ['PATH'] += self.driver_path
        super(Booking,self).__init__()
        self.implicitly_wait(15) # wait 15 seconds
        self.maximize_window() # maximize the window
    
    def __exit__(self,exc_type,exc_val,exc_tb):
        print(self.teardown,"__exit__")
        if self.teardown:
            self.quit()
       
    def land_first_page(self):
        self.get(const.BASE_URL)
        # time.sleep(5)

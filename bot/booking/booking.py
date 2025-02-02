# booking class insatanse
import booking.constants as const
import os
from selenium import webdriver

class Booking(webdriver.Chrome):
    # constructor
    def __init__(self,driver_path = r"C:\selenium\chrome-win64"):
        self.driver_path = driver_path
        #to instantiate the web driver class , their might be a error that inherited class is not instantiated
        os.environ['PATH'] += self.driver_path
        super(Booking,self).__init__()
        
    def land_first_page(self):
        self.get(const.BASE_URL)

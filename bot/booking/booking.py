# booking class insatanse
import booking.constants as const
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        print("[__exit__]",self.teardown)
        if self.teardown:
            self.quit()
        # time.sleep(15)
        # self.quit()
       
    def land_first_page(self):
        self.get(const.BASE_URL)
        # time.sleep(5)

    def dismiss_modal_if_present(self):
        try:
            # Wait up to 3 seconds for the modal to appear
            WebDriverWait(self, 3).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Dismiss sign-in info."]'))
            )

            # If found, click to dismiss
            dismiss_modal_element = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Dismiss sign-in info."]')
            dismiss_modal_element.click()
            print("[Dismiss sign in] Modal closed")
    
        except:
            print("[Dismiss sign in] No modal found")
    
    
    def change_currency(self, currency='None'):

        if currency == 'None':
            print("[lib err] No currency provided")
            return
        # dismiss modal
        # try:
        #     dismiss_modal_element = self.find_element(
        #         By.CSS_SELECTOR,
        #         'button[aria-label="Dismiss sign-in info."]'
        #     )
        #     dismiss_modal_element.click()
        # except:
        #     print("[Dismiss sign in] No element found ")
        #     pass
        
        self.dismiss_modal_if_present()

        # click on currency selector button
        currency_element = self.find_element(
            By.CSS_SELECTOR,
            'button[aria-controls="header_currency_picker"]'
        )
        currency_element.click()

        # select currency

        selcted_currency = self.find_element(
            By.XPATH, f"//button[.//div[contains(@class, 'CurrencyPicker_currency') and contains(text(), '{currency}')]]"
        )
        selcted_currency.click()
    
    # def search_place_to_visit(self, place_to_visit='None'):
    #     if place_to_visit == 'None':
    #         print("[lib err] No place to visit provided")
    #         return
        
    #     self.dismiss_modal_if_present()
    
    #     search_field = self.find_element(
    #         By.ID,
    #         ':rh:'
    #     )
    #     search_field.send_keys(place_to_visit)

    #     # get first dropdown and click
    #     try:
    #         first_item = WebDriverWait(self, 20).until(
    #             EC.presence_of_element_located((By.ID, 'autocomplete-result-0'))
    #         )
    #         # optional check if element is clickable
    #         clickable = WebDriverWait(self, 20).until(
    #             EC.element_to_be_clickable(first_item)
    #         )

    #         clickable.click()
    #         print(f"[search_place_to_visit] Selected: {place_to_visit}")


    #     except Exception as e:
    #         print(f"[search_place_to_visit] Error finding item: {str(e)}")

    def search_place_to_visit(self, place_to_visit='None'):
        if place_to_visit == 'None':
            print("[lib err] No place to visit provided")
            return

        # Dismiss any modal if present
        self.dismiss_modal_if_present()

        # Locate the search field and enter the place to visit
        search_field = self.find_element(By.ID, ':rh:')
        search_field.send_keys(place_to_visit)

        # Wait for the dropdown to appear and ensure it has items
        try:
            # Wait until the dropdown with role="group" is visible and contains results
            WebDriverWait(self, 50).until(
                EC.visibility_of_element_located((By.XPATH, '//ul[@role="group"]/li'))
            )
            time.sleep(2)

            # Wait for the first result to be clickable
            first_item = WebDriverWait(self, 50).until(
                EC.element_to_be_clickable((By.ID, 'autocomplete-result-0'))
            )

            first_item.click()  # Click on the first result
            print(f"[search_place_to_visit] Selected: {place_to_visit}")

        except Exception as e:
            print(f"[search_place_to_visit] Error finding item: {str(e)}")
   
    # def select_date(self, check_in_date='2025-02-05'):
    #     # Ensure the date format matches the one in data-date attribute
    #     try:
    #         date_xpath = f'//td[span[@data-date="{check_in_date}"]]'

    #         # Wait for the date cell to be present
    #         date_cell = WebDriverWait(self, 10).until(
    #             EC.presence_of_element_located((By.XPATH, date_xpath))
    #         )

    #         # Click on the date cell
    #         date_cell.click()
    #         print(f"[select_date] Selected date: {check_in_date}")   

    #     except Exception as e:
    #         print(f"[select_date] Error selecting date: {str(e)}")

    def select_date(self, start_date='5 February 2025', end_date='8 February 2025'):
        try:
            start_date_xpath = f'//td[span[@aria-label="{start_date}"]]'
            end_date_xpath = f'//td[span[@aria-label="{end_date}"]]'

            # Wait for the date cell to be present
            start_date_cell = WebDriverWait(self, 10).until(
                EC.presence_of_element_located((By.XPATH, start_date_xpath))
            )

            # Click on the date cell
            start_date_cell.click()
            print(f"[select_date_by_aria_label] Selected date: {start_date}")


            end_date_cell = WebDriverWait(self, 10).until(
                EC.presence_of_element_located((By.XPATH, end_date_xpath))
            )

            # Click on the date cell
            end_date_cell.click()
            print(f"[select_date_by_aria_label] Selected date: {end_date}")

        except Exception as e:
            print(f"[select_date_by_aria_label] Error selecting date: {str(e)}")

    def select_adults(self, adults = 1):
        # adults_button_xpath = f'//div[button[data-testid="occupancy-config"]]'
        adults_button = self.find_element(
            By.CSS_SELECTOR,
            'button[data-testid="occupancy-config"]'
        )
        # adults_button = self.find_element(By.XPATH, adults_button_xpath)
        adults_button.click()

        # Wait for the modal to appear
        # modal = WebDriverWait(self, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="occupancy-modal"]'))
        # )

        #set adults to 0

       

    def click_search(self):
        search_button = '//div[@data-testid="searchbox-layout-wide"]//button[@type="submit"]'
        search_button_element = self.find_element(By.XPATH, search_button)
        search_button_element.click()
        print("[clicked] Search buttton")

    def apply_sort(self, sort_val = 'top_reviewed'):
        try:
            sort_button = '//div//button[@data-testid="sorters-dropdown-trigger"]'
            sort_button_element = self.find_element(By.XPATH, sort_button)
            sort_button_element.click()

            # wait for drop down

            sort_dropDown = WebDriverWait(self, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//div[@data-testid="sorters-dropdown"]'))
            )

            if not sort_dropDown:
                print("[apply_sort] Sort dropdown not found")


            sort_option = const.sorting_options.get(sort_val)
            sort_option_element = self.find_element(By.XPATH, f'//div[@data-testid="sorters-dropdown"]//li//button[@{sort_option}]')


            sort_option_element.click()
            print(f"[apply_sort] Applied sort: {sort_val}")

            time.sleep(20)

        except Exception as e:
            print(f"[apply_sort] Error applying sort: {str(e)}")


    def add_more_filters(self, rating = 5):
        try:
            if(rating > 5 or rating < 0):
                print("[add_more_filters] Invalid rating value")
                return
            
            rating_element_xpath = f'//div[@data-testid="filters-sidebar"]//div[@data-filters-group="class"]//fieldset//div[@id="filter_group_class_:r23:"]//div[@data-filters-item="class:class={rating}"]//input[@type="checkbox"]'

            rating_element = self.find_element(By.XPATH, rating_element_xpath)

            if not rating_element.is_selected:
                rating_element.click()
            else :
                print("[add_more_filters] Rating already selected")

        except Exception as e:
            print(f"[add_more_filters] Error applying filters: {str(e)}") 


        






      



        

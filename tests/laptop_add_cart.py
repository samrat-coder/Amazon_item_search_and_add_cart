from pexecute.process import loom
from selenium import webdriver
import time

from config_driver.config import create_driver, open_url, switch_to_next_tab
from pages.Home_page import search_item
from pages.product_page import cart, close_popup_window
from pages.result_page import brand_name, select_first_item
def multiple_open():
 driver = create_driver()
 open_url(driver)
 time.sleep(5)
 search_item(driver, "laptop")
 time.sleep(5)
 brand_name(driver)
 time.sleep(3)
 select_first_item(driver)
 switch_to_next_tab(driver)
 cart(driver)
 time.sleep(3)
 close_popup_window(driver)
 time.sleep(5)
 driver.quit()

from pexecute.process import ProcessLoom
loom = ProcessLoom(max_runner_cap=3)

loom.add_function(multiple_open)
loom.add_function(multiple_open)
output = loom.execute()


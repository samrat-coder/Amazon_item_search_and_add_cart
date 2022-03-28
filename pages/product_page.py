import time

from pytest_bdd import when
from selenium.webdriver.common.by import By


@when("user cart item")
def cart(driver):
    add_cart = driver.find_element(By.ID, "add-to-cart-button")
    add_cart.click()
    time.sleep(5)
#@when("close popup window")
#def close_popup_window(driver):
    #close_popup = driver.find_element(By.XPATH, "//a[@class='a-link-normal close-button']")
    #close_popup.click()
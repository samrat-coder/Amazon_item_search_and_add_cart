from pytest_bdd import when, parsers
from selenium.webdriver.common.by import By


@when(parsers.cfparse("user search item '{laptop}'"))
def search_item(driver, laptop):
    var = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
    var.click()
    var.send_keys(laptop)
    var1 = driver.find_element(By.XPATH, "//input[@type='submit']")
    var1.click()
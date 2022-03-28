from pytest_bdd import when
from selenium.webdriver.common.by import By


@when("user click brand name")
def brand_name(driver):
    var2 = driver.find_element(By.XPATH, '//a[@id="p_89/HP"]')
    var2.click()
@when("user select first item")
def select_first_item(driver):
    var3 = driver.find_elements(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
    var3[0].click()
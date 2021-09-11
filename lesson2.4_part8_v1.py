from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


def func(x):
    return math.log(abs(12 * math.sin(int(x))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)
 
try:
    button = browser.find_element_by_css_selector("#book")
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button.click()
    
    x = (browser.find_element_by_css_selector("#input_value")).text
    result = func(x)
    
    output = browser.find_element_by_css_selector(".form-control")
    output.send_keys(str(result))
    
    button = browser.find_element_by_css_selector("#solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    
    alert = browser.switch_to.alert
    print(alert.text)
    
    browser.quit()    
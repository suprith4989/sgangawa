from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
# We import it to use the sleep() method in the end
import time

def page_is_loaded(driver):
    return driver.find_element_by_tag_name("body") != None

driver = webdriver.Firefox()
driver.get("https://www.facebook.com/")

wait = ui.WebDriverWait(driver, 10)
wait.until(page_is_loaded)

# Here you provide your mail id
email_field = driver.find_element_by_id("email")
email_field.send_keys("example@example.com")

# Here you pass your password
password_field = driver.find_element_by_id("pass")
password_field.send_keys("password")
password_field.send_keys(Keys.RETURN)

# Wait for 5 seconds until the login is successful
time.sleep(5)
# Close the driver
driver.close()

# Try and run this script as it is and have a look for yourself

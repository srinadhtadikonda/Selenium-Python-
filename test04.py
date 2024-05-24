from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("http://demo.guru99.com/v1")
user_id_box = driver.find_element(By.XPATH, "//input[@name='uid']")
user_id_box.send_keys("mngr34926")  # Replace with the actual user ID
print("successfully Executed.")

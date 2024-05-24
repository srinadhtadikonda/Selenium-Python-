from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("https://demo.guru99.com/test/newtours/")
user_id_box = driver.find_element(By.LINK_TEXT, "REGISTER")
print("successfully Executed.")

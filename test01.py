from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get('https://www.facebook.com')    
print('Test Success.')

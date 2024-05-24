from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get('https://www.facebook.com')
element = driver.find_element(By.ID, 'email')
element.send_keys('nipuna@gmail.com')    
print('Element found and interacted with successfully.')

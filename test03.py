sfrom selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get('https://demo.guru99.com/v1')s
element = driver.find_element(By.NAME, 'uid')
element.send_keys('nipuna@gmail.com')    
print('Element found and interacted with successfully.')

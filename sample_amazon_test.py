from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='drivers/chromedriver')

# open the url
driver.get('https://www.amazon.com/gp/help/customer/display.html')

search = driver.find_element(By.XPATH, "//input[@id='helpsearch']")
search.clear()
search.send_keys('Cancel order')

# wait for 2 sec
sleep(2)

# click search
driver.find_element(By.XPATH, "//span[@id='helpSearchSubmit']//input[@type='submit']").click()

# verify
assert 'Cancel Items or Orders' in driver.find_element(By.XPATH, "//div[@class='help-content']").text

# wait for 2 sec
sleep(2)

driver.quit()
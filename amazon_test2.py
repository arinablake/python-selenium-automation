from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='drivers/chromedriver')

# open the url
driver.get('https://www.amazon.com')


# click search
driver.find_element(By.XPATH, "//span[@class='nav-line-2'][text()='& Orders']").click()

# verify
assert 'Sign-In' in driver.find_element(By.XPATH, "//form[@name='signIn']").text

# wait for 2 sec
sleep(2)

driver.quit()
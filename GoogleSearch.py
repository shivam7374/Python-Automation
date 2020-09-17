# import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

searchtext="Coding Blocks"
driver = webdriver. Chrome()
driver.get("https://www.google.com")
element = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
element.send_keys(searchtext)
element = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
element.click()
element.send_keys(Keys.RETURN)
element.close()
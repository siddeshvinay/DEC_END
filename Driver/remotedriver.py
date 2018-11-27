from selenium import webdriver
import time

# driver=webdriver.Chrome()
#
# driver.get('https://www.w3.org/')
# for a in driver.find_elements_by_xpath('.//a'):
#     print(a.get_attribute('href'))

driver = webdriver.Chrome()
driver.get('http://imgur.com/')

images = driver.find_elements_by_tag_name('img')
for image in images:
    print(image.get_attribute('src'))

driver.close()
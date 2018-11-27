from selenium import webdriver
from  selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


oBrowser=webdriver.Chrome()
oBrowser.maximize_window()
oBrowser.get("https://network-rctp.qa.gtnexus.com/login.jsp")
sleep(2)
oBrowser.find_element_by_xpath("//input[@id='login']").send_keys("sp@gtnexus")
oBrowser.find_element_by_xpath("//input[@id='password']").send_keys("bfqFDIZWkv6st@")
sleep(2)
oBrowser.find_element_by_xpath("//input[@id='loginButton']").click()
sleep(2)
oBrowser.find_element_by_xpath(" //a[@id='navmenu__user']").click()
sleep(1)
oBrowser.find_element_by_xpath("//a[@id='navmenu__switch to gtn nh']").click()
sleep(2)
oBrowser.find_element_by_xpath("//input[@id='loginAsField-input']").send_keys("dhliscadmin")
sleep(2)
oBrowser.find_element_by_xpath("//*[@id='gtn_auto_19']/tbody/tr[2]/td[2]/em/button").click()
sleep(1)
oBrowser.find_element_by_xpath("//input[@id='customerSelector-input']").clear()
sleep(2)
oBrowser.find_element_by_xpath("//input[@id='customerSelector-input']").send_keys("Caterpillar Inc.")
sleep(1)
oBrowser.find_element_by_xpath("//div[@role='listitem']").click()
sleep(2)
oBrowser.find_element_by_xpath("//select[@class='qstext searchType']").click()
sleep(2)
sle=oBrowser.find_element_by_xpath("//select[@class='qstext searchType']")
all_opt=sle.find_elements_by_tag_name("option")
# for i in all_opt:
#     print("value is: %s" % i
# sleep(2)
opt=[]
select =Select(oBrowser.find_element_by_xpath("//select[@class='qstext searchType']"))
opt=select.options
for i in opt:
    if "Shipment Plans" in i.text:
        print("the shipment plan is preasent")
        select.select_by_visible_text("Shipment Plans")
        #select.select_by_value('15')

#Advance Searc
oBrowser.find_element_by_xpath("//a[@href='javascript:advancedSearch();']").click()

Customer_div=Select(oBrowser.find_element_by_xpath("//select[@name='custdivisions']"))
Customer_div.select_by_visible_text("CAT Containerized Material")
sleep(1)
Status=Select(oBrowser.find_element_by_xpath("//select[@name='status']"))
Status.select_by_visible_text("Planned")
sleep(1)
Exceptions=Select(oBrowser.find_element_by_xpath("//select[@name='exceptions']"))
Exceptions.select_by_visible_text("All Exceptions")
sleep(1)
Booking_Status=Select(oBrowser.find_element_by_xpath("//select[@name='bookingstatus']"))
Booking_Status.select_by_visible_text("Pending")
sleep(1)
Tender_Status=Select(oBrowser.find_element_by_xpath("//select[@name='tenderstatus']"))
Tender_Status.select_by_visible_text("All")
sleep(1)
ISF_Status=Select(oBrowser.find_element_by_xpath("//select[@name='isfstatus']"))
ISF_Status.select_by_visible_text("Accepted")
sleep(1)
#Select the Calendar button
oBrowser.find_element_by_xpath("//img[@class='x-form-trigger x-form-date-trigger']").click()

oBrowser.find_element_by_xpath("//table[@id='ext-comp-1008']/tbody/tr/td/em/button[@id='ext-gen124']").click()
sleep(1)
oBrowser.find_element_by_xpath("//div[@id='ext-gen117']/table/tbody/tr/td[@class='x-date-mp-month x-date-mp-sep']/a[text()='Oct']").click()


oBrowser.find_element_by_xpath("//div[@id='ext-gen117']/table/tbody/tr/td/button[@class='x-date-mp-ok']").click()

sleep(1)
oBrowser.find_element_by_xpath("//td[@class='x-date-active']/a[@class='x-date-date']/em/span[text()='3']").click()

sleep(1)
oBrowser.find_element_by_xpath("//input[@onclick='search(90);return false;']").click()
sleep(1)



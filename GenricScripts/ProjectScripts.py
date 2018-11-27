from selenium import webdriver
from selenium.webdriver.common.by import By
from DataTable import Datatable
from time import sleep
from selenium.webdriver.support.ui import Select
import os

oBrowser=webdriver.Chrome()

'''
launch Browser
'''
def launch(self):
    status ="False"
    Datatable.writeLog(" Launh the Chrome browser  " + Datatable.getDateTime(), "info")
    try:
        # oBrowser = webdriver.Chrome()
        sleep(1)
        oBrowser.maximize_window()
    except Exception as e:
        Datatable.writeLog("Unable to launch the Chrme browser  " + Datatable.getDateTime(), "Error")
        print("Unable to launch the Chrme browser")
    return status

''''
Navigate to URL
'''
def navigate(self):
    status ="False"
    Datatable.writeLog(" navigate to network env  " + Datatable.getDateTime(), "info")
    try:
        oBrowser.get(os.environ.get("URL")) #"https://network-rctp.qa.gtnexus.com/login.jsp")
    except Exception as e:
        Datatable.writeLog("Unale to navigate to network env" + Datatable.getDateTime(), "error")
        print("Unale to navigate to network env")
    return status

''''
Login with username and password
'''
def login(self):
    status ="False"
    Datatable.writeLog("Enter the valid username and valid passwor d" + Datatable.getDateTime(), "info")
    try:
        oBrowser.find_element_by_xpath("//input[@id='login']").send_keys(os.environ.get("UserName")) #"sp@gtnexus")
        sleep(1)
        oBrowser.find_element_by_xpath("//input[@id='password']").send_keys(os.environ.get("Password"))#"bfqFDIZWkv6st@")
        sleep(1)
        oBrowser.find_element_by_xpath("//input[@id='loginButton']").click()
        sleep(2)
        oBrowser.find_element_by_xpath(" //a[@id='navmenu__user']").click()
        sleep(1)

    except Exception as e:
        Datatable.writeLog("Unable to Enter the valid username and valid password  " + Datatable.getDateTime(), "error")
        print("unable to Enter the valid username and valid password")
    return status


''''
Switch to GTN
'''
def Switch_Gtn(self):
    status ="False"
    try:
        oBrowser.find_element_by_xpath("//a[@id='navmenu__switch to gtn nh']").click()
        sleep(2)
    except Exception as e:
        print("Unable to switch to GTN")
    return status

''''
Login as shadow user
'''
def ShadowUser(self):
    status="False"
    try:
        oBrowser.find_element_by_xpath("//input[@id='loginAsField-input']").send_keys(os.environ.get("ShadowUser"))#"dhliscadmin")
        sleep(2)
        oBrowser.find_element_by_xpath("//*[@id='gtn_auto_19']/tbody/tr[2]/td[2]/em/button").click()
        sleep(1)
    except Exception as e:
        print("Unable to login as shadow user")
    return status

''''
Select the Customer
'''
def SelectCustomer(self):
    status="False"
    try:
        oBrowser.find_element_by_xpath("//input[@id='customerSelector-input']").clear()
        sleep(2)
        oBrowser.find_element_by_xpath("//input[@id='customerSelector-input']").send_keys(os.environ.get("Customer"))#"Caterpillar Inc.")
        sleep(1)
        oBrowser.find_element_by_xpath("//div[@role='listitem']").click()
        sleep(1)
    except Exception as e:
        print("Unable to select the customer")


''''
Select the Module in Quick serach
'''
def QuickSearch(self):
    status="False"
    try:
        oBrowser.find_element_by_xpath("//select[@class='qstext searchType']").click()
        sleep(2)
        sle = oBrowser.find_element_by_xpath("//select[@class='qstext searchType']")
        all_opt = sle.find_elements_by_tag_name("option")
        # for i in all_opt:
        #     print("value is: %s" % i
        # sleep(2)
        opt = []
        select = Select(oBrowser.find_element_by_xpath("//select[@class='qstext searchType']"))
        opt = select.options
        for i in opt:
            if "Shipment Plans" in i.text:
                print("the shipment plan is preasent")
                select.select_by_visible_text(os.environ.get("QuickSearch")) #"Shipment Plans")
                # select.select_by_value('15')
        sleep(1)
        oBrowser.find_element_by_xpath("//a[@href='javascript:advancedSearch();']").click()
        sleep(1)

    except Exception as e:
        print("Unable to select in Shipment Plan in Quick search")


''''
Enter the requried details in Advance Search Page
'''
def EnterDetails_AdvanceSearch(self):
    status="False"
    try:
        #oBrowser.find_element_by_xpath("//a[@href='javascript:advancedSearch();']").click()

        Customer_div = Select(oBrowser.find_element_by_xpath("//select[@name='custdivisions']"))
        custdiv=os.environ.get("Custome_Divisions")
        #print(custdiv)
        Customer_div.select_by_visible_text(custdiv)#"CAT Containerized Material")
        sleep(1)
        Status = Select(oBrowser.find_element_by_xpath("//select[@name='status']"))
        sta=Status.select_by_visible_text(os.environ.get("Status"))#"Planned")
        print(sta)
        sleep(1)
        Exceptions = Select(oBrowser.find_element_by_xpath("//select[@name='exceptions']"))
        exc=Exceptions.select_by_visible_text(os.environ.get("Exceptions"))#"All Exceptions")
        print(exc)
        sleep(1)
        Booking_Status = Select(oBrowser.find_element_by_xpath("//select[@name='bookingstatus']"))
        Bk_st=Booking_Status.select_by_visible_text(os.environ.get("Booking_Status"))#"Pending")
        print(Bk_st)
        sleep(1)
        Tender_Status = Select(oBrowser.find_element_by_xpath("//select[@name='tenderstatus']"))
        TS=Tender_Status.select_by_visible_text(os.environ.get("Tender_Status"))#"All")
        print(TS)
        sleep(1)
        ISF_Status = Select(oBrowser.find_element_by_xpath("//select[@name='isfstatus']"))
        ISF_ST=ISF_Status.select_by_visible_text(os.environ.get("ISF_Status"))#"Accepted")
        print(ISF_ST)
        sleep(1)
    except Exception as e:
        print("enter the Advance Search Details")


''''
Select the Date in Advance Search page
'''
def AdvanceSearch_calendar(self):
    status="False"
    try:
        # Select the Calendar button
        oBrowser.find_element_by_xpath("//img[@class='x-form-trigger x-form-date-trigger']").click()

        oBrowser.find_element_by_xpath("//table[@id='ext-comp-1008']/tbody/tr/td/em/button[@id='ext-gen124']").click()
        sleep(1)
        oBrowser.find_element_by_xpath(
            "//div[@id='ext-gen117']/table/tbody/tr/td[@class='x-date-mp-month x-date-mp-sep']/a[text()='Oct']").click()

        oBrowser.find_element_by_xpath(
            "//div[@id='ext-gen117']/table/tbody/tr/td/button[@class='x-date-mp-ok']").click()

        sleep(1)
        oBrowser.find_element_by_xpath(
            "//td[@class='x-date-active']/a[@class='x-date-date']/em/span[text()='3']").click()

        sleep(1)
    except Exception as e:
        print("unable to select the date in Calendar")


''''
Click on serach button in Advance search page
'''
def Click_Search_AS(self):
    status="False"
    try:
        #Click on Search Button in Advance search page"
        oBrowser.find_element_by_xpath("//input[@onclick='search(90);return false;']").click()
        sleep(1)
    except Exception as e:
        print("Unable to click on Click on Search Button in Advance search page")









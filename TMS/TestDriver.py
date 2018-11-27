from GenricScripts import ProjectScripts
#from GenricScripts import TestCase
from DataTable import Datatable
import os
from time import sleep


def TestCase1(self):
    ProjectScripts.launch(self)
    ProjectScripts.navigate(self)
    ProjectScripts.login(self)
    ProjectScripts.Switch_Gtn(self)
    sleep(1)
    ProjectScripts.ShadowUser(self)
    ProjectScripts.SelectCustomer(self)
    ProjectScripts.QuickSearch(self)
    ProjectScripts.EnterDetails_AdvanceSearch(self)
    ProjectScripts.AdvanceSearch_calendar(self)
    ProjectScripts.Click_Search_AS(self)
    # Testcases.


def fetchdata(filename, sheetname):
    rc = Datatable.getRowcount(filename, sheetname)
    cc = Datatable.getColumnCount(filename, sheetname)
    print(rc)
    print(cc)
    return rc, cc


def cellData(filename, Sheetname, ColName, RowNum):
    data = Datatable.getCelldata(filename, Sheetname, ColName, RowNum)
    print(data)
    return data


def LoadOS(Filename, SheetName):
    Datatable.loadOSenvVariables(Filename, SheetName)


def TestCase2(self):
    ProjectScripts.launch(self)
    ProjectScripts.navigate(self)
    ProjectScripts.login(self)
    ProjectScripts.Switch_Gtn(self)
    sleep(1)










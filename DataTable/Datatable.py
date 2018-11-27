from xlrd import sheet
from xlrd import open_workbook
from xlrd import *
import logging
import datetime
import os
import xlrd


def getRowcount(FileName, Sheetname):
    rc=0
    try:
        wb=xlrd.open_workbook(FileName)
        sheet=wb.sheet_by_name(Sheetname)
        rc=sheet.nrows
        return rc
    except Exception as e:
        print("unble to find the work book")

def getColumnCount(FileName, Sheetname):
    cc=0
    try:
        wb=xlrd.open_workbook(FileName)
        sheet=wb.sheet_by_name(Sheetname)
        cc=sheet.ncols
        return cc
    except Exception as e:
        print("unable to the get the column count")


def getCelldata(FileName, Sheetname,ColName, RowNum):
    ColNum=0
    try:
        wb=xlrd.open_workbook(FileName)
        sheet=wb.sheet_by_name(Sheetname)

        firstRow=sheet.row_values(0)
        for data in firstRow:
            if data==ColName:
                break
            ColNum+=1

        celldata=sheet.cell_value(RowNum,ColNum)
        return celldata
    except Exception as e:
        print("unabel to fetch the data from the cell")


def loadOSenvVariables(FileName,Sheetname):
    try:
        wb=xlrd.open_workbook(FileName)
        sheet=wb.sheet_by_name(Sheetname)

        ColoumnNames=sheet.row_values(0)
        ColoumnValues=sheet.row_values(1)

        for i in range(len(ColoumnNames)):
            os.environ[ColoumnNames[i]]=str(ColoumnValues[i])
    except Exception as e:
        print("Enter valid Filename and sheetName")


# '''
# Write the Log error
# '''
# def writelog(message, loglevel):
def getDateTime():
    strDate=datetime.datetime.now()
    return str(strDate)


def writeLog(message, loglevel):
    if(loglevel.lower()=="info"):
        logging.basicConfig(filename='C:/Users/sjanagonnavar/PycharmProjects/MYFW/logs/AutomationLogs.log',level=logging.INFO)
        logging.info(message)
    elif(loglevel.lower()=="error"):
        logging.basicConfig(filename='C:/Users/sjanagonnavar/PycharmProjects/MYFW/logs/AutomationLogs.log',level=logging.ERROR)
        logging.error(message)
    elif(loglevel.lower=="debug"):
        logging.basicConfig(filename='C:/Users/sjanagonnavar/PycharmProjects/MYFW/logs/AutomationLogs.log',level=logging.WARNING)
        logging.warning(message)
    else:
        logging.error("Invalid log level message !!!!!!!!!")









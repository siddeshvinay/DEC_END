from selenium import webdriver
from TMS import TestDriver
from DataTable import Datatable
import unittest
import os


class DriverScript(unittest.TestCase):

    def setUp(self):
        pass

    def testDriver(self):
        try:
            ControllerFileName="C:/Users/sjanagonnavar/PycharmProjects/MYFW/Controller_XLsheets/data_Controller.xlsx"
            rc=Datatable.getRowcount(ControllerFileName,"Scenarios")
            print("unable to get the TestFile")
            for r in range(rc):
                testcaseID=Datatable.getCelldata(ControllerFileName,"Scenarios","TestcaseID", r)
                testcaseName = Datatable.getCelldata(ControllerFileName, "Scenarios", "TestcaseName", r)
                testDesc = Datatable.getCelldata(ControllerFileName, "Scenarios", "Description", r)
                runStatus = Datatable.getCelldata(ControllerFileName, "Scenarios", "RunStatus", r)

                # print("testcaseID  :",+testcaseID)
                # print("testcaseName  :", +testcaseName)
                # print("testDesc  :", +testDesc)
                # print("runStatus  :", +runStatus)
                if(runStatus.lower()=='yes'):
                    testfileName=testcaseName+".xlsx"
                    testScenaioFile="C:/Users/sjanagonnavar/PycharmProjects/MYFW/DataSheets/"+testfileName
                    print(testScenaioFile)
                    print(testcaseID)

                    scenarioRowcount=Datatable.getRowcount(testScenaioFile,testcaseID)
                    print(scenarioRowcount)

                    methods=[]
                    listtestscriptid=[]
                    listtestdesc=[]
                    lisstatus=[]
                    for tsid in range(scenarioRowcount-1):
                        testscriptid=Datatable.getCelldata(testScenaioFile,testcaseID,"TestScriptID",tsid+1)
                        tsdescription = Datatable.getCelldata(testScenaioFile, testcaseID, "Description", tsid + 1)
                        tsmethodname = Datatable.getCelldata(testScenaioFile, testcaseID, "MethodName", tsid + 1)

                        # print("testscripid  :",+testscriptid)
                        # print("testdescription  :", +tsdescription)
                        # print("tsmethod  :", +tsmethodname)


                        listtestscriptid.append(testscriptid)
                        listtestdesc.append(tsdescription)
                        methods.append(tsmethodname)

                    Datatable.loadOSenvVariables(testScenaioFile,"testdata")
                    print(methods)

                    for method in methods:
                        resultstatus=eval(method)
                        lisstatus.append(resultstatus)
                        if (resultstatus=='Fail'):
                            pass
                        else:
                            lisstatus.append("")


            te = TestDriver.TestCase1()
            te.LoadOS("C:/Users/sjanagonnavar/PycharmProjects/MYFW/DataSheets/TC1.xlsx","TC1")
            te.tes("True")
        except Exception as e:
            print("unable to run the framework")

    def tearDown(self):
        try:
            os.environ.clear()

        except Exception as e:
            print("This error is raised during Treadown")


if __name__=='__main__':
    unittest.main()





import time

import pytest

from Utilities import XLutiles
from Utilities.readProperties import ReadConfigFile
from pageObjects.Login_Page import Login_Class
from pageObjects.Search_User_Page import Search_User_Class


class Test_Search_User_Excel:
    Username = ReadConfigFile.GetUsername()
    Password = ReadConfigFile.GetPassword()
    Excel_file_Path = ".\\testCases\\Test_Data\\Test_Data.xlsx"

    @pytest.mark.regression
    @pytest.mark.group2
    def test_search_user_Excel_006(self, setup):
        self.driver = setup
        self.lp = Login_Class(self.driver)
        self.lp.Click_Login_Link()
        self.lp.Enter_Username(self.Username)
        self.lp.Enter_Password(self.Password)
        self.lp.Click_Login_Button()
        # time.sleep(5)
        self.su = Search_User_Class(self.driver)
        self.su.Click_Link_User_Management()
        self.row_count = XLutiles.RowCount(self.Excel_file_Path, "SearchUser")
        print("row_count-->" + str(self.row_count))
        Status_List = []
        for r in range (2, self.row_count+1):
            self.Search_Username = XLutiles.ReadData(self.Excel_file_Path, "SearchUser", r, 2)
            self.ExpectedResult = XLutiles.ReadData(self.Excel_file_Path, "SearchUser", r, 3)
            self.su.Click_Link_User_Management()

            self.su.Enter_UserName(self.Search_Username)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # time.sleep(5)
            self.su.Click_Search_User_Button()
            time.sleep(5)
            if self.su.Validate_Search_User() == "pass" and self.ExpectedResult == "pass":
                self.actual_result = XLutiles.ReadData(self.Excel_file_Path, "SearchUser", r, 4, "pass")
                Status = XLutiles.ReadData(self.Excel_file_Path, "SearchUser", r, 5, "pass")
                Status_List.append("pass")
                # assert True
            elif self.su.Validate_Search_User() == "pass" and self.ExpectedResult == "fail":
                actual_result = XLutiles.ReadData(self.Excel_file_Path, "SearchUser", r, 4, "pass")
                Status = XLutiles.ReadData(self.Excel_file_Path, "SearchUser", r, 5, "fail")
                Status_List.append("fail")
                # assert False
            elif self.su.Validate_Search_User() == "fail" and self.ExpectedResult == "pass":
                actual_result = XLutiles.ReadData(self.Excel_file_Path, "SearchUser", r, 4, "fail")
                Status = XLutiles.ReadData(self.Excel_file_Path, "SearchUser", r, 4, "fail")
                Status_List.append("fail")
                # assert False
            elif self.su.Validate_Search_User() == "fail" and self.ExpectedResult == "fail":
                actual_result = XLutiles.ReadData(self.Excel_file_Path, "SearchUser", r, 4, "fail")
                Status = XLutiles.ReadData(self.Excel_file_Path, "SearchUser", r, 4, "pass")
                Status_List.append("pass")
                # assert True
        print(Status_List)

        if "fail" not in Status_List:
            assert True
        else:
            assert False


# pytest -v -s -k "test_search_user_Excel_006" --browser firefox




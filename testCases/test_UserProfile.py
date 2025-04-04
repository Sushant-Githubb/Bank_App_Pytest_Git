import time

import allure
import pytest
from allure_commons.types import AttachmentType

from Utilities.Logger import Log_Class
from Utilities.readProperties import ReadConfigFile
from pageObjects.Login_Page import Login_Class
from pageObjects.SignUp_Page import SignUp_Class


class Test_UserProfile:
    Username = ReadConfigFile.GetUsername()
    Password = ReadConfigFile.GetPassword()
    Log = Log_Class.log_generator()

    @pytest.mark.sanity
    @pytest.mark.group1
    @allure.title("BankApp url testing 01")
    def test_BankApp_Url_001(self, setup):
        """self.Log.debug("This is debug")
        self.Log.info("This is info")
        self.Log.warning("This is warning")
        self.Log.error("This is error")
        self.Log.critical("This is critical")"""

        self.Log.info("Testcase test_BankApp_Url_001 is started")
        self.driver = setup
        self.Log.info("Opening browser")
        self.Log.info("Checking page title")
        if self.driver.title == "Bank Application":
            self.Log.info("Testcase test_BankApp_Url_001 is passed")
            self.Log.info("Taking screenshot")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_BankApp_Url_001_pass", attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot(".\\Screeshots\\test_BankApp_Url_001_pass.png")
            self.Log.info("Testcase test_BankApp_Url_001 is completed\n")
            assert True
        else:
            self.Log.info("Testcase test_BankApp_Url_001 is fail")
            self.Log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screeshots\\test_BankApp_Url_001_fail.png")
            self.Log.info("Testcase test_BankApp_Url_001 is completed\n")
            assert False

    @pytest.mark.sanity
    @pytest.mark.group1
    def test_Signup_002(self, setup):
        self.Log.info("Testcase test_Signup_002 is started")
        self.driver = setup
        self.Log.info("Opening browser")
        self.su = SignUp_Class(self.driver)
        self.su.Click_Signup()
        self.Log.info("Entering the Username")
        self.su.Enter_Username("Demo555")
        self.Log.info("Entering the Password")
        self.su.Enter_Password("Demo555@")
        self.Log.info("Entering the Email")
        self.su.Enter_Email("Demo555@credence.in")
        self.Log.info("Entering the Phone")
        self.su.Enter_Phone("7656765456")
        self.Log.info("Click on Create user button")
        self.su.Click_CreateUser_Button()
        self.Log.info("Checking user creation")
        if self.su.Validate_User_Creation() == "User created successfully":
            self.Log.info("Testcase test_Signup_002 is passed")
            self.Log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screeshots\\test_Signup_002_pass.png")
            self.Log.info("Testcase test_Signup_002 is completed\n")
            assert True
        else:
            self.Log.info("Testcase test_Signup_002 is fail")
            self.Log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screeshots\\test_Signup_002_fail.png")
            self.Log.info("Testcase test_Signup_002 is completed\n")
            assert False

    @pytest.mark.sanity
    @pytest.mark.group2
    def test_Login_003(self, setup):
        self.Log.info("Testcase test_Login_003 is started")
        self.driver = setup
        self.Log.info("Opening browser")
        self.lp = Login_Class(self.driver)
        self.Log.info("Click on Login link")
        self.lp.Click_Login_Link()
        self.Log.info("Entering the username")
        self.lp.Enter_Username(self.Username)
        self.Log.info("Entering the password")
        self.lp.Enter_Password(self.Password)
        self.Log.info("Click on login button")
        self.lp.Click_Login_Button()
        self.Log.info("Checking the page title")
        if self.driver.title == "Dashboard":
            self.Log.info("Testcase test_Login_003 is passed")
            self.Log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screeshots\\test_Login_003_pass.png")
            self.Log.info("Testcase test_Login_003 is completed\n")
            assert True

        else:
            self.Log.info("Testcase test_Login_003 is failed")
            self.Log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screeshots\\test_Login_003_fail.png")
            self.Log.info("Testcase test_Login_003 is completed\n")
            assert False

# Allure report image attach
# Full page screenshot
# Allure decorators
# Random username, email, phone number for signup write python program for this and give the data to signup testcase
# pytest -v -s -n=3 -m "sanity and group1" --html=HTMLReports/myreport_chrome.html --browser chrome --alluredir="Allure-results" -p no:warnings

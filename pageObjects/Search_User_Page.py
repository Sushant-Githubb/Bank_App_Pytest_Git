from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Search_User_Class:
    click_user_management_link_xpath = "//a[normalize-space()='User Management']"  #//a[normalize-space()='User Management']
    text_username_xpath = "//input[@id='username']"
    click_search_user_button_xpath = "//button[@type='submit']"
    validate_search_user_page_title_css_selector = "div[class='container'] h2"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def Click_Link_User_Management(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.click_user_management_link_xpath))
        self.driver.find_element(By.XPATH, self.click_user_management_link_xpath).click()

    def Enter_UserName(self, username):
        self.wait.until(expected_conditions.visibility_of_element_located(self.text_username_xpath))
        self.driver.find_element(By.XPATH, self.text_username_xpath).send_keys(username)

    def Click_Search_User_Button(self):
        self.driver.find_element(By.XPATH, self.click_search_user_button_xpath).click()

    def Validate_Search_User(self):
        title = self.driver.find_element(By.CSS_SELECTOR, self.validate_search_user_page_title_css_selector).text
        if title == "Edit User":
            return "pass"
        else:
            return "fail"




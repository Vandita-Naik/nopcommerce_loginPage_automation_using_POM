from locators.locators import Locators
class LoginPage():

    def __init__(self,driver):
        self.driver=driver
        self.textBox_username_id=Locators.textBox_username_id
        self.textBox_password_id=Locators.textBox_password_id
        self.button_xpath=Locators.button_xpath
        self.logout_btton_linkText=Locators.logout_btton_linkText

    def enter_username(self,username):
        self.driver.find_element_by_id(Locators.textBox_username_id).clear()
        self.driver.find_element_by_id(Locators.textBox_username_id).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element_by_id(Locators.textBox_password_id).clear()
        self.driver.find_element_by_id(Locators.textBox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(Locators.button_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(Locators.logout_btton_linkText).click()






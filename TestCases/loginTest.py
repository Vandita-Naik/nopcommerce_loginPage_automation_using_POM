import time
import HtmlTestRunner
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..",".."))
from PageObjects.LoginPage import LoginPage

class Test_login(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome(executable_path="C:/Users/vandi/PycharmProjects/python imp files/PomProject/pom3/driver/chromedriver.exe")
        self.driver.get("https://admin-demo.nopcommerce.com/")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        print("title is: ", self.driver.title)
        self.assertEqual("Your store. Login", self.driver.title, "title is not same")

    def test_login(self):
        lp=LoginPage(self.driver)
        lp.enter_username("admin@yourstore.com")
        lp.enter_password("admin")
        time.sleep(5)
        lp.click_login()
        time.sleep(3)
        lp.click_logout()


    def tearDown(self):
        print("test completed")
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\vandi\\PycharmProjects\\python imp files\\PomProject\\pom3\\Reports"))











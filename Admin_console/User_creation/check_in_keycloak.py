import time
import unittest

from Data.parameters import Data
from get_dir import pwd
from reuse_func import GetData


class keycloak(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.p = pwd()
        self.driver = self.data.get_driver()
        self.driver.implicitly_wait(30)
        self.driver.get('https://cqube.tibilprojects.com/auth/admin')
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id('username').send_keys('admin')
        self.driver.find_element_by_id('password').send_keys('tibil123')
        self.driver.find_element_by_id(Data.login).click()
        self.data.page_loading(self.driver)

    def test_user_tables(self):

        self.driver.find_element_by_xpath("//*[@id='view']/div[2]/div[3]/ul/li[2]/a").click()
        count = 0
        self.driver.find_element_by_id("viewAllUsers").click()
        time.sleep(3)
        if "Users" in self.driver.page_source:
            print("Users page is displayed")
        else:
            print("Users page is not exist")
            count = count + 1
        self.assertEqual(count, 0, msg="User page is not exists")
        if "qateam1" not in self.driver.page_source:
            print("Admin user is not  present ")
            count = count + 1
        if "qa2" not in self.driver.page_source:
            print("report viewer is not present")
            count  = count + 1
        if "qa3" not in self.driver.page_source:
            print("emission user is not present ")
            count = count + 1
        self.assertEqual(0,count,msg="Some user is not present in keycloak table")
        self.data.page_loading(self.driver)

    @classmethod
    def tearDown(self):
        self.driver.close()
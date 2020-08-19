import time
import unittest

from keycloak_funcs import keyData


class user_options(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = keyData()
        self.driver = self.data.get_driver()
        self.data.open_keycloack(self.driver)
        self.data.login_keycloack(self.driver)
        self.driver.find_element_by_xpath("//*[@id='view']/div[2]/div[3]/ul/li[2]/a").click()
        self.f = open(self.data.get_json_file_path(), "r")

    def test_users(self):
        count = 0
        self.driver.find_element_by_id("viewAllUsers").click()
        if "Users" in self.driver.page_source:
            print("Users page is displayed")
        else:
            print("Users page is not exist")
            count = count + 1
        self.assertEqual(count,0,msg="User page is not exists")

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.close()
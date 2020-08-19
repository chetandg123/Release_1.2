import json
import time
import unittest

from selenium.webdriver.support.select import Select

from keycloak_funcs import keyData


class roles_options(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = keyData()
        self.driver = self.data.get_driver()
        self.data.open_keycloack(self.driver)
        self.data.login_keycloack(self.driver)
        self.driver.find_element_by_xpath("//*[@id='view']/div[2]/div[2]/ul/li[4]/a").click()
        self.f = open(self.data.get_json_file_path(), "r")
        self.file = json.loads(self.f.read())

    def test_admin(self):
        count = 0
        self.driver.find_element_by_id("viewAllRoles").click()
        cqube_admin = self.driver.find_element_by_xpath("//a[contains(text(),'admin')]").text
        self.assertEqual(cqube_admin,self.file['roles']['realm'][2]['name'],msg="admin  is not present")
        if "admin" in self.driver.page_source:
            print("admin  is present in client table")
        else:
            print("admin is not present in client table")
            count = count + 1
        self.assertEqual(0,count,msg="admin is not present")

    def test_emission(self):
        count = 0
        self.driver.find_element_by_id("viewAllRoles").click()
        cqube_admin = self.driver.find_element_by_xpath("//a[contains(text(),'emission')]").text
        self.assertEqual(cqube_admin,self.file['roles']['realm'][0]['name'],msg="admin  is not present")
        if "emission" in self.driver.page_source:
            print("emission  is present in client table")
        else:
            print("emission is not present in client table")
            count = count + 1
        self.assertEqual(0,count,msg="emission is not present")


    def test_report_viewer(self):
        count = 0
        self.driver.find_element_by_id("viewAllRoles").click()
        cqube_admin = self.driver.find_element_by_xpath("//a[contains(text(),'report_viewer')]").text
        self.assertEqual(cqube_admin,self.file['roles']['realm'][1]['name'],msg="admin  is not present")
        if "report_viewer" in self.driver.page_source:
            print("report_viewer  is present in client table")
        else:
            print("report_viewer is not present in client table")
            count = count + 1
        self.assertEqual(0,count,msg="report_viewer is not present")

    def test_default_role(self):
        self.driver.find_element_by_xpath("//*[@id='view']/div[1]/ul/li[2]/a").click()
        roles =Select(self.driver.find_element_by_id("available"))
        for i in range(len(roles.options)):
            print(roles.options[i].text)
        if len(roles.options) == 3:
            print("All roles are present in Available box ")
        else:
            print("All roles are not present in Available box")
        self.driver.find_element_by_xpath("//*[@id='view']/div[1]/ul/li[1]/a").click()

    def test_click_on_admin(self):
        self.driver.find_element_by_id("viewAllRoles").click()
        self.driver.find_element_by_xpath("//a[contains(text(),'admin')]").click()
        rolename = self.driver.find_element_by_id("name").get_attribute('value')
        self.assertEqual(self.file['roles']['realm'][2]['name'],rolename,msg="role name is mismatching")
        description = self.driver.find_element_by_id("description").get_attribute("value")
        print(description)
        self.assertEqual(self.file['roles']['realm'][2]['description'],description,msg="Mis matched discription ")
        status = self.driver.find_element_by_xpath("//*[@id='view']/div[1]/form/fieldset[1]/div[3]/div/span/div/label/span[1]/span[2]").text
        print("Composite role :",status)
        self.assertEqual("OFF", status, msg="Composite roles is in ON state!")
        self.driver.find_element_by_xpath("//*[@id='view']/div[1]/ol/li[1]/a").click()

    def test_click_on_emission(self):
        self.driver.find_element_by_id("viewAllRoles").click()
        self.driver.find_element_by_xpath("//a[contains(text(),'emission')]").click()
        rolename = self.driver.find_element_by_id("name").get_attribute('value')
        self.assertEqual(self.file['roles']['realm'][0]['name'],rolename,msg="role name is mismatching")
        description = self.driver.find_element_by_id("description").get_attribute("value")
        print(description)
        self.assertEqual(self.file['roles']['realm'][0]['description'],description,msg="Mis matched discription ")
        status = self.driver.find_element_by_xpath("//*[@id='view']/div[1]/form/fieldset[1]/div[3]/div/span/div/label/span[1]/span[2]").text
        print("Composite role :",status)
        self.assertEqual("OFF", status, msg="Composite roles is in ON state!")
        self.driver.find_element_by_xpath("//*[@id='view']/div[1]/ol/li[1]/a").click()

    def test_click_on_reportviewer(self):
        self.driver.find_element_by_id("viewAllRoles").click()
        self.driver.find_element_by_xpath("//a[contains(text(),'report_viewer')]").click()
        rolename = self.driver.find_element_by_id("name").get_attribute('value')
        self.assertEqual(self.file['roles']['realm'][1]['name'],rolename,msg="role name is mismatching")
        description = self.driver.find_element_by_id("description").get_attribute("value")
        self.assertEqual(self.file['roles']['realm'][1]['description'],description,msg="Mis matched discription ")
        status = self.driver.find_element_by_xpath("//*[@id='view']/div[1]/form/fieldset[1]/div[3]/div/span/div/label/span[1]/span[2]").text
        print("Composite role :",status)
        self.assertEqual("OFF", status, msg="Composite roles is in ON state!")
        self.driver.find_element_by_xpath("//*[@id='view']/div[1]/ol/li[1]/a").click()


    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.close()
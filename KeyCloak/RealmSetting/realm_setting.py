import json
import time
import unittest

from keycloak_funcs import keyData


class realm_settings(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.data = keyData()
        self.driver = self.data.get_driver()
        self.data.open_keycloack(self.driver)
        self.data.login_keycloack(self.driver)
        self.driver.find_element_by_xpath("//*[@id='view']/div[2]/div[2]/ul/li[1]/a").click()
        self.f = open(self.data.get_json_file_path(), "r")
        self.file = json.loads(self.f.read())

    def test_general(self):
        self.driver.find_element_by_xpath("//*[@id='view']/div[1]/div/ul/li[1]/a").click()
        if "cQube" in self.driver.page_source:
            print("realmsetting page is present on screen")
        else:
            print("realmsetting page is not exists")
        name = self.driver.find_element_by_id("name").get_attribute('value')

        self.assertEqual(self.file['id'],name,msg="Name attribute is change")
        val = self.driver.find_element_by_xpath("//*[@id='view']/div[1]/form/div[6]/div/span/div/label/span[1]/span[1]").text
        self.assertEqual("ON",val,msg="Mismatch found")

    def test_login(self):
        self.driver.find_element_by_xpath("//*[@id='view']/div[1]/div/ul/li[2]/a").click()
        val = self.driver.find_element_by_xpath("//*[@id='view']/div[1]/form/fieldset/div[7]/div/span/div/label/span[1]/span[1]").text
        self.assertEqual("ON", val, msg="Mismatch found")
        ssl = self.driver.find_element_by_xpath("//*[@id='sslRequired']/option[2]")
        len = ssl.is_selected()
        self.assertTrue(len,msg="External request is not selected")

    def test_tokens(self):
        self.driver.find_element_by_xpath("//a[contains(text(),'Tokens')]").click()
        off = self.driver.find_element_by_xpath("//*[@id='view']/div[1]/form/div[2]/div/span/div/label/span[1]/span[2]").text
        self.assertEqual("OFF",off,msg="Revoke Refresh Token is ON mode")

        accessTokenLifespan = self.driver.find_element_by_id("accessTokenLifespan").get_attribute('value')
        time = self.file['accessTokenLifespan'] / 60
        self.assertEqual(int(accessTokenLifespan),int(time),msg="timing is mismatch found at accessTokenLifespan")

        accessTokenLifespanForImplicitFlow = self.driver.find_element_by_id("accessTokenLifespanForImplicitFlow").get_attribute('value')
        time =self.file['accessTokenLifespanForImplicitFlow'] / 60
        self.assertEqual(int(accessTokenLifespanForImplicitFlow),int(time),msg="mismatch found at accessTokenLifespanForImplicitFlow timings")

        ssoSessionIdleTimeout = self.driver.find_element_by_id("ssoSessionIdleTimeout").get_attribute('value')
        time =self.file['ssoSessionIdleTimeout'] / 60
        self.assertEqual(int(ssoSessionIdleTimeout),int(time),msg="timing miss match found at ssoSessionIdleTimeout")

        ssoSessionMaxLifespan = self.driver.find_element_by_id("ssoSessionMaxLifespan").get_attribute('value')
        time = int(self.file['ssoSessionMaxLifespan'] / 60 /60)
        self.assertEqual(time, int(ssoSessionMaxLifespan), msg="timing miss match found at ssoSessionMaxLifespan")

        ssoSessionIdleTimeoutRememberMe = self.driver.find_element_by_id("ssoSessionIdleTimeoutRememberMe").get_attribute('value')
        time = int(self.file['ssoSessionIdleTimeoutRememberMe'])
        self.assertEqual(time, int(ssoSessionIdleTimeoutRememberMe), msg="timing miss match found at ssoSessionIdleTimeoutRememberMe")

        ssoSessionMaxLifespanRememberMe = self.driver.find_element_by_id("ssoSessionMaxLifespanRememberMe").get_attribute('value')
        time = int(self.file['ssoSessionMaxLifespanRememberMe'])
        self.assertEqual(time, int(ssoSessionMaxLifespanRememberMe), msg="timing miss match found at ssoSessionMaxLifespanRememberMe")

        offlineSessionIdleTimeout = self.driver.find_element_by_id("offlineSessionIdleTimeout").get_attribute('value')
        time = int(self.file['offlineSessionIdleTimeout'] /86400)
        self.assertEqual(time, int(offlineSessionIdleTimeout),msg="timing miss match found at offlineSessionIdleTimeout")

        accessCodeLifespan = self.driver.find_element_by_id("accessCodeLifespan").get_attribute("value")
        time = int(self.file['accessCodeLifespan'] / 60)
        self.assertEqual(time, int(accessCodeLifespan),msg="timing miss match found at accessCodeLifespan")


        accessCodeLifespanUserAction = self.driver.find_element_by_id("accessCodeLifespanUserAction").get_attribute("value")
        time = int(self.file['accessCodeLifespanUserAction'] / 60)
        self.assertEqual(time, int(accessCodeLifespanUserAction), msg="timing miss match found at accessCodeLifespanUserAction")

        accessCodeLifespanLogin = self.driver.find_element_by_id("accessCodeLifespanLogin").get_attribute("value")
        time = int(self.file['accessCodeLifespanLogin'] / 60)
        self.assertEqual(time, int(accessCodeLifespanLogin),msg="timing miss match found at accessCodeLifespanLogin")

        actionTokenGeneratedByAdminLifespan = self.driver.find_element_by_id("actionTokenGeneratedByAdminLifespan").get_attribute("value")
        time = int(self.file['actionTokenGeneratedByAdminLifespan'] / 60 /60)
        self.assertEqual(time, int(actionTokenGeneratedByAdminLifespan), msg="timing miss match found at actionTokenGeneratedByAdminLifespan")

        actionTokenGeneratedByUserLifespan = self.driver.find_element_by_id("actionTokenGeneratedByUserLifespan").get_attribute("value")
        time = int(self.file['actionTokenGeneratedByUserLifespan'] / 60)
        self.assertEqual(time, int(actionTokenGeneratedByUserLifespan), msg="timing miss match found at actionTokenGeneratedByUserLifespan")

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.close()

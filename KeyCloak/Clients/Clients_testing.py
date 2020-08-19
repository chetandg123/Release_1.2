import json
import time
import unittest

from KeyCloak.Clients.check_base_url_with_private_ip_and_domain_name import CheckBaseUrl
from KeyCloak.Clients.check_clientid_with_json_file import ClientID
from KeyCloak.Clients.check_cqube_admin_client_scopes_assigned_default import CqubeAdminDefaultScopes
from KeyCloak.Clients.check_cqube_admin_client_scopes_assigned_optional import CqubeAdminOptionalScopes
from KeyCloak.Clients.check_cqube_admin_settings import CqubeAdminSetting
from KeyCloak.Clients.check_cqube_app_client_scopes_assigned_default import CqubeAppDefaultScopes
from KeyCloak.Clients.check_cqube_app_client_scopes_assigned_optional import CqubeAppOptionalScopes
from KeyCloak.Clients.check_cqube_app_settings import CqubeAppSetting
from KeyCloak.Clients.check_cqube_flask_client_scopes_assigned_default import CqubeFlaskDefaultScopes
from KeyCloak.Clients.check_cqube_flask_client_scopes_assigned_optional import CqubeFlaskOptionalScopes
from KeyCloak.Clients.check_cqube_flask_settings import CqubeFlaskSetting
from KeyCloak.Clients.check_enabled_with_json_file import Enabled
from keycloak_funcs import keyData
from reuse_func import GetData


class Clients(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = keyData()
        self.file =self.data.open_json_file()
        self.driver = self.data.get_driver()
        self.data.open_keycloack(self.driver)
        self.data.login_keycloack(self.driver)
        time.sleep(2)
        # self.driver.navigate_to_clients(self.driver)
        self.driver.find_element_by_xpath("//*[@id='view']/div[2]/div[2]/ul/li[2]/a").click()
        time.sleep(3)



    def test_base_url_with_private_ip_and_domain_name(self):
        cal = CheckBaseUrl(self.driver, self.file)
        json_baseurl, url = cal.check_BaseUrl_with_domain_name_and_privateip()
        self.assertEqual(json_baseurl, url, msg="urls is mismatched")

    def test_clients(self):
        cal = ClientID(self.driver, self.file)
        json_client_id, table_client_id = cal.check_clienid()
        self.assertEqual(json_client_id, table_client_id, msg="json_client_id is not equal to table_client_id")

    def test_enabled(self):
        data = keyData()
        data.navigate_to_clients(self.driver)
        time.sleep(2)
        cal = Enabled(self.driver, self.file)

        json_enabled, table_enabled = cal.check_enabled()
        self.assertEqual(json_enabled, table_enabled, msg="json_enabled is not equal to table_enabled")

    # def test_BaseUrl(self):
    #     cal = BaseUrl(self.driver, self.file)
    #     json_baseurl, table_baseurl = cal.check_BaseUrl()
    #     self.assertEqual(json_baseurl, table_baseurl, msg="json_baseurl is not equal to table_baseurl")

    def test_cqube_admin(self):
        cal = CqubeAdminSetting(self.driver, self.file)
        json_cqube_admin_client, keycloack_cqube_admin_client = cal.check_cqube_admin_setting()
        self.assertEqual(json_cqube_admin_client, keycloack_cqube_admin_client,
                         msg="Json parameters and keycloack parameters are not matching")

    def test_cqube_admin_default_scopes(self):
        cal = CqubeAdminDefaultScopes(self.driver, self.file)
        jason_defaultClientScopes, keycloack_assigned_default_client_scopes = cal.check_cqube_admin_default_scopes()
        self.assertEqual(jason_defaultClientScopes, keycloack_assigned_default_client_scopes,
                         msg="Json parameters and keycloack parameters are not matching")

    def test_cqube_admin_optional_scopes(self):
        cal = CqubeAdminOptionalScopes(self.driver, self.file)
        json_assigned_ClientScopes, keycloack_assigned_optional_client_scopes = cal.check_cqube_admin_optional_scopes()
        self.assertEqual(json_assigned_ClientScopes, keycloack_assigned_optional_client_scopes,
                         msg="Json parameters and keycloack parameters are not matching")

    def test_cqube_app(self):
        cal = CqubeAppSetting(self.driver, self.file)
        json_cqube_admin_client, keycloack_cqube_admin_client = cal.check_cqube_app_setting()
        self.assertEqual(json_cqube_admin_client, keycloack_cqube_admin_client,
                         msg="Json parameters and keycloack parameters are not matching")

    def test_cqube_app_default_scopes(self):
        cal = CqubeAppDefaultScopes(self.driver, self.file)
        jason_defaultClientScopes, keycloack_assigned_default_client_scopes = cal.check_cqube_app_default_scopes()
        self.assertEqual(jason_defaultClientScopes, keycloack_assigned_default_client_scopes,
                         msg="Json parameters and keycloack parameters are not matching")

    def test_cqube_app_optional_scopes(self):
        cal = CqubeAppOptionalScopes(self.driver, self.file)
        json_assigned_ClientScopes, keycloack_assigned_optional_client_scopes = cal.check_cqube_app_optional_scopes()
        self.assertEqual(json_assigned_ClientScopes, keycloack_assigned_optional_client_scopes,
                         msg="Json parameters and keycloack parameters are not matching")

    def test_cqube_flask(self):
        cal = CqubeFlaskSetting(self.driver, self.file)
        json_cqube_admin_client, keycloack_cqube_admin_client = cal.check_cqube_flask_setting()
        self.assertEqual(json_cqube_admin_client, keycloack_cqube_admin_client,
                         msg="Json parameters and keycloack parameters are not matching")

    def test_cqube_flask_default_scopes(self):
        cal = CqubeFlaskDefaultScopes(self.driver, self.file)
        jason_defaultClientScopes, keycloack_assigned_default_client_scopes = cal.check_cqube_flask_default_scopes()
        self.assertEqual(jason_defaultClientScopes, keycloack_assigned_default_client_scopes,
                         msg="Json parameters and keycloack parameters are not matching")

    def test_cqube_flask_optional_scopes(self):
        cal = CqubeFlaskOptionalScopes(self.driver, self.file)
        json_assigned_ClientScopes, keycloack_assigned_optional_client_scopes = cal.check_cqube_flask_optional_scopes()
        self.assertEqual(json_assigned_ClientScopes, keycloack_assigned_optional_client_scopes,
                         msg="Json parameters and keycloack parameters are not matching")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

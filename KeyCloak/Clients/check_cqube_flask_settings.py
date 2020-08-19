from Data.parameters import Data
from keycloak_funcs import keyData
from reuse_func import GetData
from selenium import webdriver


class CqubeFlaskSetting():
    def __init__(self,driver,file):
        self.driver=driver
        self.file=file

    def check_cqube_flask_setting(self):
        cal = keyData()
        cal.navigate_to_clients(self.driver)
        json_cqube_admin_client=cal.check_clients(self.file,'cqube_flask')
        cal.click_on_cqube_flask(self.driver)
        cal.click_on_settings(self.driver)
        keycloack_cqube_admin_client=cal.check_setting(self.driver)
        cal.click_on_client_scopes(self.driver)
        return json_cqube_admin_client,keycloack_cqube_admin_client

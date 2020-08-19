import time

from Data.parameters import Data
from keycloak_funcs import keyData
from reuse_func import GetData
from selenium import webdriver


class CqubeAdminDefaultScopes():
    def __init__(self,driver,file):
        self.driver=driver
        self.file=file

    def check_cqube_admin_default_scopes(self):
        cal = keyData()
        cal.navigate_to_clients(self.driver)
        cal.click_on_cqube_admin(self.driver)
        time.sleep(3)
        cal.click_on_client_scopes(self.driver)
        jason_defaultClientScopes=cal.check_defaultClientScopes_json(self.file)
        keycloack_assigned_default_client_scopes=cal.check_assigned_default_client_scopes(self.driver)
        jason_defaultClientScopes.sort()
        keycloack_assigned_default_client_scopes.sort()
        return jason_defaultClientScopes,keycloack_assigned_default_client_scopes




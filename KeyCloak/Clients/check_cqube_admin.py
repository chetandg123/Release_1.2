from Data.parameters import Data
from reuse_func import GetData
from selenium import webdriver


class CqubeAdmin():
    def __init__(self,driver,file):
        self.driver=driver
        self.file=file

    def check_cqube_admin(self):
        cal = GetData()
        json_cqube_admin_client=cal.check_clients(self.file,'cqube_admin')
        cal.click_on_cqube_admin(self.driver)
        keycloack_cqube_admin_client=cal.check_setting(self.driver)
        cal.click_on_client_scopes(self.driver)
        jason_defaultClientScopes=cal.check_defaultClientScopes_json(self.file)
        keycloack_assigned_default_client_scopes=cal.check_assigned_default_client_scopes(self.driver)
        jason_defaultClientScopes.sort()
        keycloack_assigned_default_client_scopes.sort()
        json_assigned_ClientScopes = cal.check_assigned_ClientScopes_json(self.file)
        json_assigned_ClientScopes.sort()
        keycloack_assigned_optional_client_scopes= cal.assigned_optional_client_scopes(self.driver)
        keycloack_assigned_optional_client_scopes.sort()
        return json_cqube_admin_client,keycloack_cqube_admin_client,jason_defaultClientScopes,keycloack_assigned_default_client_scopes,json_assigned_ClientScopes,keycloack_assigned_optional_client_scopes



        # json_cqube_admin = []
        # cqube_admin = []
        # for x in self.file['clients']:
        #     if x['clientId'] == 'cqube_admin':
        #         json_cqube_admin.append(x['clientId'])
        #         json_cqube_admin.append(x['enabled'])
        #         json_cqube_admin.append(x['consentRequired'])
        #         json_cqube_admin.append(x['clientAuthenticatorType'])
        #         json_cqube_admin.append(x['standardFlowEnabled'])
        #         json_cqube_admin.append(x['implicitFlowEnabled'])
        #         json_cqube_admin.append(x['directAccessGrantsEnabled'])
        #         json_cqube_admin.append(x['rootUrl'])
        #         json_cqube_admin.append(x['redirectUris'])
        #         json_cqube_admin.append(x['baseUrl'])
        #         json_cqube_admin.append(x['adminUrl'])
        # print(json_cqube_admin)





        # table = GetData()
        # result = table.get_row_count(self.driver)
        #
        # for x in range(1,result):
        #     table_clientid.append(self.driver.find_element_by_xpath('//tbody/tr[%d]/td[1]'%x).text)
        #
        # # print(json_clientid)
        # # print(table_clientid)
        # return json_clientid,table_clientid




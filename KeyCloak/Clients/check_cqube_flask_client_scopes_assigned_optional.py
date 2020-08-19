import time

from keycloak_funcs import keyData


class CqubeFlaskOptionalScopes():
    def __init__(self,driver,file):
        self.driver=driver
        self.file=file

    def check_cqube_flask_optional_scopes(self):
        cal = keyData()
        cal.navigate_to_clients(self.driver)
        cal.click_on_cqube_flask(self.driver)
        time.sleep(3)
        cal.click_on_client_scopes(self.driver)
        json_assigned_ClientScopes = cal.check_assigned_ClientScopes_json(self.file)
        json_assigned_ClientScopes.sort()
        keycloack_assigned_optional_client_scopes= cal.assigned_optional_client_scopes(self.driver)
        keycloack_assigned_optional_client_scopes.sort()
        return json_assigned_ClientScopes,keycloack_assigned_optional_client_scopes





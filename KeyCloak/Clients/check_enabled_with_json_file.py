from Data.parameters import Data
from keycloak_funcs import keyData
from reuse_func import GetData


class Enabled():
    def __init__(self,driver,file):
        self.driver=driver
        self.file=file

    def check_enabled(self):
        json_enabled = []
        table_enabled = []
        for x in self.file['clients']:
            json_enabled.append(str(x['enabled']))

        table = keyData()
        table.navigate_to_clients(self.driver)
        result = table.get_row_count(self.driver)

        for x in range(1,result):
            table_enabled.append(self.driver.find_element_by_xpath('//tbody/tr[%d]/td[2]'%x).text)

        # print(json_enabled)
        # print(table_enabled)
        return json_enabled,table_enabled




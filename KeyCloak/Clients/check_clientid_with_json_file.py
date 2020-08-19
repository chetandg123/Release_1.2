from Data.parameters import Data
from keycloak_funcs import keyData
from reuse_func import GetData


class ClientID():
    def __init__(self,driver,file):
        self.driver=driver
        self.file=file

    def check_clienid(self):
        json_clientid = []
        table_clientid = []
        for x in self.file['clients']:
            json_clientid.append(x['clientId'])

        table = keyData()
        result = table.get_row_count(self.driver)

        for x in range(1,result):
            table_clientid.append(self.driver.find_element_by_xpath('//tbody/tr[%d]/td[1]'%x).text)

        # print(json_clientid)
        # print(table_clientid)
        return json_clientid,table_clientid




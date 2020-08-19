from Data.parameters import Data
from reuse_func import GetData


class BaseUrl():
    def __init__(self,driver,file):
        self.driver=driver
        self.file=file

    def check_BaseUrl(self):
        json_baseurl = []
        table_baseurl = []
        for x in self.file['clients']:
            if x['clientId'] == 'cqube_app' or x['clientId'] == 'cqube_admin' or x['clientId'] == 'cqube_flask':
                json_baseurl.append(x['rootUrl'])

        table = GetData()
        result = table.get_row_count(self.driver)

        for x in range(1,result):
            table_baseurl.append(self.driver.find_element_by_xpath('//tbody/tr[%d]/td[3]'%x).text)

        print(json_baseurl)
        print(table_baseurl)
        # return json_baseurl,table_baseurl




# from reuse_func import GetData
#
# driver1 = GetData()
# file = driver1.open_json_file()
# driver = driver1.get_driver()
# driver1.open_keycloack(driver)
# driver1.login_keycloack(driver)
# driver1.navigate_to_clients()
# lst = driver.find_elements_by_xpath("//table[@class='datatable table table-striped table-bordered dataTable no-footer']/tbody/tr")
# print(len(lst))
# for x in range(1, 9):
#     print(driver.find_element_by_xpath("//tbody/tr[%d]/td[1]"% x).text)
# import unittest
#
#
import unittest


class Clients(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print("")
    def test_lst(self):
        lst1=['email', 'profile', 'role_list', 'roles', 'web-origins']
        lst2=['email', 'profile', 'roles', 'web-origins']
        lst3=set(lst1)-set(lst2)
        print(lst3)
        #self.assertEqual(lst1,lst2,msg="not equal")
        #self.assertListEqual(lst1,lst2,msg="")
    @classmethod
    def tearDownClass(self):
        print("")


#
# import json
#
# import json
#
# with open('/home/devraj/Downloads/realm-export-cqube.json',"r") as f:
#     data = json.loads(f.read())
    # print(data['clients'])
    # for x in data['clients']:
        # print(x['clientId'])
        # print(x['clientId'])
        # print(x['enabled'])
        # if x['clientId'] == 'cqube_app' or x['clientId'] =='cqube_admin' or x['clientId'] =='cqube_flask':
        #     print(x)
    # print(data['clients'][0]['defaultClientScopes'])
    # print(data['defaultOptionalClientScopes'])
    # print(data['clients'][0]['defaultClientScopes'])


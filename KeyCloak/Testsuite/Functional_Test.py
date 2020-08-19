from KeyCloak.Authentications import Authentication_option
from KeyCloak.Clients import Clients_testing
from KeyCloak.RealmSetting import realm_setting
from KeyCloak.Roles import roles_option
from KeyCloak.Users import user_list
from get_dir import pwd
import unittest
from HTMLTestRunner import HTMLTestRunner

class MyTestSuite(unittest.TestCase):

    def test_Issue(self):

            functional_test = unittest.TestSuite()
            functional_test.addTests([
                # file name .class name
                unittest.defaultTestLoader.loadTestsFromTestCase(Authentication_option.Authentication_options),
                unittest.defaultTestLoader.loadTestsFromTestCase(Clients_testing.Clients),
                unittest.defaultTestLoader.loadTestsFromTestCase(realm_setting.realm_settings),
                unittest.defaultTestLoader.loadTestsFromTestCase(roles_option.roles_options),
                unittest.defaultTestLoader.loadTestsFromTestCase(user_list.user_options),
            ])
            p= pwd()
            outfile = open("/home/chetan/Desktop/cQubeTesting/KeyCloak/Testsuite/keycloak.html", "w")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Keycloak  Test Report',
                verbosity=1,
            )

            runner1.run(functional_test)

    @classmethod
    def tearDownClass(self):
        self.driver.close()



if __name__ == '__main__':
    unittest.main()
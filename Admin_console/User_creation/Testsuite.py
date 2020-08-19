import unittest

from HTMLTestRunner import HTMLTestRunner

from Create_User import check_in_keycloak, create_user, login_cqube_with_new_users
from get_dir import pwd


class MyTestSuite(unittest.TestCase):

    def test_Issue(self):

            functional_test = unittest.TestSuite()
            functional_test.addTests([
                # file name .class name
                unittest.defaultTestLoader.loadTestsFromTestCase(check_in_keycloak.keycloak),
                unittest.defaultTestLoader.loadTestsFromTestCase(create_user.Creating_users),
                unittest.defaultTestLoader.loadTestsFromTestCase(login_cqube_with_new_users.Creating_users),
            ])
            p= pwd()
            outfile = open(p.get_user_report_path(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='User creation  Test Report',
                verbosity=1,
            )

            runner1.run(functional_test)

    @classmethod
    def tearDownClass(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
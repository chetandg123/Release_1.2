import time
import unittest

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from get_dir import pwd
from reuse_func import GetData


class Test_summaryreport(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.p = pwd()
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.page_loading(self.driver)
        self.data.login_to_adminconsole(self.driver)

    def test_summary_icon(self):
        count = 0
        self.data.page_loading(self.driver)
        self.driver.find_element_by_xpath("//*[@id='summary']/img").click()
        self.data.page_loading(self.driver)
        if 'summary-statistics' in self.driver.current_url:
            print("Summmary statistics report page is present ")
        else:
            print('Summary report page is not displayed')
            count = count + 1
        self.assertEqual(0,count,msg='Summary report page is not working')
        self.driver.find_element_by_id('homeBtn').click()
        self.data.page_loading(self.driver)

    def test_dashboard_summary(self):
        count = 0
        self.driver.find_element_by_id(Data.Dashboard).click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='summary']/div/td[2]").click()
        self.data.page_loading(self.driver)
        if 'summary-statistics' in self.driver.current_url:
            print("Summmary statistics report page is present ")
        else:
            print('Summary report page is not displayed')
            count = count + 1
        self.assertEqual(0,count,msg='Summary report page is not working')
        self.driver.find_element_by_id('homeBtn').click()
        self.data.page_loading(self.driver)

    def test_check_summary(self):
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Dashboard).click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='summary']/div/td[2]").click()
        self.data.page_loading(self.driver)
        reports =self.driver.find_elements_by_tag_name('h2')
        count = len(reports)
        for i in range(len(reports)):
            print(reports[i].text)
        self.assertNotEqual(0,count,msg='All summary reports are not present')
        if count > 6:
            print("summary report of all files to be updated")
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id('homeBtn').click()
        self.data.page_loading(self.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
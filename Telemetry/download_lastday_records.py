import os
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from get_dir import pwd
from reuse_func import GetData


class lastday_download():
    def __init__(self, driver):
        self.driver = driver

    def test_lastday_records(self):
        self.data = GetData()
        self.p = pwd()
        self.data.page_loading(self.driver)
        period = Select(self.driver.find_element_by_id('year'))
        period.select_by_visible_text(' Last Day ')
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(4)
        self.filename = self.p.get_download_dir() + '/District_wise_report.csv'
        file = os.path.isfile(self.filename)
        self.data.page_loading(self.driver)
        os.remove(self.filename)
        return file

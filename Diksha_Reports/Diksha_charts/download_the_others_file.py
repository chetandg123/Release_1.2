import os
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from get_dir import pwd
from reuse_func import GetData


class Diksha_others_download():
    def __init__(self, driver):
        self.driver = driver
        self.filename = ''

    def test_others_file(self):
        self.data = GetData()
        self.p = pwd()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        download = Select(self.driver.find_element_by_id('downloader'))
        download.select_by_visible_text(' Other ')
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id('download').click()
        time.sleep(5)
        self.filename = self.p.get_download_dir() + '/Diksha_All_data_Other.csv'
        file =  os.path.isfile(self.filename)
        self.data.page_loading(self.driver)
        os.remove(self.filename)
        return file



from selenium.webdriver.support.select import Select

from Data.parameters import Data
from reuse_func import GetData


class overall_timeperiod():
    def __init__(self,driver):
        self.driver = driver

    def test_overall_records(self):
        self.data = GetData()
        self.data.page_loading(self.driver)
        period = Select(self.driver.find_element_by_id('year'))
        period.select_by_visible_text(' Over All ')
        self.data.page_loading(self.driver)
        if 'No data found' in self.driver.page_source:
            print('Selected catagory  has no records')
        else:
            self.driver.find_element_by_id('block').click()
            markers = self.driver.find_elements_by_class_name(Data.dots)
            bcount = len(markers)
            self.data.page_loading(self.driver)
            self.driver.find_element_by_id('cluster').click()
            markers = self.driver.find_elements_by_class_name(Data.dots)
            ccount = len(markers) - 1
            self.data.page_loading(self.driver)
            self.driver.find_element_by_id('school').click()
            markers = self.driver.find_elements_by_class_name(Data.dots)
            scount = len(markers)
            self.data.page_loading(self.driver)
            # return bcount,ccount,scount

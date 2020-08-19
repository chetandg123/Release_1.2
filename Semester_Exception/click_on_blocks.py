import os
import time

from Data.parameters import Data
from get_dir import pwd
from reuse_func import GetData


class Semester_Blocks():
    def __init__(self, driver):
        self.driver = driver

    def check_markers_on_block_map(self):
        self.driver.find_element_by_id(Data.sr_block_btn).click()
        cal = GetData()
        cal.page_loading(self.driver)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        markers = len(dots) - 1
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(2)
        p = pwd()
        self.filename = p.get_download_dir() + "/Block_wise_report.csv"
        if os.path.isfile(self.filename) != True:
            return "File Not Downloaded"
        if os.path.isfile(self.filename) == True:
            os.remove(self.filename)
        return markers
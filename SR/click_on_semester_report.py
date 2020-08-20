import time

from Data.parameters import Data
from reuse_func import GetData


class SemesterReport():
    def __init__(self, driver):
        self.driver = driver

    def check_semester_landing_page(self):
        return self.driver.page_source



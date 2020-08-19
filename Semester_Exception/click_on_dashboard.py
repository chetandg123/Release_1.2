import time

from Data.parameters import Data
from reuse_func import GetData


class sem_dashboard():
    def __init__(self, driver):
        self.driver = driver

    def test_click_on_dashboard(self):
        count = 0
        self.driver.find_element_by_id(Data.Dashboard).click()
        time.sleep(1)
        self.driver.find_element_by_id(Data.sem_exception).click()
        cal = GetData()
        cal.page_loading(self.driver)
        if 'sem-exception' in self.driver.current_url:
            print("Semester exception report is present ")
        else:
            print("Semester exception is not exist")
            count = count + 1
        return count

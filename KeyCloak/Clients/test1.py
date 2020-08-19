# import time
#
# from selenium.webdriver.support.select import Select
#
# from reuse_func import GetData
#
# driver1 = GetData()
# file = driver1.open_json_file()
# driver = driver1.get_driver()
# driver1.open_keycloack(driver)
# driver1.login_keycloack(driver)
# driver1.navigate_to_clients()
# # lst = driver.find_elements_by_xpath("//table[@class='datatable table table-striped table-bordered dataTable no-footer']/tbody/tr")
# driver.find_element_by_link_text('cqube_admin').click()
# time.sleep(3)
# driver.find_element_by_link_text('Client Scopes').click()
# time.sleep(5)
# default_client = Select(driver.find_element_by_id('assigned'))
# print(default_client.options)
# defaults = []
# for x in default_client.options:
#     x = x.text
#     defaults.append(x.strip())
# print(defaults)


# result = driver.find_element_by_id('consentRequired')
# print(result.get_attribute('class'))
# clientid = driver.find_element_by_id('clientId')
# print(clientid.get_attribute('value'))
# enabled = driver.find_element_by_id('enabled')
# consentRequired=driver.find_element_by_id('consentRequired')
# client_protocol = Select(driver.find_element_by_id('protocol'))
# print(client_protocol.first_selected_option.text)
# standardFlowEnabled = driver.find_element_by_id('standardFlowEnabled')
# implicitFlowEnabled=driver.find_element_by_id('implicitFlowEnabled')
# directAccessGrantsEnabled=driver.find_element_by_id('directAccessGrantsEnabled')
# rootUrl=driver.find_element_by_id('rootUrl')
# redirect=driver.find_element_by_xpath('//*[@id="view"]/div[1]/form/fieldset[1]/div[33]/div/div[1]/input')
# print(redirect.get_attribute('value'))
# baseUrl=driver.find_element_by_id('baseUrl')
# adminUrl=driver.find_element_by_id('adminUrl')
import configparser

from get_dir import pwd

p = pwd()
config = configparser.ConfigParser()
config.read(p.get_keycloak_ini_path())
print(config['config']['json'])


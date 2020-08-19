import configparser
import json

from selenium import webdriver
from selenium.webdriver.support.select import Select

from Data.key_parameters import Data
from get_dir import pwd


class keyData():
    def __init__(self):
        self.p = pwd()

    def get_cqube_url(self):
        config = configparser.ConfigParser()
        config.read(self.p.get_keycloak_ini_path())
        return config['config']['domain']

    def get_keydomain_name(self):
        config = configparser.ConfigParser()
        config.read(self.p.get_keycloak_ini_path())
        return config['config']['domain_keycloak']

    def get_nifi_url(self):
        config = configparser.ConfigParser()
        config.read(self.p.get_keycloak_ini_path())
        return config['config']['nifi']

    def get_username(self):
        config = configparser.ConfigParser()
        config.read(self.p.get_keycloak_ini_path())
        return config['config']['username_keycloak']

    def get_password(self):
        config = configparser.ConfigParser()
        config.read(self.p.get_keycloak_ini_path())
        return config['config']['password_keycloak']

    def get_json_file_path(self):
        config = configparser.ConfigParser()
        config.read(self.p.get_keycloak_ini_path())
        return config['config']['json']

    def get_domain_cqube_name(self):
        config = configparser.ConfigParser()
        config.read(self.p.get_keycloak_ini_path())
        return config['config']['domainname']

    def get_privateip(self):
        config = configparser.ConfigParser()
        config.read(self.p.get_keycloak_ini_path())
        return config['config']['privateip']

    def get_driver(self):
        options = webdriver.ChromeOptions()
        # prefs = {'download.default_directory': self.p.get_download_dir()}
        # options.add_experimental_option('prefs', prefs)
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options, executable_path=self.p.get_driver_path())
        return self.driver

    def open_keycloack(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.get(self.get_keydomain_name())
        self.driver.implicitly_wait(60)

    def open_nifi(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.get(self.get_nifi_url())
        self.driver.implicitly_wait(60)

    def login_keycloack(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(60)
        # self.driver.find_element_by_xpath(Data.console_link_text).click()
        self.driver.find_element_by_id(Data.email).send_keys(self.get_username())
        self.driver.find_element_by_id(Data.passwd).send_keys(self.get_password())
        self.driver.find_element_by_id(Data.login).click()

    def navigate_to_clients(self, driver):
        self.driver = driver
        self.driver.find_element_by_link_text('Clients').click()

    def open_json_file(self):
        with open(self.get_json_file_path(), "r") as f:
            data = json.loads(f.read())
            return data

    def get_row_count(self, driver):
        self.driver = driver
        return len(self.driver.find_elements_by_xpath(Data.tbl_row_count_xpath))

    def check_setting(self, driver):
        keycloack = []
        self.driver = driver
        clientid = self.driver.find_element_by_id('clientId')
        keycloack.append(clientid.get_attribute('value'))

        enabled = self.driver.find_element_by_id('enabled')
        enabled.get_attribute('class')
        if enabled.get_attribute('class') == "onoffswitch-checkbox ng-pristine ng-untouched ng-valid ng-not-empty":
            keycloack.append('True')
        else:
            keycloack.append('False')

        consentRequired = self.driver.find_element_by_id('consentRequired')

        if consentRequired.get_attribute(
                'class') == "onoffswitch-checkbox ng-pristine ng-untouched ng-valid ng-not-empty":
            keycloack.append('True')
        else:
            keycloack.append('False')

        client_protocol = Select(self.driver.find_element_by_id('protocol'))
        keycloack.append(client_protocol.first_selected_option.text)
        standardFlowEnabled = self.driver.find_element_by_id('standardFlowEnabled')
        if standardFlowEnabled.get_attribute(
                'class') == "onoffswitch-checkbox ng-pristine ng-untouched ng-valid ng-not-empty":
            keycloack.append('True')
        else:
            keycloack.append('False')

        implicitFlowEnabled = self.driver.find_element_by_id('implicitFlowEnabled')

        if implicitFlowEnabled.get_attribute(
                'class') == "onoffswitch-checkbox ng-pristine ng-untouched ng-valid ng-not-empty":
            keycloack.append('True')
        else:
            keycloack.append('False')

        directAccessGrantsEnabled = self.driver.find_element_by_id('directAccessGrantsEnabled')
        if directAccessGrantsEnabled.get_attribute(
                'class') == "onoffswitch-checkbox ng-pristine ng-untouched ng-valid ng-not-empty":
            keycloack.append('True')
        else:
            keycloack.append('False')

        rootUrl = self.driver.find_element_by_id('rootUrl')
        keycloack.append(rootUrl.get_attribute('value'))

        redirect = self.driver.find_element_by_xpath('//*[@id="view"]/div[1]/form/fieldset[1]/div[33]/div/div[1]/input')
        keycloack.append(redirect.get_attribute('value'))

        baseUrl = self.driver.find_element_by_id('baseUrl')
        keycloack.append(baseUrl.get_attribute('value'))

        adminUrl = self.driver.find_element_by_id('adminUrl')
        keycloack.append(adminUrl.get_attribute('value'))

        return keycloack

    def check_clients(self, filename, cid):
        self.file = filename
        json_cqube_admin = []
        for x in self.file['clients']:
            if x['clientId'] == cid:
                json_cqube_admin.append(x['clientId'])
                json_cqube_admin.append(str(x['enabled']))
                json_cqube_admin.append(str(x['consentRequired']))
                json_cqube_admin.append(x['protocol'])
                json_cqube_admin.append(str(x['standardFlowEnabled']))
                json_cqube_admin.append(str(x['implicitFlowEnabled']))
                json_cqube_admin.append(str(x['directAccessGrantsEnabled']))
                json_cqube_admin.append(x['rootUrl'])
                json_cqube_admin.append(x['redirectUris'][0])
                json_cqube_admin.append(x['baseUrl'])
                json_cqube_admin.append(x['adminUrl'])

        return json_cqube_admin

    def check_assigned_default_client_scopes(self, driver):
        self.driver = driver
        default_client = Select(self.driver.find_element_by_id('assigned'))
        defaults = []
        for x in default_client.options:
            x = x.text
            defaults.append(x.strip())
        return defaults

    def check_defaultClientScopes_json(self, filename):
        self.file = filename
        return self.file['clients'][0]['defaultClientScopes']

    def check_assigned_ClientScopes_json(self, filename):
        self.file = filename
        return self.file['defaultOptionalClientScopes']

    def assigned_optional_client_scopes(self, driver):
        self.driver = driver
        default_client = Select(self.driver.find_element_by_id('assigned-opt'))
        defaults = []
        for x in default_client.options:
            x = x.text
            defaults.append(x.strip())
        return defaults

    def click_on_cqube_admin(self, driver):
        self.driver = driver
        self.driver.find_element_by_link_text('cqube_admin').click()

    def click_on_cqube_app(self, driver):
        self.driver = driver
        self.driver.find_element_by_link_text('cqube_app').click()

    def click_on_cqube_flask(self, driver):
        self.driver = driver
        self.driver.find_element_by_link_text('cqube_flask').click()

    def click_on_settings(self, driver):
        self.driver = driver
        self.driver.find_element_by_link_text('Settings').click()

    def click_on_client_scopes(self, driver):
        self.driver = driver
        self.driver.find_element_by_link_text('Client Scopes').click()

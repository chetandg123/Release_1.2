from keycloak_funcs import keyData

class CheckBaseUrl():
    def __init__(self,driver,file):
        self.driver=driver
        self.file=file

    def check_BaseUrl_with_domain_name_and_privateip(self):
        cal = keyData()
        json_baseurl = []
        url = []
        for x in self.file['clients']:
            if x['clientId'] == 'cqube_app' or x['clientId'] == 'cqube_admin' or x['clientId'] == 'cqube_flask':
                json_baseurl.append(x['rootUrl'])
        url.append(cal.get_privateip())
        url.append(cal.get_domain_cqube_name())
        url.append(cal.get_domain_cqube_name()+"/data")
        json_baseurl.sort()
        url.sort()
        return json_baseurl,url





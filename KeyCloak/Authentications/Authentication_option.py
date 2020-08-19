import json
import re
import time
import unittest

from keycloak_funcs import keyData


class Authentication_options(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.data = keyData()
        self.driver = self.data.get_driver()
        self.data.open_keycloack(self.driver)
        self.data.login_keycloack(self.driver)
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='view']/div[2]/div[2]/ul/li[7]/a").click()
        self.f = open(self.data.get_json_file_path(), "r")
        self.file = json.loads(self.f.read())


    def test_flows(self):
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(),'Flows')]").click()
        reset = self.driver.find_element_by_xpath("//*[@id='view']/div[1]/table/thead/tr[1]/th/div[1]/select/option[1]")
        len = reset.is_selected()
        self.assertTrue(len, msg="http   is not selected")

        user = self.driver.find_element_by_xpath("//*[@id='view']/div[1]/table/tbody/tr[1]/td[3]/label/input")
        radio = user.is_selected()
        self.assertTrue(radio,msg="Choose user	is not in Required state ")

        mail = self.driver.find_element_by_xpath("//*[@id='view']/div[1]/table/tbody/tr[2]/td[3]/label/input")
        radio = mail.is_selected()
        self.assertTrue(radio, msg="send reset mail is not in required state ")

        resetpwd = self.driver.find_element_by_xpath("//*[@id='view']/div[1]/table/tbody/tr[3]/td[3]/label/input")
        radio = resetpwd.is_selected()
        self.assertTrue(radio, msg="reset password  is  not in required state  ")


        resetconditional = self.driver.find_element_by_xpath("//*[@id='view']/div[1]/table/tbody/tr[4]/td[6]/label/input")
        radio = resetconditional.is_selected()
        self.assertTrue(radio, msg="Reset conditional otp is conditional is not selected ")


        userconfig = self.driver.find_element_by_xpath("//*[@id='view']/div[1]/table/tbody/tr[5]/td[3]/label/input")
        radio = userconfig.is_selected()
        self.assertTrue(radio, msg="userconfig is not selected ")

        resetotp = self.driver.find_element_by_xpath("//*[@id='view']/div[1]/table/tbody/tr[6]/td[3]/label/input")
        r = resetotp.is_selected()
        self.assertTrue(r,msg="Reset otp is not selected ")

    def test_Bindings(self):
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(),'Bindings')]").click()

        browserflow = self.driver.find_element_by_id("browser").get_attribute('value')
        self.assertEqual("string:"+self.file['browserFlow'],browserflow,msg="Browser is not selected at browserflow ")

        registrationflow = self.driver.find_element_by_id("registration").get_attribute('value')
        self.assertEqual("string:"+self.file['registrationFlow'],registrationflow, msg="Browser is not selected at registrationflow ")

        directgrantflow = self.driver.find_element_by_id("grant").get_attribute('value')
        self.assertEqual("string:"+self.file['directGrantFlow'], directgrantflow, msg="Browser is not selected at directGrantFlow ")

        resetcredential = self.driver.find_element_by_id("resetCredentials").get_attribute('value')
        self.assertEqual("string:"+self.file['resetCredentialsFlow'], resetcredential,msg="Browser is not selected at directGrantFlow ")

        clientAuthenticationFlow = self.driver.find_element_by_id("clientAuthentication").get_attribute('value')
        self.assertEqual("string:"+self.file['clientAuthenticationFlow'], clientAuthenticationFlow, msg="Browser is not selected at directGrantFlow ")
        print("all configuration are correct in binding section")

    def test_RequiredActions(self):
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(),'Required Actions')]").click()
        configurotp = self.driver.find_element_by_id("CONFIGURE_TOTP.enabled")
        otp = configurotp.is_selected()
        print("status of selction : ", otp)
        print("Files contains",self.file['requiredActions'][0]['enabled'])
        self.assertEqual(otp , self.file['requiredActions'][0]['enabled'],msg="configure otp is not selected")

        defaultval = self.driver.find_element_by_id("CONFIGURE_TOTP.defaultAction")
        d = defaultval.is_selected()
        print("file contains",self.file['requiredActions'][0]['defaultAction'])
        self.assertEqual(d , self.file['requiredActions'][0]['defaultAction'],msg="Default configure otp is not selected")

        # default = self.driver.find_element_by_id("CONFIGURE_TOTP.defaultAction")
        # enable = default.is_selected()
        # self.assertTrue(enable, msg="configure otp is default  not selected ")

        terms = self.driver.find_element_by_id("terms_and_conditions.enabled")
        ter = terms.is_selected()
        self.assertEqual(self.file['requiredActions'][1]['enabled'],ter ,msg="Terms and condition is selected")
        dterms = self.driver.find_element_by_id("terms_and_conditions.defaultAction")
        dter = dterms.is_selected()
        self.assertEqual(self.file['requiredActions'][1]['defaultAction'],dter ,msg="Terms and condition is selected")

        updatepass = self.driver.find_element_by_id("UPDATE_PASSWORD.enabled")
        enable = updatepass.is_selected()
        self.assertEqual(self.file['requiredActions'][2]['enabled'],enable, msg=" Update password is   not selected ")
        defupdate = self.driver.find_element_by_id("UPDATE_PASSWORD.defaultAction")
        disable = defupdate.is_selected()
        self.assertEqual(self.file['requiredActions'][2]['defaultAction'], disable, msg="default Update password is selected ")

        updateprofile = self.driver.find_element_by_id("UPDATE_PROFILE.enabled")
        enable = updateprofile.is_selected()
        self.assertEqual(self.file['requiredActions'][3]['enabled'], enable, msg="default Update profile is  not selected ")
        updateprofile = self.driver.find_element_by_id("UPDATE_PROFILE.defaultAction")
        enable = updateprofile.is_selected()
        self.assertEqual(self.file['requiredActions'][3]['defaultAction'], enable, msg="default Update profile is selected ")


        verifymail = self.driver.find_element_by_id("VERIFY_EMAIL.enabled")
        enable = verifymail.is_selected()
        self.assertEqual(self.file['requiredActions'][4]['enabled'], enable, msg="default verify mail is not selected ")
        verifymail = self.driver.find_element_by_id("VERIFY_EMAIL.defaultAction")
        disable = verifymail.is_selected()
        self.assertEqual(self.file['requiredActions'][4]['defaultAction'], disable, msg="default verify mail  is selected ")

        updateuser = self.driver.find_element_by_id("update_user_locale.enabled")
        enable = updateuser.is_selected()
        self.assertEqual(self.file['requiredActions'][5]['enabled'], enable, msg="default Update password is not selected ")
        updateuser = self.driver.find_element_by_id("update_user_locale.defaultAction")
        enable = updateuser.is_selected()
        self.assertEqual(self.file['requiredActions'][5]['defaultAction'], enable, msg="default Update password is selected ")


    def test_PasswordPolicy(self):
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(),'Password Policy')]").click()

        passwordexipe = self.driver.find_element_by_xpath("//*[@id='view']/div[1]/form/table/tbody/tr[1]/td[2]/input").get_attribute('value')
        self.assertEqual(180,int(passwordexipe),msg="mismatch found at password expire field")

        specialchar = self.driver.find_element_by_xpath("//*[@id='view']/div[1]/form/table/tbody/tr[2]/td[2]/input").get_attribute('value')
        self.assertEqual(1, int(specialchar), msg="mismatch found at  special character field")

        upper = self.driver.find_element_by_xpath("//*[@id='view']/div[1]/form/table/tbody/tr[3]/td[2]/input").get_attribute('value')
        self.assertEqual(1, int(upper), msg="mismatch found at  upper character field")

        lower = self.driver.find_element_by_xpath("//*[@id='view']/div[1]/form/table/tbody/tr[4]/td[2]/input").get_attribute('value')
        self.assertEqual(1, int(lower), msg="mismatch found at lower character field")

        maxlength = self.driver.find_element_by_xpath("//*[@id='view']/div[1]/form/table/tbody/tr[5]/td[2]/input").get_attribute('value')
        self.assertEqual(8, int(maxlength), msg="mismatch found at Max length field")

        digits = self.driver.find_element_by_xpath("//*[@id='view']/div[1]/form/table/tbody/tr[6]/td[2]/input").get_attribute('value')
        self.assertEqual(1, int(digits), msg="mismatch found at digits field")



    def test_otp_policty(self):
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(),'OTP Policy')]").click()
        # type = self.driver.find_element_by_id("type").get_attribute('value')
        # self.assertEqual(self.file['otpPolicyType'],type,msg="unknown policy type")

        # alg = self.driver.find_element_by_id("alg").get_attribute('value')
        # self.assertEqual(self.file['otpPolicyAlgorithm'], alg, msg="algorithm name mis matched")

        digits = self.driver.find_element_by_id("digits").get_attribute('value')
        nums = res = re.sub('\D', "", digits)
        self.assertEqual(self.file['otpPolicyDigits'],int(nums), msg="no fo digits changed")

        lookAhead = self.driver.find_element_by_id("lookAhead").get_attribute('value')
        nums = res = re.sub('\D', "", lookAhead)
        self.assertEqual(self.file['otpPolicyLookAheadWindow'], int(nums), msg="lookahaed is changed their values")

        period = self.driver.find_element_by_id("period").get_attribute('value')
        self.assertEqual(self.file['otpPolicyPeriod'],int(period), msg="time periods changed")

    def test_webauth(self):
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(),'WebAuthn Policy')]").click()
        name = self.driver.find_element_by_id("name").get_attribute('value')
        self.assertEqual(self.file['webAuthnPolicyRpEntityName'],name,msg="webAuthnPolicyRpEntityName is different")

        algorithm= self.driver.find_element_by_xpath("//*[@id='sigalg']/option[1]")
        alg = algorithm.is_selected()
        self.assertTrue(alg,msg="algorithm change found")

        tout = self.driver.find_element_by_id("timeout").get_attribute('value')
        self.assertEqual(self.file['webAuthnPolicyCreateTimeout'],int(tout),msg="time out value mis matched")

        register = self.driver.find_element_by_xpath("//*[@id='view']/div[1]/form/div[9]/div/div/span/div/label/span[1]/span[2]").text
        self.assertEqual("OFF",register,msg="webAuthnPolicyAvoidSameAuthenticatorRegister is ON state")

    def test_PasswordlessPolicy(self):
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(),'WebAuthn Passwordless Policy')]").click()
        name = self.driver.find_element_by_id("name").get_attribute('value')
        self.assertEqual(self.file['webAuthnPolicyRpEntityName'],name,msg="webAuthnPolicyRpEntityName is different")

        algorithm= self.driver.find_element_by_xpath("//*[@id='sigalg']/option[1]")
        alg = algorithm.is_selected()
        self.assertTrue(alg,msg="algorithm change found")
        print("algorithm :",algorithm)
        # self.assertEqual(algorithm,self.file['webAuthnPolicyPasswordlessSignatureAlgorithms'],msg="webAuthnPolicyPasswordlessSignatureAlgorithms is changed")

        tout = self.driver.find_element_by_id("timeout").get_attribute('value')
        self.assertEqual(self.file['webAuthnPolicyCreateTimeout'],int(tout),msg="time out value mis matched")

        register = self.driver.find_element_by_xpath("//*[@id='view']/div[1]/form/div[9]/div/div/span/div/label/span[1]/span[2]").text
        self.assertEqual("OFF",register,msg="webAuthnPolicyAvoidSameAuthenticatorRegister is ON state")


    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.close()

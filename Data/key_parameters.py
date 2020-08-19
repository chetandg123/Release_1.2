


class Data():
    realme_setting = "//*[@id='view']/div[2]/div[2]/ul/li[1]/a/text()"
    login = "kc-login"
    email = "username"
    passwd = "password"
    home = 'homeBtn'
    Dashboard ='menu'
    cuser = 'crtUsr'
    userlist ='user'
    cuser_icon ="//*[@id='logs']/img"
    #Administration Console
    console_link_text='/html/body/div[2]/div/div/div[2]/div[1]/div/div/h3/a'

    #clients
    clients_link_text = 'Clients'
    setting_link_text='Settings'

    #clients table
    tbl_row_count_xpath ="//table[@class='datatable table table-striped table-bordered dataTable no-footer']/tbody/tr"

    clientid='clientId'
    enabled_class='onoffswitch-inner'
    rootUrl_id='rootUrl'
    baseUrl_id='baseUrl'
    adminUrl_id='adminUrl'
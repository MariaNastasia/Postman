from selenium import webdriver
import time
from selenium.webdriver.common.by import By



DRIVER_PATH = "E:\\Maya\Login\\msedgedriver.exe"
URL_TO_TEST = "https://www.demo.guru99.com/V4"
USER = "mngr503832"
PASSWORD = "YzYdevy"

class Login():

    def loginUtilizatior (self, utilizator, parola):
        print("Incep testarea")
        driver = webdriver.Edge (DRIVER_PATH)
        driver.get(URL_TO_TEST)

        time.sleep(10)
        

        iframe = driver.find_element(By.ID, "gdpr-consent-notice")
        driver.switch_to.frame(iframe)

   

        acceptALL = driver.find_element(By.ID, "save")
        acceptALL.click()


        time.sleep(20)
       

        userName = driver.find_element(By.NAME,"uid")
      
        userName.send_keys(utilizator)

        userPassword = driver.find_element(By.NAME,"password")
        userPassword.send_keys(parola)

        loginBtn = driver.find_element(By.NAME,"btnLogin")
        loginBtn.click()

        time.sleep(10)

        test = 0
        try:
            actualTitle = driver.title
        except:
            print("Test Case PASSED")
            test = 1
            
        assert test == 1, "Test failed should not login"
            
        time.sleep(10)
        
        driver.close()

    def loginTest(self):
        print("Incep testarea")
        driver = webdriver.Edge (DRIVER_PATH)
        driver.get(URL_TO_TEST)

        time.sleep(10)
        

        iframe = driver.find_element(By.ID, "gdpr-consent-notice")
        driver.switch_to.frame(iframe)

   

        acceptALL = driver.find_element(By.ID, "save")
        acceptALL.click()


        time.sleep(20)
       

        userName = driver.find_element(By.NAME,"uid")

        userName.send_keys(USER)

        userPassword = driver.find_element(By.NAME,"password")
        userPassword.send_keys(PASSWORD)

        loginBtn = driver.find_element(By.NAME,"btnLogin")
        loginBtn.click()

        actualTitle = driver.title
        
        assert actualTitle == "Guru99 Bank Manager HomePage", "FAILED actual title"

        time.sleep(10)
        
        driver.close()

    def loginTestUserNOTOK(self):
        self.loginUtilizatior ("userNOTOK",PASSWORD )

    def loginTestPasswordNOTOK(self):
        self.loginUtilizatior(USER, "PasswordNOTOK")        


    def loginTestUserandPasswordNOTOK(self):
        self.loginUtilizatior("UserNOTOK", "PasswordNOTOK")

    def loginTestEmptyUser(self):
        self.loginUtilizatior("", PASSWORD)

                        
    def loginTestEmptyPassword(self):
        print("Incep testarea")
        driver = webdriver.Edge (DRIVER_PATH)
        driver.get (URL_TO_TEST)

        time.sleep(10)
        

        iframe = driver.find_element(By.ID, "gdpr-consent-notice")
        driver.switch_to.frame(iframe)

   

        acceptALL = driver.find_element(By.ID, "save")
        acceptALL.click()


        time.sleep(20)
       

        userName = driver.find_element(By.NAME,"uid")
       
        userName.send_keys(USER)

        userPassword = driver.find_element(By.NAME,"password")
        userPassword.send_keys("")

        loginBtn = driver.find_element(By.NAME,"btnLogin")
        loginBtn.click()

        time.sleep(10)

        #ID = message18
        find = 0
        try:
            driver.find_element(By.ID, "message18")
            find = 1 
        except: find = 0
        assert find == 1, "Message Password empty not found"

        
            
       
        
        driver.close()

                        
logintest = Login()
logintest.loginTest()
logintest.loginTestUserNOTOK()
logintest.loginTestPasswordNOTOK()
logintest.loginTestUserandPasswordNOTOK()
logintest.loginTestEmptyUser()
logintest.loginTestEmptyPassword()
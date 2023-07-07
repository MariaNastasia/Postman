from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

DRIVER_PATH = "E:\\Maya\Login\\msedgedriver.exe"
URL_TO_TEST = "https://www.letskodeit.com/practice"


class Incercari():
    def primaincercare(self):
        print ("prima incercare")
        driver = webdriver.Edge (DRIVER_PATH)
        driver.get(URL_TO_TEST)
        time.sleep(10)  

        bmwRadioBtn = driver.find_element(By.ID, "bmwradio")
        bmwRadioBtn.click()
        time.sleep(10)  

        benzRadioBtn = driver.find_element(By.ID,"benzradio")
        benzRadioBtn.click()
        time.sleep(10)  

        hondaRadioBtn = driver.find_element(By.ID, "hondaradio")
        hondaRadioBtn.click()
        time.sleep(10)

    def adouaincercare(self):
        print ("a doua incercare")
        driver = webdriver.Edge (DRIVER_PATH)
        driver.get(URL_TO_TEST)
        time.sleep(10)  



        radioBtnList = driver.find_elements(By.XPATH, "//input[contains(@type, 'radio') and contains(@name, 'cars')]")

        for x in radioBtnList: 
            x.click()
            time.sleep(10)

    def dropDown(self):
        print("drop Down")
        driver = webdriver.Edge (DRIVER_PATH)
        driver.get(URL_TO_TEST)
        time.sleep(10)  

        element = driver.find_element(By.ID, "carselect")
        sel = Select(element)

        sel.select_by_value("benz")
        time.sleep(10)

        sel.select_by_value("honda")
        time.sleep(10)

        sel.select_by_value("bmw")
        time.sleep(10)

        sel.select_by_index(1) #benz
        time.sleep(5)
        
        sel.select_by_index(2) #honda
        time.sleep(5)

        sel.select_by_index(0) #bmw
        time.sleep(5)

    def dropDown_second(self):
        print("drop Down second")
        driver = webdriver.Edge (DRIVER_PATH)
        driver.get(URL_TO_TEST)
        time.sleep(10)  

        element = driver.find_element(By.ID, "carselect")
        sel = Select(element)

        length = len(element.size)
        print(length)

        for  x in range(length+1):
            sel.select_by_index(x)
            time.sleep(5)


    def dropDown_text(self):
        print("drop Down text")
        driver = webdriver.Edge (DRIVER_PATH)
        driver.get(URL_TO_TEST)
        time.sleep(10)  

        element = driver.find_element(By.ID, "carselect")
        sel = Select(element)

        sel.select_by_visible_text("Benz")
        time.sleep(5)  

        sel.select_by_visible_text("Honda")
        time.sleep(5)  

        sel.select_by_visible_text("BMW")
        time.sleep(5)  











incerc = Incercari()
#incerc.primaincercare()
#incerc.adouaincercare()
#incerc.dropDown()
#incerc.dropDown_second()
incerc.dropDown_text()
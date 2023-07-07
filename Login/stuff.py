from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

DRIVER_PATH = "E:\\Maya\Login\\msedgedriver.exe"
URL_TO_TEST = "https://www.letskodeit.com/practice"

class Stuff:
    def incercare(self):
        print ("prima incercare")
        driver = webdriver.Edge (DRIVER_PATH)
        driver.get(URL_TO_TEST)
        time.sleep(10)  


        text = driver.find_element(By.LINK_TEXT, "PRACTICE")

        if text is not None:
            print("Am gasit un element dupa partial link text")


        el = driver.find_element(By.CLASS_NAME, "inputs")
        if el is not None:
            print("Am gasit elementul dupa clasa")

        el.send_keys("ceva")


        element = driver.find_element(By.TAG_NAME, "h1")
        if element is not None:
            print("Am gasit elemenetul dupa tag name")
        time.sleep(10)

    def switch_to_window(self):
        print ("switch")
        driver = webdriver.Edge (DRIVER_PATH)
        driver.get(URL_TO_TEST)
        time.sleep(10)  

        el=driver.find_element(By.ID, "openwindow")
        el.click()

        print(driver.window_handles)

        time.sleep(10)

        driver.switch_to.window(driver.window_handles[0])

        time.sleep(10)


        driver.switch_to.window(driver.window_handles[1])
        time.sleep(10)



incerc = Stuff()
#incerc.incercare()
incerc.switch_to_window()


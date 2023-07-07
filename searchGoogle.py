from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class searchGoogle():
    def test(self):
        print("incep testarea")
        driver = webdriver.Edge("E:\\Maya\\Software Testing\\msedgedriver.exe")

        driver.get("http://google.com")

        element = driver.find_element(By.CLASS_NAME, "sy4vM")
        element.click()

        elementSearch = driver.find_element(By.ID, "APjFqb")
        elementSearch.send_keys("selenium")
        #elementSubmit = driver.find_element(By.XPATH, "//input[@name='btnK'])[2]")
        

        
        time.sleep(30)



search = searchGoogle()
search.test()
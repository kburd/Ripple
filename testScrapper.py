from configparser import ConfigParser
import unittest
import selenium
from bs4 import BeautifulSoup as bsoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import time
class PythonOrgSearch(unittest.TestCase):
    user = ""
    password = ""
    driverPath = ""
    url = ""
    def setUp(self):
        config = ConfigParser()
        config.read('config.ini')
        self.driverPath = config['driver']['driver']
        self.user = config['emdat']['user']
        self.password = config['emdat']['password']
        self.driver = webdriver.Chrome(self.driverPath)
        self.url = config['emdat']['url']
    def test_search_in_python_org(self):
        driver = self.driver
        url = self.url
        print(url)
        driver.get(self.url)
        time.sleep(4)
        #self.assertIn("emdat_db", driver.title)
        user = driver.find_element_by_id("textfield-1012-inputEl")
        user.send_keys(self.user)
        password = driver.find_element_by_id("textfield-1013-inputEl")
        password.send_keys(self.password)
        login = driver.find_element_by_id("button-1017-btnInnerEl")
        login.click()
        try:
            page = WebDriverWait(driver,10)
            profiles = page.until(EC.presence_of_element_located((By.XPATH,'//*[@id="button-1026-btnInnerEl"]')))
        except TimeoutException:
            print("Took to long to load page")
        profiles.click()
        time.sleep(1)
        # Country selection
        countryRadio = driver.find_element_by_id("radiofield-1055-inputEl")
        countryRadio.click()
        countryTop = driver.find_element_by_xpath('//*[@id="boundlist-1079-listEl"]/li[1]')
        countryBot = driver.find_element_by_xpath('//*[@id="boundlist-1079-listEl"]/li[230]')
        addBtn = driver.find_element_by_xpath('//*[@id="button-1085-btnIconEl"]')
        ActionChains(driver).key_down(Keys.SHIFT).click(countryTop).click(countryBot).key_up(Keys.SHIFT).perform()
        addBtn.click()
        # Disaster selection
        #time.sleep(20)
        climate = driver.find_element_by_xpath('//*[@id="treeview-1091-record-384"]/tbody/tr/td/div/input')
        aliens = driver.find_element_by_xpath('//*[@id="treeview-1091-record-385"]/tbody/tr/td/div/input')
        geo = driver.find_element_by_xpath('//*[@id="treeview-1091-record-386"]/tbody/tr/td/div/input')
        hydro = driver.find_element_by_xpath('//*[@id="treeview-1091-record-387"]/tbody/tr/td/div/input')
        meteor = driver.find_element_by_xpath('//*[@id="treeview-1091-record-388"]/tbody/tr/td/div/input')
        climate.click()
        aliens.click()
        geo.click()
        hydro.click()
        meteor.click()
        time.sleep(1)
        # Search options

        available = driver.find_element_by_xpath('//*[@id="boundlist-1095-listEl"]')
        searchAdd = driver.find_element_by_xpath('//*[@id="button-1101-btnIconEl"]')
        items = available.find_elements_by_tag_name("li")
        death =items[2]# driver.find_element_by_xpath('//*[@id="boundlist-1095-listEl"]/li[3]')
        death.click()
        searchAdd.click()
        available = driver.find_element_by_xpath('//*[@id="boundlist-1095-listEl"]')
        searchAdd = driver.find_element_by_xpath('//*[@id="button-1101-btnIconEl"]')
        items = available.find_elements_by_tag_name("li")
        damage = items[3]#driver.find_element_by_xpath('//*[@id="boundlist-1353-listEl"]/li[5]')
        damage.click()
        searchAdd.click()
        time.sleep(2)
        search = driver.find_element_by_xpath('//*[@id="button-1106-btnEl"]')
        search.click()
        time.sleep(5)
        try:
            page = WebDriverWait(driver,60,10)
            data = page.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gridview-1143-record-407"]/tbody/tr/td[1]/div')))
        except TimeoutException:
            print("No data available")
        time.sleep(15)
        html = driver.page_source
        soup = bsoup(html,'lxml')
        data = open("emdata.html",'w')
        data.write(str(soup.encode('utf-8')))

        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

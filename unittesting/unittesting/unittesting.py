import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_rus_city_eng_layout(self):
        driver = self.driver
        driver.get("http://2gis.ru/countries/global/")
        elem = driver.find_element_by_class_name("world__searchInput")
        elem.send_keys("yjdjcb,bhcr") #Новосибирск
        result = driver.find_elements_by_class_name("world__listItem")
        time.sleep(10)
        self.assertEqual(1, len(result))
        elem.send_keys(Keys.RETURN)

    def test_rus_city_translit(self):
        driver = self.driver
        driver.get("http://2gis.ru/countries/global/")
        elem = driver.find_element_by_class_name("world__searchInput")
        elem.send_keys("biisk")
        result = driver.find_elements_by_class_name("world__listItem")
        time.sleep(5)
        self.assertEqual(1, len(result))
        elem.send_keys(Keys.RETURN)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

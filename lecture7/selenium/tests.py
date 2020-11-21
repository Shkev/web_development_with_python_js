import os
import pathlib
import unittest

from selenium import webdriver

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

driver = webdriver.Safari()

class WebpageTests(unittest.TestCase):

    def setUp(self):
        self.uri = file_uri('counter.html')

    def test_title(self):
        driver.get(self.uri)
        self.assertEqual(driver.title, "Counter")

    def test_increase(self):
        driver.get(self.uri)
        increase = driver.find_element_by_id('increase')
        increase.click()
        self.assertEqual(driver.find_element_by_tag_name('h1').text, "1")

    def test_decrease(self):
        driver.get(self.uri)
        decrease = driver.find_element_by_id('decrease')
        decrease.click()
        self.assertEqual(driver.find_element_by_tag_name('h1').text, "-1")

    def test_multiple_increase(self):
        driver.get(self.uri)
        increase = driver.find_element_by_id('increase')
        for i in range(3):
            increase.click()
        self.assertEqual(driver.find_element_by_tag_name('h1').text, "3")

if __name__ == '__main__':
    unittest.main()

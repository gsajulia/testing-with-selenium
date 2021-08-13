import unittest

# Para manipular um elemento dropdown, declaramos ele como uma instância da classe Select
from selenium.webdriver.support.select import Select
from selenium import webdriver

class ExploreDegrees(unittest.TestCase):
    
    def test_checkbox1(self, driver):
        firstInput = Select(driver.find_element_by_id("__BVID__72"))

        options = ["Select degree type", "All degree", "Undergraduate", "Graduate", "Certificates"]
        i = 0

        for option in firstInput.options:
            self.assertEqual(option.text.lower(), options[i].lower())
            print(option.text)
            i =  i + 1

        firstInput.select_by_value("undergraduate")

    def checkbox2(self, driver):
        secondInput = Select(driver.find_element_by_id("__BVID__73"))
        secondInput.select_by_value("engineering-degrees")

    def button(self, driver):
        exploreButton = driver.find_element_by_link_text("Explore degrees")
        exploreButton.click()
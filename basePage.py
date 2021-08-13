import unittest
from selenium import webdriver

# Para manipular um elemento dropdown, declaramos ele como uma instância da classe Select
from selenium.webdriver.support.select import Select

class BasePage(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        #Precisa dessa linha abaixo e dos argumentos
        #Se fizermos normal da erro porque tentamos sobrescrever a classe init do TestCase
        super(BasePage, self).__init__(*args, **kwargs)

        print("Starting to test!")
        self.driver = webdriver.Firefox()
        self.driver.get("https://asuonline.asu.edu/")

    def checkbox1(self):
        firstInput = Select(self.driver.find_element_by_id("__BVID__72"))

        options = ["Select degree type", "All degree", "Undergraduate", "Graduate", "Certificates"]
        i = 0

        for option in firstInput.options:
            self.assertEqual(option.text.lower(), options[i].lower())
            print(option.text)
            i =  i + 1

        firstInput.select_by_value("undergraduate")

    def checkbox2(self):
        secondInput = Select(self.driver.find_element_by_id("__BVID__73"))
        secondInput.select_by_value("engineering-degrees")

    def button(self):
        exploreButton = self.driver.find_element_by_link_text("Explore degrees")
        exploreButton.click()

    def test_exploringDegrees(self):
        self.checkbox1()
        self.checkbox2()
        self.button()
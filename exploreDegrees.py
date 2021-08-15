import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep

# Para manipular um elemento dropdown, declaramos ele como uma instância da classe Select
from selenium.webdriver.support.select import Select


class ExploreDegrees(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        # Precisa dessa linha abaixo e dos argumentos
        # Se fizermos normal da erro porque tentamos sobrescrever a classe init do TestCase
        super(ExploreDegrees, self).__init__(*args, **kwargs)

        print("Starting to test!")

        PROXY = '31.184.201.40:8080'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f'--proxy-server={PROXY}')
        self.driver = webdriver.Chrome(options=chrome_options)

        self.driver.get("https://asuonline.asu.edu/")

    def dropdown1(self):
        # Elemento existe?
        try:
            firstInput = Select(self.driver.find_element_by_id("__BVID__72"))
            self.options = ["Select degree type", "All degree",
                            "Undergraduate", "Graduate", "Certificates"]
            i = 0

            # Verifica se as opções definidas são as mesmas que o elemento contém
            for option in firstInput.options:
                self.assertEqual(option.text.lower(), self.options[i].lower())
                i = i + 1

            firstInput.select_by_value("undergraduate")

        except NoSuchElementException:
            print("Dropdown1 not found")

    def dropdown2(self):
        try:
            secondInput = Select(self.driver.find_element_by_id("__BVID__73"))
            self.options = ["Select area of interest", "All interest area", "Art and design", "Business", "Communication and digital media",
                            "Computer science and technology", "Education", "Engineering", "Entrepreneurship and innovation", "Geographical sciences and urban planning",
                            "Health and wellness", "History", "Humanities", "Information technology", "Language", "Law, criminal justice and public service",
                            "Liberal arts", "Management", "Nursing", "Nutrition", "Psychology", "Science", "Social and behavioral sciences", "STEM", "Sustainability"]

            i = 0

            # Verifica se as opções definidas são as mesmas que o elemento contém
            for option in secondInput.options:
                self.assertEqual(option.text.lower(), self.options[i].lower())
                i = i + 1

            secondInput.select_by_value("engineering-degrees")

        except NoSuchElementException:
            print("Dropdown2 not found")

    def button(self):
        try:
            exploreButton = self.driver.find_element_by_link_text(
                "Explore degrees")
            exploreButton.click()
        except NoSuchElementException:
            print("Button not found")

    def checkbox(self):
        for x in range(3):
            try:
                thirdInput = self.driver.find_element_by_css_selector(
                    '#degree-type-filters-d177d116-78a2-42c7-bc77-d6a9badb9b5f')
                print(thirdInput.get_attribute('checked'))
                break
            except NoSuchElementException:
                print("Checkbox3 not found on attempt ", x+1, "/3")
                sleep(3)

    def test_exploringDegrees(self):
        self.dropdown1()
        self.dropdown2()
        self.button()
        self.checkbox()
        self.driver.quit()
        # self.driver.close()
        sleep(2)

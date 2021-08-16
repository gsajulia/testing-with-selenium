import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# Para manipular um elemento dropdown, declaramos ele como uma instância da classe Select
from selenium.webdriver.support.select import Select


class ExploreDegrees(unittest.TestCase):
    def setUp(self):
        print("Starting to test ExploreDegrees!")

        PROXY = '188.166.162.1:3128'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument('ignore-certificate-errors')
        chrome_options.add_argument("log-level=3")
        chrome_options.add_argument(f'--proxy-server={PROXY}')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)
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

    def checkboxes(self):
        try:
            firstCB = self.driver.find_element_by_css_selector(
                '#degree-type-filters-281f9709-6f72-4ed0-8e82-5ea0b30f34fe')
            self.assertIsNone(firstCB.get_attribute('checked'))

            secondCB = self.driver.find_element_by_css_selector(
                '#degree-type-filters-49eba34b-6648-45a3-8dd8-b9deb2ee2c93')
            self.assertFalse(secondCB.is_selected())

            thirdCB = self.driver.find_element_by_css_selector(
                '#degree-type-filters-d177d116-78a2-42c7-bc77-d6a9badb9b5f')
            self.assertTrue(thirdCB.get_attribute('checked'))
            # print(EC.visibility_of_element_located(By.CSS_SELECTOR(
            #    '#degree-type-filters-281f9709-6f72-4ed0-8e82-5ea0b30f34fe')))
        except NoSuchElementException:
            print("Checkboxes not found")
        sleep(2)
        try:
            cardsTitles = self.driver.find_elements_by_xpath(
                '/html/body/div[1]/main/section[2]/div/div/div[2]/div[4]/a/div/div[1]/p')
            for card in cardsTitles:
                self.assertEqual(card.get_attribute(
                    'innerText'), "Undergraduate")
        except NoSuchElementException:
            print("cards' titles not found")

    def test_exploringDegrees(self):
        self.dropdown1()
        self.dropdown2()
        self.button()
        self.checkboxes()
        print("----------test_exploringDegrees pass\n\n")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

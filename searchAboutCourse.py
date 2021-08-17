import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from time import sleep


class SearchAboutCourse(unittest.TestCase):
    def setUp(self):
        print("Starting to test SearchAboutCourse!")

        PROXY = '188.166.162.1:3128'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument('ignore-certificate-errors')
        chrome_options.add_argument("log-level=3")
        # chrome_options.add_argument(f'--proxy-server={PROXY}')
        self.driver = webdriver.Chrome(options=chrome_options)
        # self.driver.implicitly_wait(10)
        self.driver.get(
            "https://asuonline.asu.edu/study/tech-computer-science-degrees/")

    def input1(self):
        try:
            input = self.driver.find_element_by_xpath(
                "//input[@placeholder='Search']")
            input.clear()
            input.send_keys('web')

            # Confirmando se o texto do search está certo
            input = self.driver.find_element_by_xpath(
                "//input[@placeholder='Search']")
            self.assertEqual(input.get_attribute('value'), 'web')

        except NoSuchElementException:
            print("search input not found")
            self.assertTrue(False)

    def card(self):
        try:
            sleep(2)
            # Testando se a imagem existe no card e se o total de imagens está correto
            imageOfCard = self.driver.find_elements_by_class_name(
                "degree-search-card-image")
            self.assertTrue(len(imageOfCard) == 2)

            # Testando se a quantidade é igual a quantidade esperada
            cardTopElem = self.driver.find_element_by_xpath(
                "//*[contains(text(), 'programs total')]")
            self.assertIn(str(len(imageOfCard)), cardTopElem.text)

            # Testando se o que foi digitado no search ocorre nos títulos
            cardBottomElem = self.driver.find_elements_by_xpath(
                "//div[@class='card-body degree-search-card-body']//h3")
            for elem in cardBottomElem:
                # print("-------------Opções de cards: ", elem.text)
                self.assertIn("web", elem.text.lower())

        except NoSuchElementException:
            print("some element isnt in card")

    def test_1_searchAboutComputerScience(self):
        self.input1()
        self.card()
        print("1----------test_searchAboutComputerScience pass\n\n")
        sleep(10)

    def test_2_page_title(self):
        try:
            title = self.driver.find_element_by_tag_name("h1")
            self.assertEqual(
                "Computer science and technology degrees", title.text)
            print("2----------test_page_title pass\n\n")

        except NoSuchElementException:
            print("h1 not found")
            self.assertTrue(False)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

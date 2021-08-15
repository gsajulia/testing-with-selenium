import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep 
from selenium.webdriver.common.action_chains import ActionChains

class SearchAboutCourse(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(SearchAboutCourse, self).__init__(*args, **kwargs)
        self.driver = webdriver.Firefox()
        self.driver.get("https://asuonline.asu.edu/")

    def link1(self):
        try:
            link = self.driver.find_element_by_link_text("Browse Areas of Study")
            self.driver.execute_script("arguments[0].scrollIntoView();", link)
            link.click()

        except NoSuchElementException:
            print("link1 not found")

    def button1(self):
        try:
            self.url = "https://asuonline.asu.edu/study/tech-computer-science-degrees/"
            elems = self.driver.find_elements_by_xpath("//a[@href]")
            for elem in elems:
                if(elem.get_attribute("href") == self.url):
                    button = elem

            button.click()

        except NoSuchElementException:
            print("link1 not found")
    
    def input(self):
        try:
            input = self.driver.find_element_by_xpath("//input[@placeholder='Search']")
            input.clear()
            input.send_keys('web')

        except NoSuchElementException:
            print("search input not found")

    def card(self):
        try:
            sleep(2)
            # Testando se a imagem existe no card e se o total de imagens está correto
            imageOfCard = self.driver.find_elements_by_class_name("degree-search-card-image")
            self.assertTrue(len(imageOfCard) == 2)

            # Testando se a quantidade é igual a quantidade esperada
            cardTopElem = self.driver.find_element_by_xpath("//*[contains(text(), 'programs total')]")
            self.assertIn(str(len(imageOfCard)), cardTopElem.text)

            # Testando se o que foi digitado no search ocorre nos títulos
            cardBottomElem = self.driver.find_elements_by_xpath("//div[@class='card-body degree-search-card-body']//h3")
            for elem in cardBottomElem:
                print("-------------Opções de cards: ", elem.text)
                self.assertIn("web", elem.text.lower())

            

        except NoSuchElementException:
            print("something is wrong in card")

    def test_searchAboutComputerScience(self):
        self.link1()
        self.button1()
        self.input()
        self.card()
        sleep(10)


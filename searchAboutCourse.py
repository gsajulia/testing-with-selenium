import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class SearchAboutCourse(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(SearchAboutCourse, self).__init__(*args, **kwargs)
        self.driver = webdriver.Firefox()
        self.driver.get("https://asuonline.asu.edu/")

    def link1(self):
        try:
            link = self.driver.find_element_by_link_text("Browse Areas of Study")
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

    def test_searchAboutComputerScience(self):
        self.link1()
        self.button1()

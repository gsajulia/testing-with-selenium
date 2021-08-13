import unittest
from basePage import ExploreDegrees
from selenium import webdriver

def main():
    print("Starting to test!")
    driver = webdriver.Firefox()
    driver.get("https://asuonline.asu.edu/")

    # Explorando títulos
    exploreDegrees = ExploreDegrees()
    
    exploreDegrees.test_checkbox1(driver)
    exploreDegrees.checkbox2(driver)
    exploreDegrees.button(driver)


if __name__ == "__main__":
    unittest.main()
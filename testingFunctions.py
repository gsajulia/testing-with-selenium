# Para manipular um elemento dropdown, declaramos ele como uma instância da classe Select
from selenium.webdriver.support.select import Select

def exploreDegrees(driver):
    firstInput = Select(driver.find_element_by_id("__BVID__72"))
    firstInput.select_by_value("undergraduate")

    secondInput = Select(driver.find_element_by_id("__BVID__73"))
    secondInput.select_by_value("engineering-degrees")

    exploreButton = driver.find_element_by_link_text("Explore degrees")
    exploreButton.click()
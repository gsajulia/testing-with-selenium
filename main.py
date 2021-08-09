import testingFunctions
from selenium import webdriver

def main():
    print("Starting to test!")
    driver = webdriver.Firefox()
    driver.get("https://asuonline.asu.edu/")
    testingFunctions.exploreDegrees(driver)


if __name__ == "__main__":
    main()
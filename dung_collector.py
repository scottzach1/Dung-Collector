import time
import sys

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException, \
    ElementNotInteractableException


DUNG_CLASS_NAME = 'dung'

driver = webdriver.Chrome()
driver.get("https://dunghero.online/")


# Wait reasonable time until elements should appear on screen.
time.sleep(2)
dungs = driver.find_elements_by_class_name(DUNG_CLASS_NAME)
successes = 0
failures = 0

while dungs:
    # Keep looping if we are finding more dung.
    for dung in dungs:
        try:
            # click_action = Action(dung)
            # dung.click()
            driver.execute_script('arguments[0].click()', dung)
            successes += 1
            time.sleep(0.25)
            # Success if makes to here.
        except ElementClickInterceptedException or StaleElementReferenceException or ElementNotInteractableException:
            # We only care about counting our failures here.
            failures += 1
        finally:
            # Update the tallies in the console.
            sys.stdout.write('\r')
            sys.stdout.flush()
            sys.stdout.write("Success " + str(successes) + " / " + str(successes + failures) + " Total")

    # Get some more dung.
    dungs = driver.find_elements_by_class_name(DUNG_CLASS_NAME)


driver.close()

import time
import sys

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException

DUNG_CLASS_NAME = 'dung'

driver = webdriver.Chrome()
driver.get("https://dunghero.online/")


# Wait until turds appear on the screen.
driver.implicitly_wait(10)
dungs = driver.find_elements_by_class_name(DUNG_CLASS_NAME)
successes = 0
failures = 0

while dungs:
    # Keep looping if we are finding more dung.
    for dung in dungs:
        try:
            # Click element using javascript.
            driver.execute_script('arguments[0].click()', dung)
            successes += 1
            # Sleep just enough time that the site registers events.
            time.sleep(0.1)
            # Success if makes to here.
        except StaleElementReferenceException:
            # We only care about counting our failures here.
            failures += 1
        finally:
            # Update the tallies in the console.
            sys.stdout.write('\r')
            sys.stdout.flush()
            sys.stdout.write("Success " + str(successes) + " / " + str(successes + failures) + " Total")

    # Get some more dung (waiting up to 10 seconds for more to appear).
    driver.implicitly_wait(10)
    dungs = driver.find_elements_by_class_name(DUNG_CLASS_NAME)

# Close the web browser session.
driver.close()

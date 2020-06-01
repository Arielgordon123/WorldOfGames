import os
import sys
from pathlib import Path
from selenium import webdriver
from dotenv import load_dotenv
load_dotenv(dotenv_path=Path('../.env'))


def test_scores_service(app_url):
    result = False
    try:
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        chrome_browser = webdriver.Firefox(options=options)

        chrome_browser.get(app_url)
        score = chrome_browser.find_element_by_id("score")
        result = 1 <= int(score.text) and int(score.text) <= 1000
    finally:
        chrome_browser.quit()
    return result


def main_function():
    if test_scores_service(os.getenv('APP_URL')):
        sys.exit(0)
    else:
        sys.exit(-1)


main_function()

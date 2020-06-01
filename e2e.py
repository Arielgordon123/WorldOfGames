import selenium.webdriver as webdriver

def test_scores_service(app_url):
    chrome_browser = webdriver.Chrome()

    chrome_browser.get(app_url)

    score = chrome_browser.find_element_by_id("score")

def main_function():
    pass

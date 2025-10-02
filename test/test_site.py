
import time
from pages.homepage import Homepage
from pages.product import ProductPage


def test_open_s6(browser):
    homepage = Homepage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(browser)
    product_page.check_title_is('Samsung galaxy s6')

 
def test_two_monitors(browser):
    homepage = Homepage(browser)
    homepage.open()
    # browser.get('https://demoblaze.com/index.html')
    homepage.click_monitor()
    # monitor_link = browser.find_element(By.CSS_SELECTOR, '''onclick="byCat('monitor')"''')
    # monitor_link.click()
    #time.sleep(2)
    homepage.check_that_products_count(2)  
    # monitors = browser.find_elements(By.CSS_SELECTOR, '.card')
    # assert len(monitors) == 2


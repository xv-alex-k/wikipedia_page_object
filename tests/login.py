from selenium import webdriver

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.topic_page import TopicPage

# executable_path = path_to_chromedriver
driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.implicitly_wait(5)

# test 1 - Valid Search
driver.get("https://en.wikipedia.org/")
main_page = MainPage(driver)
main_page.search_for("Automated testing")
assert "Test automation" in main_page.get_topic_title()

# test 2 - Invalid Search
driver.get("https://en.wikipedia.org/")
main_page = MainPage(driver)
main_page.search_for("qwe")

search_results_page = SearchResultsPage(driver)
assert "Quechuan languages" in driver.page_source

# test 3 - Successful login
username = "your_username"
password = "your_password"
driver.get("https://en.wikipedia.org/w/index.php?title=Special:UserLogin")
login_page = LoginPage(driver)
login_page.enter_username(username)
login_page.enter_password(password)
login_page.click_login_button()

main_page = MainPage(driver)
assert username in main_page.get_username()

driver.quit()

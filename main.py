from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
from Bot import InternetSpeedBot
Chrome_driver_path = "C:/Users/Haresh/PycharmProjects/chromedriver_win32/chromedriver.exe"

driver = InternetSpeedBot(Chrome_driver_path)
driver.tweet_at_provider()
# driver.get_internet_speed()
# driver.get("https://twitter.com/login")

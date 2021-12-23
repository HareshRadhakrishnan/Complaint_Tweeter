from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
class InternetSpeedBot:
    def __init__(self,driver_path ):

        self.PROMISED_DOWNLOAD = 150
        self.PROMIED_UPLOAD = 20
        self.driver = webdriver.Chrome(executable_path=driver_path)
    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()
        sleep(90)
        down = self.driver.find_element_by_class_name('download-speed').text
        print(down)
        up = self.driver.find_element_by_class_name('upload-speed').text
        print(up)
    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/home')
        sleep(2)
        txt_username = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        txt_username.send_keys("HareshRadhakri1")

        txt_password = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        txt_password.send_keys("MyPa$$w0rd")
        txt_password.send_keys(Keys.ENTER)
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a').click()
        sleep(5)
        txt_tweet = self.driver.find_element_by_css_selector('[data-block="true"]')
        txt_tweet.send_keys('This is my message')
        btn_tweet  = self.driver.find_element_by_css_selector('[data-testid="tweetButtonInline"]')
        sleep(1)
        self.driver.execute_script("arguments[0].click();",btn_tweet)
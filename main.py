from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
import time


PROMISED_UP = 50

TWITTER_EMAIL = "My e-mail"
TWITTER_PASSWORD = "My password"


chrome_driver_path = "my path"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = uc.Chrome(service=Service(executable_path=driver_path))
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        speedtest_url = "https://www.speedtest.net/"
        self.driver.get(speedtest_url)
        time.sleep(3)
        go = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]")
        go.click()
        time.sleep(60)
        down = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span")
        print(down.text)
        up = self.driver.find_element(By.XPATH,
                                        "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")
        print(up.text)
        self.down = float(down.text)
        self.up = float(up.text)

    def tweet_at_provider(self, email, password):
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for 50 mbps?"

        self.driver.get("https://twitter.com/")
        time.sleep(3)
        login = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/a")
        login.click()
        time.sleep(2)
        input_bottom = self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        input_bottom.send_keys(email)
        time.sleep(1)
        next_bottom = self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]")
        next_bottom.click()
        time.sleep(3)
        input_password = self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        input_password.send_keys(password)
        time.sleep(2)
        input_password.send_keys(Keys.ENTER)
        time.sleep(60)
        select_write = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div")
        select_write.click()
        time.sleep(2)
        message = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div")
        message.send_keys(tweet)
        time.sleep(3)
        send_tweet = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]")
        send_tweet.click()




TwitterBot = InternetSpeedTwitterBot(chrome_driver_path)

TwitterBot.get_internet_speed()
if TwitterBot.up < PROMISED_UP:
    TwitterBot.tweet_at_provider(TWITTER_EMAIL, TWITTER_PASSWORD)

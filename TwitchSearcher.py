import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import selenium.common.exceptions
import random


class TwitchSearcher:
    def __init__(self, timeout=15):
        service = Service(ChromeDriverManager().install())
        options = Options()
        options.add_experimental_option("mobileEmulation", {"deviceName": "iPhone SE"})
        self.driver = webdriver.Chrome(service=service, options=options)
        options.add_argument("--start-maximized")
        self.wait = WebDriverWait(self.driver, timeout)
        channels = []

    def gotoWeb(self, url):
        self.driver.get(url)
        time.sleep(2)

    def search(self, keyword):
        search_button = self.driver.find_element(By.XPATH, "(//div[contains(@class, 'iwaIid')])[2]")
        search_button.click()
        time.sleep(2)
        search_box = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="search"]'))
        )
        search_box.send_keys(keyword)
        print(f"Entering search page : {keyword}")
        search_box.send_keys("\n")
        time.sleep(2)

        video_list_button = self.driver.find_element(By.XPATH, "(//div[contains(@class, 'gesXMd')])[2]")
        video_list_button.click()
        time.sleep(2)

    def scroll(self, times):
        for _ in range(times):
            self.driver.execute_script("window.scrollBy(0, 1000);")
            time.sleep(3)
            print("Scrolling")

    def gotoChannel(self, channel_name):
        try:
            channel_link = self.wait.until(
                    EC.presence_of_all_elements_located(
                        (By.CSS_SELECTOR, '.cZfgmJ')
                        )
                    )
            for el in channel_link:
                text = el.text.strip()
                if channel_name in text:
                    print(f"Go to channel: {el.get_attribute('href')}")
                    el.click()
                    break
                else:
                    print("No matching channel")
        except:
            print("Can't find channl")
            return False
        try:
            ad = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '.ad-banner__message'))
                    )
            WebDriverWait(driver, 180).until_not(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '.ad-banner__message'))
                    )
        except:
            print("")

        time.sleep(5)
    def gotoRandomChannel(self):
        streamers = self.wait.until(
                EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, 'button.cZfgmJ')
                    )
                )

        print(f"{len(streamers)} channels found")

        if streamers:
            for streamer in streamers:
                try:
                    streamer.click()
                except selenium.common.exceptions.ElementClickInterceptedException:
                    continue
                except selenium.common.exceptions.StaleElementReferenceException:
                    continue
                break
            print("Entering channel")
            time.sleep(15)
        else:
            print("\n No channel")


        try:
            ad = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '.ad-banner__message'))
                    )
            WebDriverWait(self.driver, 180).until_not(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '.ad-banner__message'))
                    )
        except:
            print("")

        time.sleep(5)

    def screenshot(self):
        self.driver.save_screenshot("selected_channel.png")
        print("已截圖 selected_channel.png")


    def quit(self):
        self.driver.quit()

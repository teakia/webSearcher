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
from urllib.parse import urlparse
from selenium.webdriver.common.action_chains import ActionChains



class TwitchSearcher:
    def __init__(self, timeout=15):
        service = Service(ChromeDriverManager().install())
        options = Options()
        self.driver = webdriver.Chrome(service=service, options=options)
        options.add_argument("--start-maximized")
        self.wait = WebDriverWait(self.driver, timeout)
        channels = []

    def gotoWeb(self, url):
        self.driver.get(url)
        time.sleep(5)

    def search(self, keyword):
        search_box = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Search" or @placeholder="搜尋"]'))
        )
        search_box.send_keys(keyword)
        search_box.send_keys("\n")
        time.sleep(5)

    def scroll(self):
        actions = ActionChains(self.driver)

        window_size = self.driver.get_window_size()
        center_x = window_size['width'] // 2
        center_y = window_size['height'] // 2
        actions.move_by_offset(center_x, center_y).perform()
        time.sleep(0.5)
        print('lala')
        actions.move_by_offset(200, 0).perform()
        time.sleep(0.5)
        print('lala')
        actions.move_by_offset(-200, 0).perform()
        time.sleep(0.5)
        print('lala')
        actions.move_by_offset(200, 0).perform()
        time.sleep(0.5)
        print('lala')

    def gotoChannel(self, channel_name, blacklist):
        try:
            channel_link = self.wait.until(
                    EC.presence_of_all_elements_located(
                        (By.XPATH, f'//div[@data-a-target="search-result-live-channel"//a and .//p[text()="{channel_name}"]]')
                        )
                    )
            print(f"Go to channel: {channel_link.get_attribute('href')}")
            channel_link.click()
            return True
        except:
            print("Can't find channl")
            return False
        channel_links = set()
        for ch in channel_link:
            href = ch.get_attribute("href")
            if not href:
                continue
            if any(bad in href for bad in blacklist):
                continue
            if urlparse(href).path.count('/') == 1:
                channel_links.add(href)
        print(f"\n共 {len(channel_links)} 個頻道：")
        for i, link in enumerate(channel_links, 1):
            print(f"[{i}] {link}")

        if channel_links:
            selected_link = channel_links[0]
            print(f"\n Selected link：{selected_link}")
            driver.get(selected_link)
            time.sleep(15)
        else:
            print("")


        try:
            ad = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '.ad-banner__message'))
                    )
            WebDriverWait(driver, 180).until_not(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '.ad-banner__message'))
                    )
        except:
            print("")


    def gotoRandomChannel(self, blacklist):
        channels = self.wait.until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, '//div[@data-a-target="search-result-live-channel"]//a')
                    )
                )

        channel_links = set()
        for ch in channels:
            href = ch.get_attribute("href")
            if not href:
                continue
            if any(bad in href for bad in blacklist):
                continue
            if urlparse(href).path.count('/') == 1:
                channel_links.add(href)
        print(f"\n共 {len(channel_links)} 個頻道：")
        for i, link in enumerate(channel_links, 1):
            print(f"[{i}] {link}")

        if channel_links:
            selected_link = random.choice(list(channel_links))
            print(f"\n Selected link：{selected_link}")
            self.driver.get(selected_link)
            time.sleep(15)
        else:
            print("\n No channel")


        try:
            ad = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '.ad-banner__message'))
                    )
            WebDriverWait(driver, 180).until_not(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '.ad-banner__message'))
                    )
        except:
            print("")



    def screenshot(self):
        self.driver.save_screenshot("selected_channel.png")
        print("已截圖 selected_channel.png")


    def quit(self):
        self.driver.quit()

'''        
def __init
desLink ="https://www.twitch.tv/"
driver_path = "./chromedriver-linux64/chromedriver"
service = Service(driver_path)
options = Options()
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 15)

driver.get(desLink)
time.sleep(5)

search_box = wait.until(
    EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Search" or @placeholder="搜尋"]'))
)
search_box.send_keys("StarCraft II")
search_box.send_keys(Keys.RETURN)
time.sleep(5)  


for _ in range(5):
    driver.execute_script("window.scrollBy(0, 20);")
    time.sleep(2)


channels = wait.until(
        EC.presence_of_all_elements_located(
            (By.XPATH, '//div[@data-a-target="search-result-live-channel"]//a')
            )
        )


blacklist = ["/directory/", "/videos/", "/collections/", "/clip/", "/schedule"]
channel_links = set()
for ch in channels:
    href = ch.get_attribute("href")
    if not href:
        continue
    if any(bad in href for bad in blacklist):
        continue
    if urlparse(href).path.count('/') == 1:
        channel_links.add(href)
print(f"\n共 {len(channel_links)} 個頻道：")
for i, link in enumerate(channel_links, 1):
    print(f"[{i}] {link}")


if channel_links:
    selected_link = random.choice(list(channel_links))
    print(f"\n Selected link：{selected_link}")
    driver.get(selected_link)
    time.sleep(15)
else:
    print("\n⚠️No channel")


try:
    ad = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.ad-banner__message'))
    )
    WebDriverWait(driver, 180).until_not(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.ad-banner__message'))
    )
except:
    print("")

driver.save_screenshot("selected_channel.png")
print("已截圖 selected_channel.png")

driver.quit()
'''

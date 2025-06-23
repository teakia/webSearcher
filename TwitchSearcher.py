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
        time.sleep(5)

    def search(self, keyword):
        search_button = self.driver.find_element(By.XPATH, "(//div[contains(@class, 'iOKESX')])[2]")
        search_button.click()
        time.sleep(5)
        search_box = self.wait.until(
    EC.presence_of_element_located((By.XPATH, '//input[@type="search"]'))
)
        search_box.send_keys(keyword)
        search_box.send_keys("\n")
        time.sleep(5)

    def scroll(self):
        for _ in range(2):
            self.driver.execute_script("window.scrollBy(0, 300);")
            time.sleep(1)
            print("Scrolling")

    def gotoChannel(self, channel_name, blacklist):
        try:
            channel_link = self.wait.until(
                    EC.presence_of_all_elements_located(
                        (By.XPATH, f'//div[@data-a-target="search-result-card"//a and .//p[text()="{channel_name}"]]')
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

        time.sleep(5)

    def gotoRandomChannel(self, blacklist):
        channels = self.wait.until(
                EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, '.search-result-card__img.tw-image')
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

        time.sleep(5)


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

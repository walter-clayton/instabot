
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys, os

sys.path.append(os.path.join(sys.path[0], "../../"))

def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()


class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path='./chromedriver')

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        cookie_button = driver.find_element_by_xpath("//button[text()='Accept All']")
        cookie_button.click()
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        time.sleep(2)
        passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        passworword_elem.send_keys(Keys.RETURN)
        time.sleep(5)
        bot.upload_photo("book.png", caption="My top book for the year 2020. Product Led Growth gives you a good insight on how to build a SAAS product that can sell. Post Designed with @canva #belgiumtechnology #tech2021 #techpodcast #saas #toptechbook #webdeveloper #frontenddeveloper")
        
    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)

        # gathering photos
        pic_hrefs = []

        for i in range(1, 7):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                # get tags
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                # finding relevant hrefs
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                 if '.com/p/' in elem.get_attribute('href')]
                # building list of unique photos
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
                # print("Check: pic href length " + str(len(pic_hrefs)))
            except Exception:
                continue

        # Liking photos
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            like_button = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/section[1]/main[1]/div[1]/div[1]/article[1]/div[3]/section[1]/span[1]/button[1]')
            time.sleep(5)
            like_button.click()
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


if __name__ == "__main__":

    ig = InstagramBot('clayton.tech', 'spongei94')
    ig.login()

    hashtags = ['brussels', 'belgium']

    while True:
        try:
            # Choose a random tag from the list of tags
            tag = random.choice(hashtags)
            ig.like_photo(tag)
        except Exception:
            ig.closeBrowser()
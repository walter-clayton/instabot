#!/usr/bin/python
# - * - coding: utf-8 - * -
from instabot import Bot 
from random import randint
import time

my_bot = Bot()

my_bot.login(username="clayton.text", password="")

# upload photo
my_bot.upload_photo("./pictures/product-led-growth.jpg", caption="Bush reveals how your product—not expensive sales teams—can be the main vehicle to acquire, convert, and retain customers")

# unfollow 
following_list = my_bot.get_user_followers("clayton.tech")
print(following_list)
followers_list = my_bot.get_user_following("clayton.tech")
print(followers_list)
non_followers = set(followers_list)==set(following_list)
time.sleep(randint(5,10))

for non_follower in non_followers:
    try:
        my_bot.unfollow(non_followers)
        time.sleep(randint(10,15))
    except Exception as e:
        print(e)
        time.sleep(randint(50,100))
        
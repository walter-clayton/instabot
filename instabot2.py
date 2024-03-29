#!/usr/bin/python
# - * - coding: utf-8 - * -
from __future__ import unicode_literals

import argparse
import os
import sys

import captions_for_medias

sys.path.append(os.path.join(sys.path[0], "../../"))
from instabot import Bot  # noqa: E402


parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-u", type=str, help="clayton.tech")
parser.add_argument("-p", type=str, help="spongei94")
parser.add_argument("-proxy", type=str, help="proxy")
parser.add_argument("-photo", type=str, help="book")
parser.add_argument("-caption", type=str, help="My top book for the year 2020. Product Led Growth gives you a good insight on how to build a SAAS product that can sell. Post Designed with @canva #belgiumtechnology #tech2021 #techpodcast #saas #toptechbook #webdeveloper #frontenddeveloper")
parser.add_argument('-tag', action='append', help='clayton.tech')

args = parser.parse_args()

bot = Bot()
bot.login()

posted_pic_file = "pics.txt"

posted_pic_list = []
caption = "My top book for the year 2020. Product Led Growth gives you a good insight on how to build a SAAS product that can sell. Post Designed with @canva #belgiumtechnology #tech2021 #techpodcast #saas #toptechbook #webdeveloper #frontenddeveloper"

if not os.path.isfile(posted_pic_file):
    with open(posted_pic_file, "w"):
        pass
else:
    with open(posted_pic_file, "r") as f:
        posted_pic_list = f.read().splitlines()

# Get the filenames of the photos in the path ->
if not args.photo:
    import glob

    pics = []
    exts = ["jpg", "JPG", "jpeg", "JPEG", "png", "PNG"]
    for ext in exts:
        pics += [os.path.basename(x) for x in glob.glob("media/*.{}".format(ext))]
    from random import shuffle

    shuffle(pics)
else:
    pics = [args.photo]
pics = list(set(pics) - set(posted_pic_list))
if len(pics) == 0:
    if not args.photo:
        bot.logger.warn("NO MORE PHOTO TO UPLOAD")
        exit()
    else:
        bot.logger.error("The photo `{}` has already been posted".format(pics[0]))
try:
    for pic in pics:
        bot.logger.info("Checking {}".format(pic))
        if args.caption:
            caption = args.caption
        else:
            if captions_for_medias.CAPTIONS.get(pic):
                caption = captions_for_medias.CAPTIONS[pic]
            else:
                try:
                    caption = raw_input(
                        "No caption found for this media. " "Type the caption now: "
                    )
                except NameError:
                    caption = input(
                        "No caption found for this media. " "Type the caption now: "
                    )
        bot.logger.info(
            "Uploading pic `{pic}` with caption: `{caption}`".format(
                pic=pic, caption=caption
            )
        )

        # prepare tagged user_id
        users_to_tag = [{'user_id': u, 'x': 0.5, 'y': 0.5} for u in args.tag]

        if not bot.upload_photo(
            os.path.dirname(os.path.realpath(__file__)) + "/media/" + pic,
            caption=caption,
            user_tags=users_to_tag
        ):
            bot.logger.error("Something went wrong...")
            break
        posted_pic_list.append(pic)
        with open(posted_pic_file, "a") as f:
            f.write(pic + "\n")
        bot.logger.info("Succesfully uploaded: " + pic)
        break
except Exception as e:
    bot.logger.error("\033[41mERROR...\033[0m")
    bot.logger.error(str(e))
import praw
import pdb
import re
import os
from config_bot import *

# If config file is missing, displays error message
if not os.path.isfile("config_bot.py"):
    print("You must create a config file with your username and password.")
    print("Please see config_skel.py.")
    exit(1)

user_agent = ("PyFor Eng bot 0.1")
r = praw.Reddit(user_agent=user_agent)

r.login(REDDIT_USERNAME, REDDIT_PASS)

# if txt file for post_id storage is missing or not created, makes a list to store post_ids in
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
# otherwise opens txt file, reads it, splits each line into a new list item, filters out lines without values in them
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = filter(None, posts_replied_to)

# if top 5 post in the "hot" section has "i love python" in the title and it hasn't been touched by the bot, bot posts a comment on it
subreddit = r.get_subreddit("pythonforengineers")
for submission in subreddit.get_hot(limit=5):
    if submission.id not in posts_replied_to:
        if re.search("i love python", submission.title, re.IGNORECASE):
            submission.add_comment("Botty bot says: Me too!!")
            print("Bot replying to : ", submission.title)
            posts_replied_to.append(submission.id)

# write all new post_ids to the txt file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")

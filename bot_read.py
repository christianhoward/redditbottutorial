# File used to understand how the praw package reads reddit
import praw

user_agent = ("PyEng Bot 0.1")

r = praw.Reddit(user_agent = user_agent)

subreddit = r.get_subreddit("learnpython")

# gets 5 posts based on the "hot" section of the subreddit and prints the title, text and aggregate up/down vote
for submission in subreddit.get_hot(limit = 5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")

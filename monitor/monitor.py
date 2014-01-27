import praw
import time
import re

# access Reddit with user_agent
reddit = praw.Reddit("Subreddit Monitor by github.com/pixelvirus/")

# login
reddit.login()

# obtain subreddit
sr = raw_input("\nWhich subreddit to monitor? ")

# obtain keywords
keywords = raw_input("\nKeywords to look for? (separate with comma) ")
# slice string into a list of words
wordlist = re.sub("[^\w]", " ",  keywords).split()

# obtain number of posts to monitor
number = raw_input("\nHow many top posts to monitor? ")

print "\nBot is now monitoring r/{name}\n".format(name=sr)

# stores submission IDs that has already been processed
completed = []

while True:
    subreddit = reddit.get_subreddit(sr)
    for submission in subreddit.get_hot(limit=number):
        text = submission.selftext.lower()
        found = any(string in text for string in wordlist)
        if submission.id not in completed and found:
            msg = "Post found matching keyword(s): {link}".format(link=submission.short_link)
            reddit.user.send_message('pixelvirus', msg)
            completed.append(submission.id)
    time.sleep(1800)
import praw
import getpass
import re
import time

# access Reddit with user_agent
reddit = praw.Reddit("Subreddit Monitor by github.com/pixelvirus/")

# login - add to praw.ini for autologin
username = raw_input("Username? ")
password = getpass.getpass("Password? ")
print "\nLogging in..."
reddit.login(username, password)

# obtain subreddit
sr = raw_input("\nWhich subreddit to monitor? ")

# obtain keywords
keywords = raw_input("\nKeyword(s) to look for? (separate with comma) ")
# slice string into a list of words
wordlist = re.sub("[^\w]", " ",  keywords).split()

# obtain message receiver
receiver = raw_input("\nWhich user should receive the notifications? ")
redittor = reddit.get_redditor(receiver)

print "\nThe bot is now monitoring r/{name}\n".format(name=sr)

# stores submission IDs that has already been processed
completed = []

while True:
    subreddit = reddit.get_subreddit(sr)
    for submission in subreddit.get_hot(limit=25):
        text = submission.selftext.lower()
        # look for keyword in top 25 posts
        found = any(string in text for string in wordlist)
        # send a message if found is true and not already sent
        if submission.id not in completed and found:
            msg = "Post matching keyword(s) found: {link}".format(link=submission.short_link)
            redittor.send_message('pixelvirus', msg)
            print "Post matching keyword(s) found. Message sent to {name}".format(name=receiver)
            completed.append(submission.id)
    time.sleep(1800)
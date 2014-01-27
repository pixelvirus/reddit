import praw
import re
import time

# access Reddit with user_agent
reddit = praw.Reddit("Subreddit Monitor by github.com/pixelvirus/")

# login
#username = raw_input("Username? ")
#password = raw_input("\nPassword? ")
#print "\nLogging in...\n"
reddit.login()#(username, password)

# obtain subreddit
sr = raw_input("\nWhich subreddit to monitor? ")

# obtain keywords
keywords = raw_input("\nKeywords to look for? (separate with comma) ")
# slice string into a list of words
wordlist = re.sub("[^\w]", " ",  keywords).split()

# obtain number of posts to monitor
number = raw_input("\nHow many top posts to monitor? ")

print "\nThe bot is now monitoring r/{name}\n".format(name=sr)

# stores submission IDs that has already been processed
completed = []

while True:
    subreddit = reddit.get_subreddit(sr)
    for submission in subreddit.get_hot(limit=number):
        # returns submission text
        text = submission.selftext.lower()
        # returns submission title
        title = submission.selftext.lower()
        # look for keyword in text and title
        found = any(string in text or title for string in wordlist)
        # send a message if found and not already sent
        if submission.id not in completed and found:
            msg = "Post matching keyword(s) found: {link}".format(link=submission.short_link)
            reddit.user.send_message('pixelvirus', msg)
            print "\nPost matching keyword(s) found. Message sent to {name}\n".format(name=username)
            completed.append(submission.id)
    time.sleep(1800)
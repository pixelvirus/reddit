import praw

# access Reddit with user_agent
reddit = praw.Reddit("Karma Breadown by github.com/pixelvirus/")
# obtain username
user_name = raw_input("\nWelcome!\n\nWhat is your reddit username? ")

# return a Redditor instance
redditor = reddit.get_redditor(user_name)
# obtain sorting preference
order = raw_input("\nSort in (d)escending or (a)scending order? ")

print "\nGetting your karma breakdown...this might take a few seconds\n"
# return a list of Submission contents
content = redditor.get_submitted(limit=None)

karma = {}
# calculate karma of all subreddits
for thing in content:
    subreddit = thing.subreddit.display_name
    karma[subreddit] = (karma.get(subreddit, 0) + thing.score)

# sort karma
if "d" in order:
    karma_sorted = sorted(karma, key=lambda x : karma[x], reverse=True)
elif "a" in order:
    karma_sorted = sorted(karma, key=lambda x : karma[x])
else:
    karma_sorted = karma

# print
for subreddit in karma_sorted:
    print "r/{name}: {karma}".format(name=subreddit, karma=karma[subreddit])
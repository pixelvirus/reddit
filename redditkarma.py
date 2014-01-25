import praw

user_agent = ("Karma Breadown by Subreddits by github.com/retropixelvirus/")
r = praw.Reddit(user_agent=user_agent)

user_name = raw_input("Welcome! What is your reddit username? ")

user = r.get_redditor(user_name)
gen = user.get_submitted(limit=None)

print "Getting your karma breakdown...\n"

karma = {}
for thing in gen:
    subreddit = thing.subreddit.display_name
    karma[subreddit] = (karma.get(subreddit, 0) + thing.score)
	
for subreddit in karma:
    print "r/{name}: {karma}".format(name=subreddit, karma=karma[subreddit])
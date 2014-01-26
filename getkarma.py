import praw

user_agent = ("Karma Breadown by Subreddits by github.com/pixelvirus/")
r = praw.Reddit(user_agent=user_agent)

user_name = raw_input("\nWelcome!\n\nWhat is your reddit username? ")

user = r.get_redditor(user_name)
gen = user.get_submitted(limit=None)

sort_case = raw_input("\nSort in descending or ascending order? ('d' or 'a') ")

print "\nGetting your karma breakdown...this might take a few seconds\n"

karma = {}
for thing in gen:
    subreddit = thing.subreddit.display_name
    karma[subreddit] = (karma.get(subreddit, 0) + thing.score)

if "d" in sort_case:
    karma_sorted = sorted(karma, key=lambda x : karma[x], reverse=True)
elif "a" in sort_case:
    karma_sorted = sorted(karma, key=lambda x : karma[x])
else:
	karma_sorted = karma

for subreddit in karma_sorted:
    print "r/{name}: {karma}".format(name=subreddit, karma=karma[subreddit])
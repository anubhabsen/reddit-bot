import praw
import re
import pdb
import os

reddit = praw.Reddit('bot1')

with open('posts_modified.txt', 'r') as f:
       posts_replied_to = f.read().split('\n')
       posts_replied_to = list(filter(None, posts_replied_to))

subreddit = reddit.subreddit('pythonforengineers')

for posts in subreddit.hot(limit = 5):
	if posts.id not in posts_replied_to:
		if re.search('i love python', posts.title, re.IGNORECASE):
			posts.reply('Test bot reply')
			print('Bot replying to: ', posts.title)
			posts_replied_to.append(posts.id)

with open('posts_modified.txt', 'w') as f:
    for post_id in posts_replied_to:
    	f.write(post_id + '\n')
import praw

client_id = 'H02aN-lk2LcPed3OTtU_tQ'  
client_secret = 'Oh5W-ZJFloxPvYBXOdPtL0bdYTsZ7A'  
user_agent = 'test_api/0.1 by Worried_Gene2999'  
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent)

subreddit_name = 'football'  # Subrredit 
post_limit = 10  # Nombre de posts à récupérer

subreddit = reddit.subreddit(subreddit_name)
for submission in subreddit.hot(limit=post_limit):
    print(f'Titre: {submission.title}, Score: {submission.score}, URL: {submission.url}, Auteur: {submission.author}')
import requests
import os.path as osp
import json

script_dir = osp.dirname(__file__)

# FUNCTION TO GET THE INFORMATION FROM A SUBREDDIT FED AS INPUT
def fetch(subreddit):

	num_posts = 100
	x = requests.get(f'http://api.reddit.com/r/{subreddit}/new?limit={num_posts}', headers={'User-Agent': 'mac:requests (by /u/thomas)'})
	return x.json()['data']['children']

def main():

    # LOAD THE DESIRED SUBREDDITS AND OUTPUT FILES
    subredditsBySub = ['funny', 'AskReddit', 'gaming', 'aww', 'pics', 'Music', 'science', 'worldnews', 'videos', 'todayilearned']
    subredditsByDay = ['AskReddit', 'memes', 'politics', 'nfl', 'nba', 'wallstreetbets', 'teenagers', 'PublicFreakout', 'leagueoflegends', 'unpopularopinion']
    output_file1 = open(osp.join(script_dir, '..', 'data', 'sample1.json'), 'w')
    output_file2 = open(osp.join(script_dir, '..', 'data', 'sample2.json'), 'w')

    # FETCH THE REDDIT POST DATA
    for sub in subredditsBySub:
        post = fetch(sub)
        for line in post:
            json.dump(line, output_file1)
            output_file1.write("\n")

    for sub in subredditsByDay:
        post = fetch(sub)
        for line in post:
            json.dump(line, output_file2)
            output_file2.write("\n")
    

if __name__ == '__main__':
    main()
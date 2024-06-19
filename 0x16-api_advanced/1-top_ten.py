#!/usr/bin/python3
"""
This module provides a function to query and print the titles
of the top 10 hot posts for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; MyBot/0.1; +http://mywebsite.com/bot)'
    }
    params = {'limit': 10}
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data', {})
            posts = data.get('children', [])
            for post in posts:
                print(post['data'].get('title'))
        else:
            print(None)
    except requests.RequestException:
        print(None)

if __name__ == "__main__":
    pass

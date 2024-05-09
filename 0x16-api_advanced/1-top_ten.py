#!/usr/bin/python3
"""
1-top_ten
"""
import requests


def top_ten(subreddit):

    """
    Function to query the Reddit API and print the titles of the
    first 10 hot posts for a given subreddit
    """

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                       'AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/58.0.3029.110 Safari/537.3')
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        children = data.get('children', [])
        if children:
            for post in children:
                print(post.get('data', {}).get('title'))
        else:
            print(None)
    else:
        print(None)


if __name__ == "__main__":
    pass

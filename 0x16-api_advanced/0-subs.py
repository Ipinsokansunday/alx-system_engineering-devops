#!/usr/bin/python3
"""
Queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API
    and returns the number of subscribers for a given subreddit.

    Parameters:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit.
        If the subreddit is not found or there is an error,
        returns 0.
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
    )

    if req.status_code == 200:
        # Check if 'data' key exists and 'subscribers' key exists within 'data'
        data = req.json().get("data")
        if data and "subscribers" in data:
            return data["subscribers"]
        else:
            return 0
    else:
        return 0

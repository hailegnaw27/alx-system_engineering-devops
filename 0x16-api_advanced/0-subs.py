#!/usr/bin/python3
# pylint: disable=invalid-name
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    headers = {
        'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)'
    }
    url = f'http://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers, timeout=5).json()
    subscribers = response.get("data", {}).get("subscribers", 0)
    return subscribers

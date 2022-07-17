# TweetScraper

A Python script that scrapes tweets from a user account (refer to this for [ratelimit info](https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/api-reference/get-users-id-tweets))

# How to run
- clone the project using `git clone `
- go into the project folder using `cd TweetScraper`
- install httpx using `pip install httpx`
- change the `BEARER_TOKEN` in `main.py` which you get from [here](https://developer.twitter.com/en/portal/petition/essential/basic-info) & the `USERNAME` to the username of the player you want to scrape
- run the script using `python main.py`
- this will output to `tweets.json` with the tweets (DOES NOT SCRAPE RETWEETS, REPLIES OR TWEETS WITH MEDIA)

# LANDSCAPEforCHANGE
Code for Instagram data extraction by hashtag
## Features

- Scrapes Instagram posts for a specific location (e.g. Verviers) or hashtag (e.g. `#Belgiumflood`) 
- Downloads images from the posts
- Extracts captions, likes, comments, hashtags, user info, and timestamps
- Saves all data into structured CSV and JSON formats
- Avoids duplicate posts and images
- Scrapes up to 50 comments per post using the Instagram Comment Scraper

## Requirements

- Python 3.x
- An [Apify](https://apify.com/) account and API token
- The following Python libraries:
  - `requests`
  - `csv`
  - `os`
  - `apify-client`
  - `json`

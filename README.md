# LANDSCAPEforCHANGE
# instagram_scraper.py
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
# sentiment_analysis.py
This script performs emotion classification on Facebook post data using pre-trained transformer models from Hugging Face. It supports single-label and multi-label emotion detection with RoBERTa-based models.

Features
Loads posts from CSV files

Uses j-hartmann/emotion-english-distilroberta-base or cardiffnlp/twitter-roberta-base-emotion for emotion classification

Automatically truncates long text inputs to comply with token limits

Outputs the dominant emotion and associated confidence score

Saves the results back into a CSV file for further analysis or visualization

Requirements
Python 3.x

pandas

transformers (by Hugging Face)

You can install the required libraries using:

bash
Copy
Edit
pip install pandas transformers

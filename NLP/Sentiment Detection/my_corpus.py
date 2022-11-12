'''
import and combine corpus
Topic of Interest: "Sam Matekane"
Collect tweets regarding sam matekane and to analyze their sentiments
and understand how people feel about him.

'''
# Import Libraries
from textblob import TextBlob
import sys
# for accessing Twitter API
import tweepy
from tweepy import OAuthHandler
# for visualizing data in different ways
import matplotlib.pyplot as plt
# for data manipulations
import pandas as pd
# for working with arrays
import numpy as np
# for censoring data
from better_profanity import profanity
import os
import nltk
import pycountry
import re
import string
# visualize word frequencies
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from langdetect import detect
from nltk.stem import SnowballStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer 


# Remember to keep your Keys and Tokens a secret!

consumer_key = 'xxxxx'
consumer_secret = 'xxxxx' 
access_token = 'xxxxx'
access_token_secret = 'xxxxx'

# Access Twitter Data

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)
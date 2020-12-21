# Name: Carrie Lu
# Date: November 18, 2020
# Description: This program performs a simple sentiment analysis on Twitter data and
# determines the happiness score, number of tweets, and total number of tweets in each timezone (Eastern, Central, Mountain, Pacific).

from sentiment_analysis import compute_tweets

# Prompt user to enter the name of the file containing the tweets and the file containing the keywords
user_file = input('Enter name of file with tweets:')
user_keywords_file = input('Enter file name of file with keywords:')
results = compute_tweets(user_file, user_keywords_file)

# Output the results in a readable form
if results != []:
    print("EASTERN:", "\nHappiness Score: ", results[0][0], "\nNumber of Tweets in Timezone: ", results[0][1],
          "\nTotal Number of Tweets in Timezone: ", results[0][2], "\n")
    print("CENTRAL:", "\nHappiness Score: ", results[1][0], "\nNumber of Tweets in Timezone: ", results[1][1],
          "\nTotal Number of Tweets in Timezone: ", results[1][2], "\n")
    print("MOUNTAIN:", "\nHappiness Score: ", results[2][0], "\nNumber of Tweets in Timezone: ", results[2][1],
          "\nTotal Number of Tweets in Timezone: ", results[2][2], "\n")
    print("PACIFIC:", "\nHappiness Score: ", results[3][0], "\nNumber of Tweets in Timezone: ", results[3][1],
          "\nTotal Number of Tweets in Timezone: ", results[3][2])
else:
    print("EASTERN:", "\nHappiness Score: 0", "\nNumber of Tweets in Timezone: 0",
          "\nTotal Number of Tweets in Timezone: 0", "\n")
    print("CENTRAL:", "\nHappiness Score: 0", "\nNumber of Tweets in Timezone: 0",
          "\nTotal Number of Tweets in Timezone: 0", "\n")
    print("MOUNTAIN:", "\nHappiness Score: 0", "\nNumber of Tweets in Timezone: 0",
          "\nTotal Number of Tweets in Timezone: 0", "\n")
    print("PACIFIC:", "\nHappiness Score: 0", "\nNumber of Tweets in Timezone: 0",
          "\nTotal Number of Tweets in Timezone: 0")

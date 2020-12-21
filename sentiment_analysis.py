# Create constants for the longitude and latitude boundaries of the regions
MAX_LAT = 49.189787
MIN_LAT = 24.660845
P1_LONG = -67.444574
P3_LONG = -87.518395
P5_LONG = -101.998892
P7_LONG = -115.236428
P9_LONG = -125.242264


# Function that computes and returns the happiness score for each tweet and its corresponding region, date, and time
def compute_tweets(tweetFile, keywordFile):
    try:
        t = open(tweetFile, "r", encoding="utf-8")
        tweets = t.readlines()
        k = open(keywordFile, "r", encoding="utf-8")
        keywords = k.readlines()

        # Create and initialize empty lists, dictionaries, and tuples to store values that will be used later
        region_scores = {'Eastern': 0, 'Central': 0, 'Mountain': 0, 'Pacific': 0}
        tweet_count = {'Eastern': 0, 'Central': 0, 'Mountain': 0, 'Pacific': 0}
        keyword_count = {'Eastern': 0, 'Central': 0, 'Mountain': 0, 'Pacific': 0}
        lines_list = []
        keywords_dict = {}
        result = []

        # Store keywords into a dictionary named keywords_dict
        for line in keywords:
            line = line.split(',')
            line[1] = line[1].replace('\n', '')
            keywords_dict[line[0]] = line[1]

        # Split each line in tweets by whitespace and store the values in a list, lines. Then store lines into lines_list
        for line in tweets:
            line = line.lower()
            lines = []
            line = line.split()
            for item in line:
                lines.append(item)
            lines_list.append(lines)

        # Remove the value, date, and time from each list from the tweet file.
        for item in lines_list:
            item.pop(2)
            item.pop(2)
            item.pop(2)
            # Find the region in which the tweet was sent and remove punctuation from the beginning and end of words.
            latitude = item[0].replace('[', '')
            latitude = latitude.replace(',', '')
            longitude = item[1].replace(']', '')
            # Remove all punctuation in the tweets
            for index, char in enumerate(item):
                if char[0] in ',.?!@#$%-()\'\"':
                    item[index] = char.replace(char[0], '')
                if char[-1] in ',.?!@#$%-()\'\"':
                    item[index] = char.replace(char[-1], '')
            # Call function find_region to determine which timezone the tweet belongs in
            timezone = find_region(float(latitude), float(longitude))
            # Check if a tweet is from one of the given timezones and increment the score by such; if not, it is not added to the score.
            if timezone != "":
                tweet_count[timezone] += 1
                # Call function calculate_score to find the happiness score of the tweet
                score = calculate_score(item, keywords_dict)
                if score is not None:
                    region_scores[timezone] += score
                    keyword_count[timezone] += 1

        # Create a tuple storing the average happiness value, the number of keyword tweets and the total number of tweets.
        for place in tweet_count:
            if keyword_count[place] != 0:
                average = region_scores[place] / keyword_count[place]
            else:
                average = 0
            regions = (average, keyword_count[place], tweet_count[place])
            result.append(regions)

        return result

    # Raise exception if file does not exist and return an empty list
    except IOError:
        return []


# Function that finds the region where the tweet was sent
def find_region(latitude, longitude):
    if MIN_LAT <= latitude <= MAX_LAT:  # If the tweet is not within the longitude boundaries, nothing is returned
        # If the tweet is within the longitude boundaries, eastern, central, mountain or nothing will be returned depending on where it falls within the latitude boundaries
        if P1_LONG >= longitude >= P3_LONG:
            return "Eastern"
        elif P3_LONG >= longitude >= P5_LONG:
            return "Central"
        elif P5_LONG >= longitude >= P7_LONG:
            return "Mountain"
        elif P7_LONG >= longitude >= P9_LONG:
            return "Pacific"
        else:
            return ""
    else:
        return ""


# Function that calculates and returns the happiness score in each tweet
def calculate_score(tweet, keywords):
    sentiment_value = 0
    num_keywords = 0
    for word in tweet:
        for key, value in keywords.items():
            if word == key:
                num_keywords += 1
                sentiment_value += int(value)
    if num_keywords != 0:
        happiness_score = sentiment_value / num_keywords
        return happiness_score

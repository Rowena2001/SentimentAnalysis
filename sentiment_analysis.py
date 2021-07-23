import string
translator = str.maketrans('', '', string.punctuation)


# GET TWEETS FROM REGIONS
def determineRegion(latitude, longitude):
  lower_lat = 24.660845
  upper_lat = 49.189787

  p1_lon = -67.444574
  p3_lon = -87.518395
  p5_lon = -101.998892
  p7_lon = -115.236428
  p9_lon = -125.242264

  if (lower_lat <= latitude <= upper_lat):
    if (p1_lon >= longitude >= p3_lon):
      return "eastern"
    elif (p3_lon >= longitude >= p5_lon):
      return "central"
    elif (p5_lon >= longitude >= p7_lon):
      return "mountain"
    elif (p7_lon >= longitude >= p9_lon):
      return "pacific"

# DETERMINES COORDINATES OF TWEET
def getLatitudeAndLongitude(tweet):
  content = tweet.split(" ")
  latitude = content[0].strip("[").strip(",") # latitude
  longitude = content[1].strip("]") # longitude

  return {"latitude": float(latitude), "longitude": float(longitude)}

# TWEETS STATISTICS (pass in a specific region of tweets ie. pacific)
def getTweetStats(regionalTweets, wordValueDictionary):
  happinessPointsTotal = 0
  happyTweetsCount = 0
  totalTweetsCount = 0

  # reads the tweet file line by line
  for tweet in regionalTweets:
    totalTweetsCount += 1

    content = " ".join(tweet.split(" ")[5:])
    # print(content)
    content = content.translate(translator).lower()
    # reading each word from tweet
    for word in content.split():
      try:
        if word in wordValueDictionary.keys():
          happinessPointsTotal += wordValueDictionary[word]
          happyTweetsCount += 1
          break
      except:
        pass

  results = {
    "happinessPointsTotal" : happinessPointsTotal,
    "happyTweetsCount" : happyTweetsCount,
    "totalTweetsCount" : totalTweetsCount
  }
  return results

# COMPUTE TWEETS
def compute_tweets(tweetsFileName, keywordsFileName):
  try:
    tweetsFile = open(tweetsFileName, "r", encoding="utf-8")
    keywordsFile = open(keywordsFileName, "r", encoding="utf-8")
  except:
    exit("Please enter two valid files.")

  # KEYWORDS AND VALUES
  wordValueDictionary = {}
  # assigns values to keywords
  for line in keywordsFile:
    content = line.split(",")
    word = content[0].strip()
    value = int(content[1].strip("\n"))
    wordValueDictionary[word] = value

  # a dictionary of the list of tweets for each region
  regionalTweets = {
    "eastern": [],
    "central": [],
    "mountain": [],
    "pacific": []
  }

  for tweet in tweetsFile:
    coordinates = getLatitudeAndLongitude(tweet)
    region = determineRegion(coordinates["latitude"], coordinates["longitude"])

    if (region != None):
      regionalTweets[region].append(tweet)

  listOfTuples = []
  # goes through each region's list of tweets
  for regionList in regionalTweets.values(): # regionalTweets.values() to get the values of a dictionary
    regionStats = getTweetStats(regionList, wordValueDictionary) # returns a dictionary of stats for the specific region
    if regionStats["happyTweetsCount"] != 0:
        averageHappiness = regionStats["happinessPointsTotal"] / regionStats["happyTweetsCount"]
    else:
        averageHappiness = "does not exist"
    regionTuple = (averageHappiness, regionStats["happyTweetsCount"], regionStats["totalTweetsCount"])
    listOfTuples.append(regionTuple)
  tweetsFile.close()
  keywordsFile.close()
  return listOfTuples

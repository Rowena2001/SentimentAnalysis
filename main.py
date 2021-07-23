# Name: Rowena Shi

# Program reads a given tweets file and a given keywords file and computes the happiness score for each region
# # Assigns a value to each keyword
# # Identifies the region of each tweet
# # Reads each word in each tweet and adds the corresponding values for every keyword
# # Computes the average happiness score, total keyword tweets, and total tweets in each region

# import functions from module
from sentiment_analysis import*

# prompts user for file names
tweetsFileName = input("Enter tweets file: ")
keywordsFileName = input("Enter keywords file: ")

# calls compute_tweets function
listOfTuples = compute_tweets(tweetsFileName, keywordsFileName)

# displays results
regions = ["\nEASTERN", "CENTRAL", "MOUNTAIN", "PACIFIC"]
for i in range(len(listOfTuples)):
  regionalTuple = listOfTuples[i]
  print(regions[i])
  print("Average: " + str(regionalTuple[0]))
  print("Number of keyword tweets: " + str(regionalTuple[1]))
  print("Total tweets: " + str(regionalTuple[2]) + "\n")

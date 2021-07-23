# Driver for testing ... tests combinations of test files by calling call compute_tweets
#

from sentiment_analysis import compute_tweets

print()
print("** Test 1")
results = compute_tweets("test_tweets1.txt","testkey1.txt")
print(results)
print()

print()
print("** Test 2")
results = compute_tweets("test_tweets2.txt","testkey2.txt")
print(results)
print()

print()
print("** Test 3")
results = compute_tweets("test_tweets2.txt","testkey1.txt")
print(results)
print()

print()
print("** Test 4")
results = compute_tweets("test_tweets1.txt","testkey2.txt")
print(results)
print()

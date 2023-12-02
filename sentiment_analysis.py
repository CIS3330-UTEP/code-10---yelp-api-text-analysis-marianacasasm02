from vaderSentiment.vadersentiment import SentimentIntensityAnalyzer 

analyzer = SentimentIntensityAnalyzer()

reviews = open('tacos_reviews.txt')

for review in reviews:
    print (review)
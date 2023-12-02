from yelpapi import YelpAPI
import pandas as pd
import nltk
from nltk.corpus import stopwords
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

api_key = "SbkLr-2W6hh9xW5TrWLXxji-oyPFSpDakq6XRkgplPYs803SN54hCgez2F8uauABG2OZS0NsLVya3awrS3Zy0wyXJn-cLVNq8Ktr8jtRu7U39e3hQH-Cg3aV2GBMZXYx"
yelp_api_instance =  YelpAPI(api_key)

search_term = 'tacos'
location_term = 'New York, New York'


search_results = yelp_api_instance.search_query(term=search_term, location=location_term, sort_by='rating', limit=10) 
print(search_results)

analyzer = SentimentIntensityAnalyzer()

alias_for_reviews = 'los-tacos-no-1-new-york-3'
review_response = yelp_api_instance.reviews_query(id=alias_for_reviews) 
reviews_df = pd.DataFrame.from_dict(review_response['reviews'])
reviews_df.to_csv('api_result')

for review in review_response['reviews']:
    review_text = review['text']  
    sentiment_score = analyzer.polarity_scores(review_text)
    
    print(review_text)
    print(sentiment_score)
    print("\n-----------------------------------------------------------------------------------------")
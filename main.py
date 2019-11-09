from google_wrapper import get_entity_sentiment
import twitter_wrapper
from textblob import TextBlob
import flask
import numpy as np

def jacobs(request):
    query = request.args.get('query')
    handle = twitter_wrapper.getHandle(query)
    tweets = twitter_wrapper.getTweets(handle)
    
    popularity = np.log10(twitter_wrapper.getFollowers(handle))
    objectivity = (1 - TextBlob(tweets).subjectivity) * 10
    optimism = (TextBlob(tweets).sentiment.polarity/2 + 0.5) * 10
    
    analysis = get_entity_sentiment(tweets)

    response = {
        'objectivity': objectivity,
        'optimism': optimism,
        'popularity': popularity,
        'entities': analysis
    }

    response = flask.jsonify(response)
    response.headers.set('Access-Control-Allow-Origin', '*')
    response.headers.set('Access-Control-Allow-Methods', 'GET, POST')

    return response
    
if __name__ == '__main__':
    app.run()
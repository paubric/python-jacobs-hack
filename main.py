from google_wrapper import get_entity_sentiment
import twitter_wrapper
from textblob import TextBlob

def jacobs(request):
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST',
        'Access-Control-Request-Method': '*',
        'Access-Control-Allow-Headers': '*'
    }

    query = request.args.get('query')
    handle = twitter_wrapper.getHandle(query)
    tweets = twitter_wrapper.getTweets(handle)

    objectivity = (1 - TextBlob(tweets).subjectivity) * 10
    optimism = (TextBlob(tweets).sentiment.polarity/2 + 0.5) * 10
    
    analysis = get_entity_sentiment(tweets)

    response = {
        'objectivity': objectivity,
        'optimism': optimism,
        'popularity': 7.48,
        'entities': analysis
    }

    return (response, 200, headers)
    
if __name__ == '__main__':
    app.run()
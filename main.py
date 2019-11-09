from google_wrapper import get_entity_sentiment
import twitter_wrapper

def jacobs(request):
    # Set CORS headers for the preflight request
    if request.method == 'OPTIONS':
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }

        return ('', 204, headers)

    # Set CORS headers for the main request
    headers = {
        'Access-Control-Allow-Origin': '*'
    }

    query = request.args.get('query')
    handle = twitter_wrapper.getHandle(query)
    tweets = twitter_wrapper.getTweets(handle)
    analysis = get_entity_sentiment(tweets)

    return (analysis, 200, headers)
    
if __name__ == '__main__':
    app.run()
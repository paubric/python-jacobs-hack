from google_wrapper import get_entity_sentiment

def jacobs(request):
    query = request.args.get('query')
    analysis = get_entity_sentiment(query)

    return analysis

if __name__ == '__main__':
    app.run()
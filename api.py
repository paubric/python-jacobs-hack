from flask import Flask
from google_wrapper import get_entity_sentiment
from flask import request

print('Finished imports')

app = Flask(__name__)

@app.route('/api')
def hello_world():
    query = request.args.get('query')
    analysis = get_entity_sentiment(query)

    return analysis

if __name__ == '__main__':
    app.run()
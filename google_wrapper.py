from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from pprint import pprint

type_mapping = [
    'Unknown',
    'Person',
    'Location',
    'Organization',
    'Event',
    'Artwork',
    'Consumer product',
    'Other',
    'Phone number',
    'Address',
    'Date',
    'Number',
    'Price'
]

def get_entity_sentiment(text):
    result = {}

    client = language.LanguageServiceClient()

    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    response = client.analyze_entity_sentiment(document=document)
    entities = response.entities

    for entity in entities:
        if result.get(entity.name) == None:
            result[entity.name] = {}

            result[entity.name]['total_sentiment'] = entity.sentiment.score * entity.sentiment.magnitude
            result[entity.name]['total_magnitude'] = entity.sentiment.magnitude
            result[entity.name]['type'] = type_mapping[entity.type]
            result[entity.name]['mention_count'] = 1
            result[entity.name]['average_sentiment'] = result[entity.name]['total_sentiment']
            result[entity.name]['average_magnitude'] = result[entity.name]['total_magnitude']
        else:
            result[entity.name]['total_sentiment'] += entity.sentiment.score * entity.sentiment.magnitude
            result[entity.name]['total_magnitude'] += entity.sentiment.magnitude
            result[entity.name]['mention_count'] += 1
            result[entity.name]['average_sentiment'] = result[entity.name]['total_sentiment'] / result[entity.name]['mention_count']
            result[entity.name]['average_magnitude'] = result[entity.name]['total_magnitude'] / result[entity.name]['mention_count']

        sorted_result = sorted(result.items(), key=lambda kv: kv[1]['average_magnitude'], reverse=True)

    return sorted_result

pprint(get_entity_sentiment('Natural Language uses machine learning to reveal the structure and meaning of text. You can extract information about people, places, and events, and better understand social media sentiment and customer conversations. Natural Language enables you to analyze text and also integrate it with your document storage on Google Cloud Storage. '))
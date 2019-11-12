# Jacob's Hack 2019 MLH Project
## Inspiration

NGOs, activists, and other entities advocating for social good are facing difficulties in forming strong, meaningful partnerships because of the inefficiency of the human-conducted political research process required for that. This issue is greatly limiting their potential for achieving their ambitious goals.

## What it does

Standpoint is streamlining the political research process by automatically extracting actionable insights about public figures and organizations from their public statements through natural language processing. It scrapes social media and media outlets for their declarations and determines the stance each entity has in relation to various subjects. In addition, it provides some proprietary scores which help the user get a better feel of the queried entity at a glance.

## How we built it

We built a serverless Python API on Google Cloud Functions which was tasked with the scraping of Twitter posts and the entity sentiment analysis performed by Google Natural Language API. We then created a single-page demo in React which runs on Google App Engine and presents the functionality of the API. Additionally, we created an UiPath Robot which automates the scraping of articles from the Huffington Post, presumably for further integrating this data source into our results.

## Challenges we ran into

Twitter's API does not allow for ambiguous searches for entities, it needs the exact handle. We automatically perform a Google search to find the appropriate Twitter handle from the more general name of an entity.

## Accomplishments that we're proud of

We managed to deploy a serverless function which triggers NLP analysis, and present its result in an intuitive way.

## What we learned

GCP provides hilariously complex services in a super accessible fashion. One of us learned the basics of GitHub. One of us learned how to debug cloud services from logs.

## What's next for Standpoint

Further validating the relevance of the identified issue and brainstorming on possible sustainable ways of implementing such a service.

_AI has been infamously used to exploit voters. Let’s use it instead to better understand the power dynamics in our society._

Videos: https://drive.google.com/drive/folders/1JBC141wMEcSRpa1ZX8r7fHkDlc6o_5Gc?usp=sharing

## Contribution
Paul: GCP, UiPath, ReactJS

Jasper: Twitter

Alina: UX Prototyping

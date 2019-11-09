import twitter
from urllib3 import request
from BeautifulSoup import BeautifulSoup

name = "jk rowling"
name.replace(" ", "+")
print(name)

url = "https://www.google.com/search?q=twitter+" + name
page = request.urlopen(url)
soup = BeautifulSoup(page.read())
links = soup.findAll("a")
for link in links:
    print link["href"]



# Take in "United Nations" and return "UN" (its Twitter handle)
def getHandle(query):
    pass

# Take in "UN" and return ['last tweet', 'previous tweet']
def getTweets(handle):
    api = twitter.Api(consumer_key='AP84RmwW08IvolBCJQw3hz9VC',
                      consumer_secret='6rJbXWzPAGkYHL7CQm6Q3NLerVNtW0qpkxEjOJHNAnez7wVaCk',
                      access_token_key='959803788981932032-WLmUPiLHF7QxnDAWYqgjmaICcBJjLBE',
                      access_token_secret='i82j9LJrK4kUea6jPbBMJ8U5vRkLYJesJlhyH9eMzSMEM')

    #print(api.VerifyCredentials())

    # Gets the past 20 statuses from twitter
    statuses = api.GetUserTimeline(screen_name=handle)
    statusArray = [s.text for s in statuses]

    print(statusArray[0])
    pass




import twitter
from googlesearch import search

# Take in "United Nations" and return "UN" (its Twitter handle)
def getHandle(query):
    query += " Twitter"

    # Get the first google hit for the query
    urllist = []
    for url in search(query, stop=1):
        urllist.append(url)

    # extracts the twitter handle of the first google hit
    twitterHandle = []
    for i in range(1):
        if urllist[i].startswith("https://twitter.com/"):
            urllist[i] = urllist[i][20:]
            if urllist[i].endswith("?lang=en"):
                urllist[i] = urllist[i][:-8]
            if (urllist[i].find("/") == -1):
                twitterHandle.append(urllist[i])

    if (len(twitterHandle) != 0):
        return twitterHandle[0]
    else: 
        print("No handle found")
        return 0

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
    
    # only certain characters will be saved as part of the twitterPost
    allowedCharacters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ', '@']
    for i in range(len(statusArray)):
        twitterPost = ""
        twitterPostlist = list(statusArray[i])
        for j in range(len(twitterPostlist)):
            if twitterPostlist[j] in allowedCharacters:
                twitterPost += twitterPostlist[j]
        statusArray[i] = twitterPost


    return statusArray




handle = getHandle(input("What do you what the twitter-handle for?\n"))
print(handle)
print(getTweets(handle))
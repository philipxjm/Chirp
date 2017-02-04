from TwitterSearch import *
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['Guttenberg', 'Doktorarbeit']) # let's define all words we would like to have a look for
    tso.set_language('de') # we want to see German tweets only
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = 'A9XcMbJQNoc5UuDDQqYhDIkDi',
        consumer_secret = 'cfDMXwwCs3Pf3jyu551dQCIKxpaVQwuDWPsqYtNZ3J4dTfatiI',
        access_token = '2155608048-Tmj6JM6b5KEprwvPsShtpBaL6JiwheWt07qlt7F',
        access_token_secret = '3MnKXHa21eZFmrj8tNKfdhIISJLDN5wprZHTZEAkvsNL6'
     )

     # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)
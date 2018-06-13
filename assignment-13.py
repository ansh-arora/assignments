#Q1
#API- API stands for application programming interface. In computer programming, an application programming interface (API) is a set of subroutine definitions, protocols, and tools for building application software. In general terms, it is a set of clearly defined methods of communication between various software components.
#access token for twitter= 1006816314080550914-03TPMGEse7s30U4RzIHeLepCMarekc

#Q2
#google IP address= 172.217.160.238
#facebook IP address= 157.240.23.35
#gmail IP address= 172.217.161.5

#Q3
#tweets using '#PMO':
import tweepy
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_key,access_secret)
api= tweepy.API(auth)

tw =api.search('#PMO', lang="en",count=15, tweet_mode="extended")

for t in tw:
    print('---------')
    print(t.full_text)
    print('---------')

#Q4
#Library: A library is a collection of code built to perform common tasks. Library code tends to be relatively stable and bug free. Use of appropriate libraries can reduce the amount of code the need to be written. It will tend to reduce line of code counts for an application will increasing the rate at which functionality is delivered. In most cases, it is better to use a library routine than to write your own code.
#API: An API (Application Programming Interface) is interface to some functionality which allows an application to access the available functionality. An API may be referred to as an Interface. API exist at many levels including system, library, framework, program, and application. APIs should be defined before the code implementing them is implemented.
#Example: Go to a library and start reading books. If you are the application then the collection of books is the library. The shelves, the cupboards, and the compound that houses all this constitutes the framework. Everything you come in contact while performing the task of reading the books is the API.

#!/usr/bin/env python
# coding: utf-8

# In[1]:

#importing required modules and libraries
import tweepy, sys
import matplotlib.pyplot as plt
from textblob import TextBlob
import mpld3
# In[2]:


# function to calculate the percentage
def percent(part, whole):
    return 100 * float(part)/float(whole)


# In[3]:


#connection with the api
consumerkey = "Enter key"
consumersecret = "Enter consumer Secret"
accessToken = "Enter access token"
accessTokenSecret = "Enter access token secret" 


# In[4]:


auth = tweepy.OAuthHandler(consumer_key=consumerkey, consumer_secret=consumersecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)


# In[9]:


searchFor = input("Enter the keyword or hastag:")
numberSearch = int(input("number of tweets:"))


# In[19]:


#below down we are providing the search item and the number of items
tweets = tweepy.Cursor(api.search, q=searchFor, lang="English").items(numberSearch)

positive = 0
negative = 0
neutral = 0
polarity = 0 

for tweet in tweets:
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity
    
    if(analysis.sentiment.polarity == 0):
        neutral += 1
    elif(analysis.sentiment.polarity < 0 ):
        negative += 1
    elif(analysis.sentiment.polarity > 0):
        positive += 1
        
positive = percent(positive, numberSearch)
negative = percent(negative, numberSearch)
neutral = percent(neutral, numberSearch)    

print(positive)
print(negative)
print(neutral)
positive =  format(positive, '.2f')
negative =  format(negative, '.2f')
neutral =  format(neutral, '.2f')


# In[18]:


#get_ipython().run_line_magic('matplotlib', 'inline')
labels = ['Positive ['+str(positive)+'%]', 'Negative ['+str(negative)+'%]', 'Neutral ['+str(neutral)+'%]']
sizes = [positive, negative, neutral]
colors = ['yellowgreen', 'red', 'blue']
explode = (0.1,0,0)
patches, texts = plt.pie(sizes, colors=colors, explode=explode )

plt.legend(patches, labels, loc='best')
plt.title("People reaction on the " +searchFor)
plt.axis('equal')
plt.tight_layout()
plt.show()


# In[ ]:





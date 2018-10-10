#from newsapi import NewsApiClient
from nltk.corpus import stopwords
from textblob import TextBlob
import pandas as pd
import requests
import json

#newsapi = NewsApiClient(api_key='3241ac6a891a48749d59fa1abca9ef33')

title=[]
desc=[]
date=[]
df= []
#sources=['abc-news', 'bloomberg', 'bbc-news', 'daily-mail', 'financial-times', 'the-new-york-times', 'the-wall-street-journal']
#queries=['blockchain', 'cryptocurrency','Coinbase','ICO']
#for query in queries:
for i in range (1, 20):
      url= "https://newsapi.org/v2/everything?"
      parameters = dict(q='crypto mining',
                        language='en', page=i, sort_by='relevancy', sources='bloomberg,financial-times,the-new-york-times,the-wall-street-journal',
                         apiKey="eaa2e215ebbd4aa38f87c8d0ccfabfb4")
      articles_get = requests.get(url, params=parameters)
      all_articles = json.loads(articles_get.text)
      for items in (all_articles['articles']):
          title.append(str(items['title']))
          desc.append(str(items['description']))
          date.append(str(items['publishedAt'][:10]))

        
    
#df = df + list(all_articles)
df=pd.DataFrame({'Date':date, 'Title':title, 'Description':desc})


df['Description'] = df['Description'].str.replace('[^\w\s]','')
df['Description'].head()
df['Title'] = df['Title'].str.replace('[^\w\s]','')
df['Title'].head()

stop = stopwords.words('english')
df['Description'] = df['Description'].str.lower()
df['Description'] = df['Description'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
df['Description'].head()
#sentiment =[]
df['sentiment'] = df['Description'].apply(lambda x: TextBlob(x).sentiment[0])
df[['Description','sentiment']].head()
#text_df = df.to_string(columns=['Description'])
#for row in df.index.values:
#   text_df = df.to_string(columns=['Description'])
#   testimonial = TextBlob(text_df)
#   Sentiment_score = testimonial.sentiment.polarity
#   sentiment.append(Sentiment_score)

#df['Sentiment_Score'] = sentiment
print(df.head(10))

df_1 = df
print(df_1.head(10))

df_1.to_csv('data.csv',encoding='utf-8',index=False)
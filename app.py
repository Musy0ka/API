# importing flask or installing the flask module for making a flask web app
from flask import Flask, render_template

#installing newsapi module in terminal
#import that here
from newsapi import NewsApiClient

app = Flask(__name__)

#create a route function and render the html templates on that
@app.route('/')
def home():
  # enter client id and ap_key for authorization
  newsapi = NewsApiClient(api_key= 'a71b570af85a4a83871d2e569a90d250')

  #for top headlines of news
  top_headlines = newsapi.get_top_headlines(sources = 'bbc-news')
  # sources is meant by, where the news comes into your app by api

  #fetch all the articles of top headlines news
  t_articles = top_headlines['articles']

  #make a list of content to store the value on that list
  news = []
  desc = []
  img = []
  p_date = []
  url = []

  #fetch all the contents of articles by using for loop
  for i in range(len(t_articles)):
    main_article = t_articles[i]

    #append all the contents in to each of lists
    news.append(main_article['title'])
    desc.append(main_article['description'])
    img.append(main_article['urlToImage'])
    p_date.append(main_article['publishedAt'])
    url.append(main_article['url'])

    #make a zip for find the contents directly and shortly
    contents = zip(news,desc,img,p_date,url)

  #pass it in the render file

  return render_template('home.html',contents=contents)


if __name__ == '__main__':
  app.run(debug=True)
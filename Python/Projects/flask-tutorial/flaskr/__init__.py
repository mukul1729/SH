import os
import json
import datetime
from flask import make_response
import urllib
from flask import Flask
from flask import render_template
from flask import request
import feedparser

app = Flask(__name__)
feeds = {
'bbc':"http://feeds.bbci.co.uk/news/rss.xml",
'cnn':"http://rss.cnn.com/rss/edition.rss",
'fox':"http://feeds.foxnews.com/foxnews/l",
'iol':"http://www.iol.co.za/cmlink/1.640"}

@app.route('/',methods=['GET','POST'])
def gettemplate():
    query = request.form.get("temp")
    if not query or query.lower() not in feeds:
        temp = "bbc"
    else:
        temp = query.lower()
    feed = feedparser.parse(feeds[temp])
    first_article = feed['entries']
    response = make_response(render_template("home.html",article=first_article))
    expires = datetime.datetime.now() + datetime.timedelta(days=365)
    response.set_cookie("temp",temp,expires=expires)
    return response


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello %s</h1>'%name

if __name__ == '__main__':
    app.run(debug=True)

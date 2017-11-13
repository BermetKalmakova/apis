from flask import Flask, render_template
import urllib2, json

my_app = Flask(__name__)

@my_app.route('/', methods=['GET','POST'])
def root():
    u = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=5PqbttirS4RGT8iLNPnwXMxUPIY1WlgQh2ldOdah")
    contents = u.read()
    d = json.loads(contents)
    return render_template("rest.html", title = d["title"], pic = d["hdurl"], text = d["explanation"])

@my_app.route('/new', methods = ['GET'])
def new():
    u2 = urllib2.urlopen("https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json?api-key=66c50637748946c4b058c45e4492740e&title=confessions%20of%20a%20murder%20suspect")
    contents = u2.read()
    d2 = json.loads(contents)
    return render_template("new.html",  desc = d2["results"][0]["description"], author = d2["results"][0]["author"], age = d2["results"][0]["age_group"], title = d2["results"][0]["title"])

    
if __name__ == '__main__':
    my_app.debug = True
    my_app.run()

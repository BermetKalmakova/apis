from flask import Flask, render_template
import urllib2, json

my_app = Flask(__name__)

@my_app.route('/', methods=['GET','POST'])
def root():
    u = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=5PqbttirS4RGT8iLNPnwXMxUPIY1WlgQh2ldOdah")
    contents = u.read()
    d = json.loads(contents)
    return render_template("rest.html", title = d["title"], pic = d["hdurl"], text = d["explanation"])

    
if __name__ == '__main__':
    my_app.debug = True
    my_app.run()

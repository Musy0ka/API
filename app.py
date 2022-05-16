# importing flask or installing the flask module for making a flask web app
from flask import Flask, render_template

app = Flask(__name__)

#create a route function and render the html templates on that
@app.route('/')
def home():
  return render_template('home.html')


if __name__ == '__main__':
  app.run(debug=True)
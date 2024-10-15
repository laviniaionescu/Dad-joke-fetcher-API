from flask import Flask, render_template
import requests
app = Flask(__name__)


@app.route("/")
def homepage():
  return render_template('home.html')

@app.route('/getjoke')
def jokepage():
    headers = {'Accept': 'application/json'}

    response = requests.get('https://icanhazdadjoke.com/', headers=headers)
    if response.status_code == 200:
        joke = response.json()['joke']
        return render_template('jokepage.html', joke=joke)
    else:
        return 'Error fetching joke from API'


if __name__ == ('__main__'):
  app.run(debug=True)
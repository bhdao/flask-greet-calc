from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
  return "welcome"

@app.route('/welcome/<etc>')
def etcetera(etc):
  return f"welcome {etc}"

# They call this path variables!!

#https://youtu.be/zsYIw6RXjfM?si=GwO8TuQRsENJGGMh
"""from flask import Flask, request

app = Flask(__name__)#app is name of flask application

if __name__ == "__main__":
    app.run(debug=True)
""" #this is basic initialization
# now we create a root - this ia an endpoint a location where we can goto to get some kinda data
 #@ is a decorator , app is the flask application name , in () we put the path we want to access
#here we do / which is a default route, route is what actually comes after the / in your URL
"""
from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def Hello():
    return "Hello"

if __name__ == "__main__":
    app.run(debug=True)
"""
#once u run this (python filename.py) u get the url and if u click u will get the output
#GET - to retrieve resource # POST - to create resource #PUT -  to update resource # DELTE -

#https://chatgpt.com/share/672c4174-7438-800d-ae5b-f2ddb636f2cc
"""
from flask import Flask, jsonify
app = Flask(__name__)

#this GET is not retrieving from anywhere , u r giving vals rn and printing out
#dont need to import requests as u r not taking from web etc but u can put if u want- check link

@app.route('/api', methods=['GET'])
def get_data():
    data = {
        'message': 'Hello, world!',
        'status': 'success'
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
"""
# this is from your local - xlsx - so use pandas?????


from flask import Flask, jsonify
import pandas as pd
app = Flask(__name__)


@app.route('/api', methods=['GET'])
def get_specific_data():
    #file_path = (r'C:\Users\pooji\Downloads\athlete_events.csv\athlete_events.csv')  # local file

    df=pd.read_csv(r'C:\Users\pooji\Downloads\athlete_events.csv\athlete_events.csv')

    data=df[["Name","Age"]].head(10).to_dict(orient='records')
   # .to_dict(orient='records') - The error "TypeError: Object of type DataFrame is not JSON serializable" occurs because pandas DataFrames are not directly serializable to JSON by Flask’s jsonify() function. Flask can only automatically handle simple data structures
    #like dictionaries, lists, strings, numbers, etc. It cannot serialize pandas DataFrames or other non-standard Python objects directly.
    # You need to convert the DataFrame into a JSON-serializable format before returning it. The most common method is using .to_dict(orient='records'), which converts the DataFrame to a list of dictionaries, which jsonify() can handle

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)






















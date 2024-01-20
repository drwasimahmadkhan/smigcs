# from flask import Flask, render_template, flash, redirect, url_for, session, request, logging,jsonify
# # import nltk
# import requests
# import json

# #from data import Articles


# app = Flask(__name__)



# # Index
# @app.route('/get_data', methods=['GET'])
# def get_data_from_conceptnet():
    # keywords = request.args.get('keywords')
    # if request.method == 'GET':
        # #print(keywords)
        # base_url = "http://api.conceptnet.io/c/en/"
        # response = requests.get(base_url + keywords)
        # print(response)
        # return response.json()




# # Index
# @app.route('/')
# def index():
    # return render_template('index.html')
    

# if __name__=='__main__':
    # app.run(debug=True)
    
    
    
from flask import Flask, render_template, flash, redirect, url_for, session, request, jsonify
import requests

app = Flask(__name__)

@app.route('/get_data', methods=['GET'])
def get_data_from_conceptnet():
    keyword1 = request.args.get('keyword1')
    keyword2 = request.args.get('keyword2')

    # Assuming you want results for both keywords individually
    # base_url = "http://api.conceptnet.io/c/en/"
    base_url = "http://api.conceptnet.io/query"

    # response1 = requests.get(base_url + keyword1)
    # response2 = requests.get(base_url + keyword2)

    # # Combine the results of both requests for simplification (This can be further refined based on your requirements)
    # combined_results = {
        # 'results_keyword1': response1.json(),
        # 'results_keyword2': response2.json()
    # }

    # return jsonify(combined_results)
    
    params = {
        "start": "/c/en/" + keyword1,
        "end": "/c/en/" + keyword2,
        "limit": 10  # Assuming you want up to 10 results, change this as needed
    }

    response = requests.get(base_url, params=params)
    
    return response.json()

@app.route('/')
def index():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)

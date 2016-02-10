

from flask import Flask, render_template, request, redirect

import pickle
import numpy as np


##########################################################################
## Constants
##########################################################################
Language_list = ['Bengali', 'Dutch', 'English', 'French', 'German', 'Greek',
                 'Hindi', 'Italian', 'Japanese', 'Portuguese', 'Russian', 'Spanish', 'Thai']



##########################################################################
## Modules
##########################################################################

app_ticker = Flask(__name__)

#Variable to hold the text input from user for language Identification.
STOCK=''       

#Module which obtains user input.
@app_ticker.route('/index_ticker', methods=['GET', 'POST'])
def index_ticker():
    if request.method == 'GET':
        return render_template('ticker_info.html')
    else:
        STOCK = request.form['name_ticker']
  
        text_clf = pickle.load(open('experiment_file','r'))
    
        text_string = [STOCK]
    
        predict_string = text_clf.predict(text_string)
    
        LANGUAGE = Language_list[predict_string]
                        
        #Go to graph html for display.
        return render_template('graph.html', symb=STOCK, language=LANGUAGE)

#Module redirects the user back to the input page for a new request.
@app_ticker.route('/next_ticker')
def next_ticker():
    return redirect('/index_ticker') 

##########################################################################
## Program 
##########################################################################
    
if __name__ == "__main__":
    app_ticker.run(port=33507)
    
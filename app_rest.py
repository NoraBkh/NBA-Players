from flask import Flask, render_template,url_for,request
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods = ['POST'])

def predict():
    
    print("Model dumped!")
    
    clf = joblib.load('modelNBA.pkl')
    if request.method == 'POST':
        
        # convert input values to float
        ptg = float(request.form['ptg'])
        fg = float(request.form['fg'])
        reb = float(request.form['reb'])
        ast = float(request.form['ast'])
        stl = float(request.form['stl'])
        blk = float(request.form['blk'])
        tov = float(request.form['tov'])
        gp = float(request.form['gp'])
        min = float(request.form['min'])
        ft = float(request.form['ft'])
        p3 = float(request.form['p3'])
        
        # computing input model
        data =[[ptg, fg, p3, ft,min/gp, reb/gp, ast/gp, stl/gp, blk/gp, tov/gp]]
        vect = np.array(data)
        my_prediction = clf.predict(vect)
    return render_template('result.html', prediction = my_prediction)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask,request,render_template
import pickle
import numpy as np 

model = pickle.load(open("DTC.sav",'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/predict')
def predict():
    
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug= True)

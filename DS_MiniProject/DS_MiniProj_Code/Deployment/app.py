from flask import Flask,request,render_template
import pickle
import numpy as np 

model = pickle.load(open("DTC.sav",'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def predict():
    pH = float(request.form.get('pH'))
    Hardness = float(request.form.get('Hardness'))
    Solids = float(request.form.get('Solids'))
    Chloramines = float(request.form.get('Chloramines'))
    Sulfate = float(request.form.get('Sulfate'))
    Conductivity = float(request.form.get('Conductivity'))
    Organic_carbon = float(request.form.get('Organic_carbon'))
    Trihalomethanes = float(request.form.get('Trihalomethanes'))
    Turbidity = float(request.form.get('Turbidity'))

    result = model.predict(np.array([pH,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity]).reshape(1,9))
    
    if result[0] == 1:
        result = 'Water is not safe for you 😶'

    else:
        result = 'Water is safe for you 😄'

    return render_template('index.html',result = result)

if __name__ == '__main__':
    app.run(debug= True)

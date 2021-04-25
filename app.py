from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Holiday_1=0
    if request.method == 'POST':
        Registered = int(request.form['Registered'])
        casual=int(request.form['casual'])
        Humidity=float(request.form['Humidity'])
        Temprature=float(request.form['Temprature'])
        Day=int(request.form['Day'])
        Month=int(request.form['Month'])
        windspeed=int(request.form['Windspeed'])
        Holiday=request.form['Holiday']
        if(Holiday=='Yes'):
                Holiday_1=1
                
        else:
                Holiday_1=0
            
        
        prediction=model.predict([[Registered,casual,Humidity,Temprature,Day,Month,windspeed,Holiday_1]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="There is no demand for bikes")
        else:
            return render_template('index.html',prediction_text=" Bike demand of selected input is  {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)


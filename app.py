from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_medical.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        age = int(request.form['age'])
        height = float(request.form['height'])
        weight = int(request.form['weight'])
        gender=request.form['gender']
        if(gender=='male'):
            gender=1
        else:
            gender=0
        renal_problem=request.form['renal_problem']
        if(renal_problem=='yes'):
            renal_problem=1
        else:
            renal_problem=0
        hepatic_problem=request.form['hepatic_problem']
        if(hepatic_problem=='yes'):
            hepatic_problem=1
        else:
            hepatic_problem=0 
        plasma_conc = int(request.form['plasma_conc']) 
              
        prediction=model.predict([[age,height,weight,gender,renal_problem,hepatic_problem,plasma_conc]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot predict this dosage")
        else:
            return render_template('index.html',prediction_text="Your prescription as per Analysis is {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)


from flask import Flask, request, render_template
# from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
model = pickle.load(open("car_model.pkl", "rb"))



@app.route("/")
# @cross_origin()
def home():
    print('What the hell ois going on')
    return render_template("home.html")

@app.route("/predict", methods = ["GET", "POST"])
# @cross_origin()
def predict():
    if request.method == "POST":

        #years
        Years = int(request.form['Year'])
        # print(type(Years))
        Years = 2021-Years 

        #Kilometers
        Kilometers = float(request.form['Kilometers'])
        Kilometers = np.log10(Kilometers)
        #Fuel_Type
        Fuel_Type = request.form['Fuel_Type']
        if Fuel_Type == 'Petrol':
            Fuel_Type_Petrol = 1
            Fuel_Type_Petrol_CNG = 0
            Fuel_Type_Petrol_LPG = 0
        elif Fuel_Type == 'Petrol + CNG':
            Fuel_Type_Petrol = 0
            Fuel_Type_Petrol_CNG = 1
            Fuel_Type_Petrol_LPG = 0
        elif Fuel_Type == 'Petrol + LPG':
            Fuel_Type_Petrol = 0
            Fuel_Type_Petrol_CNG = 0
            Fuel_Type_Petrol_LPG = 1
        elif Fuel_Type == 'Diesel':
            Fuel_Type_Petrol = 0
            Fuel_Type_Petrol_CNG = 0
            Fuel_Type_Petrol_LPG = 0

        Transmission_Type = request.form['Transmission_Type']
        if Transmission_Type=="MANUAL":
            Transmission_Type_MANUAL = 1
        else:
            Transmission_Type_MANUAL = 0

        RTO = request.form['RTO']
        if RTO == "Other State":
            RTO_Other_State = 1
        else:
            RTO_Other_State = 0

        Insurance_Type = request.form['Insurance_Type']
        if Insurance_Type == "Comp":
            Insurance_Type_Comp	= 1
            Insurance_Type_Comprehensive = 0	
            Insurance_Type_Expired	= 0
            Insurance_Type_Insurance_Expired = 0 	
            Insurance_Type_Third_party	= 0
            Insurance_Type_Zero_Depreciation = 0	
            Insurance_Type_Zero_Dep = 0
        elif Insurance_Type == "Zero_Dep":
            Insurance_Type_Comp	= 0
            Insurance_Type_Comprehensive = 0	
            Insurance_Type_Expired	= 0
            Insurance_Type_Insurance_Expired = 0 	
            Insurance_Type_Third_party	= 0
            Insurance_Type_Zero_Depreciation = 0	
            Insurance_Type_Zero_Dep = 1
        elif Insurance_Type == "Third_party":
            Insurance_Type_Comp	= 0
            Insurance_Type_Comprehensive = 0	
            Insurance_Type_Expired	= 0
            Insurance_Type_Insurance_Expired = 0 	
            Insurance_Type_Third_party	= 1
            Insurance_Type_Zero_Depreciation = 0	
            Insurance_Type_Zero_Dep = 0
        elif Insurance_Type == "Expired":
            Insurance_Type_Comp	= 0
            Insurance_Type_Comprehensive = 0	
            Insurance_Type_Expired	= 1
            Insurance_Type_Insurance_Expired = 0 	
            Insurance_Type_Third_party	= 0
            Insurance_Type_Zero_Depreciation = 0	
            Insurance_Type_Zero_Dep = 0
        elif Insurance_Type == "Insurance Expired":
            Insurance_Type_Comp	= 0
            Insurance_Type_Comprehensive = 0	
            Insurance_Type_Expired	= 0
            Insurance_Type_Insurance_Expired = 1 	
            Insurance_Type_Third_party	= 0
            Insurance_Type_Zero_Depreciation = 0	
            Insurance_Type_Zero_Dep = 0
        elif Insurance_Type == "Comprehensive":
            Insurance_Type_Comp	= 0
            Insurance_Type_Comprehensive = 1	
            Insurance_Type_Expired	= 0
            Insurance_Type_Insurance_Expired = 0 	
            Insurance_Type_Third_party	= 0
            Insurance_Type_Zero_Depreciation = 0	
            Insurance_Type_Zero_Dep = 0
        elif Insurance_Type == "Zero Depreciation":
            Insurance_Type_Comp	= 0
            Insurance_Type_Comprehensive = 0	
            Insurance_Type_Expired	= 0
            Insurance_Type_Insurance_Expired = 0 	
            Insurance_Type_Third_party	= 0
            Insurance_Type_Zero_Depreciation = 1	
            Insurance_Type_Zero_Dep = 0
        elif Insurance_Type == "3rd Party":
            Insurance_Type_Comp	= 0
            Insurance_Type_Comprehensive = 0	
            Insurance_Type_Expired	= 0
            Insurance_Type_Insurance_Expired = 0 	
            Insurance_Type_Third_party	= 0
            Insurance_Type_Zero_Depreciation = 0	
            Insurance_Type_Zero_Dep = 0
        
        Owner = request.form['Owner']
        if Owner == "First Owner":
            Owner_Type_First_Owner = 1	
            Owner_Type_Fourth_Owner	 = 0
            Owner_Type_Second_Owner	= 0
            Owner_Type_Sixth_Owner = 0
            Owner_Type_Third_Owner = 0
        elif Owner == "Second Owner":
            Owner_Type_First_Owner = 0	
            Owner_Type_Fourth_Owner	 = 0
            Owner_Type_Second_Owner	= 1
            Owner_Type_Sixth_Owner = 0
            Owner_Type_Third_Owner = 0
        elif Owner == "Third Owner":
            Owner_Type_First_Owner = 0	
            Owner_Type_Fourth_Owner	 = 0
            Owner_Type_Second_Owner	= 0
            Owner_Type_Sixth_Owner = 0
            Owner_Type_Third_Owner = 1
        elif Owner == "Fourth Owner":
            Owner_Type_First_Owner = 0	
            Owner_Type_Fourth_Owner	 = 1
            Owner_Type_Second_Owner	= 0
            Owner_Type_Sixth_Owner = 0
            Owner_Type_Third_Owner = 0
        elif Owner == "Sixth Owner":
            Owner_Type_First_Owner = 0	
            Owner_Type_Fourth_Owner	 = 0
            Owner_Type_Second_Owner	= 0
            Owner_Type_Sixth_Owner = 1
            Owner_Type_Third_Owner = 0
        elif Owner == "Fifth Owner":
            Owner_Type_First_Owner = 0	
            Owner_Type_Fourth_Owner	 = 0
            Owner_Type_Second_Owner	= 0
            Owner_Type_Sixth_Owner = 0
            Owner_Type_Third_Owner = 0

        Brand_Name = request.form['Brand_Name']
        if Brand_Name == 'BMW':
            Brand_name_BMW = 1
            Brand_name_Chevrolet = 0	
            Brand_name_Datsun = 0
            Brand_name_Fiat	= 0
            Brand_name_Ford	= 0
            Brand_name_Honda = 0
            Brand_name_Hyundai = 0	
            Brand_name_Jeep	= 0
            Brand_name_KIA= 0
            Brand_name_MG = 0
            Brand_name_Mahindra	= 0
            Brand_name_Maruti = 0
            Brand_name_Mercedes = 0	
            Brand_name_Nissan = 0	
            Brand_name_Renault = 0	
            Brand_name_Skoda = 0	
            Brand_name_Ssangyong = 0	
            Brand_name_Tata	= 0
            Brand_name_Toyota = 0	
            Brand_name_Volkswagen = 0	
            Brand_name_Volvo = 0
        elif Brand_Name == 'Tata':
            Brand_name_BMW = 0
            Brand_name_Chevrolet = 0	
            Brand_name_Datsun = 0
            Brand_name_Fiat	= 0
            Brand_name_Ford	= 0
            Brand_name_Honda = 0
            Brand_name_Hyundai = 0	
            Brand_name_Jeep	= 0
            Brand_name_KIA= 0
            Brand_name_MG = 0
            Brand_name_Mahindra	= 0
            Brand_name_Maruti = 0
            Brand_name_Mercedes = 0	
            Brand_name_Nissan = 0	
            Brand_name_Renault = 0	
            Brand_name_Skoda = 0	
            Brand_name_Ssangyong = 0	
            Brand_name_Tata	= 1
            Brand_name_Toyota = 0	
            Brand_name_Volkswagen = 0	
            Brand_name_Volvo = 0
        elif Brand_Name == 'Maruti':
            Brand_name_BMW = 0
            Brand_name_Chevrolet = 0	
            Brand_name_Datsun = 0
            Brand_name_Fiat	= 0
            Brand_name_Ford	= 0
            Brand_name_Honda = 0
            Brand_name_Hyundai = 0	
            Brand_name_Jeep	= 0
            Brand_name_KIA= 0
            Brand_name_MG = 0
            Brand_name_Mahindra	= 0
            Brand_name_Maruti = 1
            Brand_name_Mercedes = 0	
            Brand_name_Nissan = 0	
            Brand_name_Renault = 0	
            Brand_name_Skoda = 0	
            Brand_name_Ssangyong = 0	
            Brand_name_Tata	= 0
            Brand_name_Toyota = 0	
            Brand_name_Volkswagen = 0	
            Brand_name_Volvo = 0
        elif Brand_Name == 'Hyundai':
            Brand_name_BMW = 0
            Brand_name_Chevrolet = 0	
            Brand_name_Datsun = 0
            Brand_name_Fiat	= 0
            Brand_name_Ford	= 0
            Brand_name_Honda = 0
            Brand_name_Hyundai = 1	
            Brand_name_Jeep	= 0
            Brand_name_KIA= 0
            Brand_name_MG = 0
            Brand_name_Mahindra	= 0
            Brand_name_Maruti = 0
            Brand_name_Mercedes = 0	
            Brand_name_Nissan = 0	
            Brand_name_Renault = 0	
            Brand_name_Skoda = 0	
            Brand_name_Ssangyong = 0	
            Brand_name_Tata	= 0
            Brand_name_Toyota = 0	
            Brand_name_Volkswagen = 0	
            Brand_name_Volvo = 0
        elif Brand_Name == 'Datsun':
            Brand_name_BMW = 0
            Brand_name_Chevrolet = 0	
            Brand_name_Datsun = 1
            Brand_name_Fiat	= 0
            Brand_name_Ford	= 0
            Brand_name_Honda = 0
            Brand_name_Hyundai = 0	
            Brand_name_Jeep	= 0
            Brand_name_KIA= 0
            Brand_name_MG = 0
            Brand_name_Mahindra	= 0
            Brand_name_Maruti = 0
            Brand_name_Mercedes = 0	
            Brand_name_Nissan = 0	
            Brand_name_Renault = 0	
            Brand_name_Skoda = 0	
            Brand_name_Ssangyong = 0	
            Brand_name_Tata	= 0
            Brand_name_Toyota = 0	
            Brand_name_Volkswagen = 0	
            Brand_name_Volvo = 0
        elif Brand_Name == 'Honda':
            Brand_name_BMW = 0
            Brand_name_Chevrolet = 0	
            Brand_name_Datsun = 0
            Brand_name_Fiat	= 0
            Brand_name_Ford	= 0
            Brand_name_Honda = 1
            Brand_name_Hyundai = 0	
            Brand_name_Jeep	= 0
            Brand_name_KIA= 0
            Brand_name_MG = 0
            Brand_name_Mahindra	= 0
            Brand_name_Maruti = 0
            Brand_name_Mercedes = 0	
            Brand_name_Nissan = 0	
            Brand_name_Renault = 0	
            Brand_name_Skoda = 0	
            Brand_name_Ssangyong = 0	
            Brand_name_Tata	= 0
            Brand_name_Toyota = 0	
            Brand_name_Volkswagen = 0	
            Brand_name_Volvo = 0
        elif Brand_Name == 'Toyota':
            Brand_name_BMW = 0
            Brand_name_Chevrolet = 0	
            Brand_name_Datsun = 0
            Brand_name_Fiat	= 0
            Brand_name_Ford	= 0
            Brand_name_Honda = 0
            Brand_name_Hyundai = 0	
            Brand_name_Jeep	= 0
            Brand_name_KIA= 0
            Brand_name_MG = 0
            Brand_name_Mahindra	= 0
            Brand_name_Maruti = 0
            Brand_name_Mercedes = 0	
            Brand_name_Nissan = 0	
            Brand_name_Renault = 0	
            Brand_name_Skoda = 0	
            Brand_name_Ssangyong = 0	
            Brand_name_Tata	= 0
            Brand_name_Toyota = 1	
            Brand_name_Volkswagen = 0	
            Brand_name_Volvo = 0
        elif Brand_Name == 'Ford':
            Brand_name_BMW = 0
            Brand_name_Chevrolet = 0	
            Brand_name_Datsun = 0
            Brand_name_Fiat	= 0
            Brand_name_Ford	= 1
            Brand_name_Honda = 0
            Brand_name_Hyundai = 0	
            Brand_name_Jeep	= 0
            Brand_name_KIA= 0
            Brand_name_MG = 0
            Brand_name_Mahindra	= 0
            Brand_name_Maruti = 0
            Brand_name_Mercedes = 0	
            Brand_name_Nissan = 0	
            Brand_name_Renault = 0	
            Brand_name_Skoda = 0	
            Brand_name_Ssangyong = 0	
            Brand_name_Tata	= 0
            Brand_name_Toyota = 0	
            Brand_name_Volkswagen = 0	
            Brand_name_Volvo = 0
        elif Brand_Name == 'Renault':
            Brand_name_BMW = 0
            Brand_name_Chevrolet = 0	
            Brand_name_Datsun = 0
            Brand_name_Fiat	= 0
            Brand_name_Ford	= 0
            Brand_name_Honda = 0
            Brand_name_Hyundai = 0	
            Brand_name_Jeep	= 0
            Brand_name_KIA= 0
            Brand_name_MG = 0
            Brand_name_Mahindra	= 0
            Brand_name_Maruti = 0
            Brand_name_Mercedes = 0	
            Brand_name_Nissan = 0	
            Brand_name_Renault = 1	
            Brand_name_Skoda = 0	
            Brand_name_Ssangyong = 0	
            Brand_name_Tata	= 0
            Brand_name_Toyota = 0	
            Brand_name_Volkswagen = 0	
            Brand_name_Volvo = 0
        elif Brand_Name == 'Volkswagen':
            Brand_name_BMW = 0
            Brand_name_Chevrolet = 0	
            Brand_name_Datsun = 0
            Brand_name_Fiat	= 0
            Brand_name_Ford	= 0
            Brand_name_Honda = 0
            Brand_name_Hyundai = 0	
            Brand_name_Jeep	= 0
            Brand_name_KIA= 0
            Brand_name_MG = 0
            Brand_name_Mahindra	= 0
            Brand_name_Maruti = 0
            Brand_name_Mercedes = 0	
            Brand_name_Nissan = 0	
            Brand_name_Renault = 0	
            Brand_name_Skoda = 0	
            Brand_name_Ssangyong = 0	
            Brand_name_Tata	= 0
            Brand_name_Toyota = 0	
            Brand_name_Volkswagen = 1	
            Brand_name_Volvo = 0
        elif Brand_Name == 'Mahindra':
            Brand_name_BMW = 0
            Brand_name_Chevrolet = 0	
            Brand_name_Datsun = 0
            Brand_name_Fiat	= 0
            Brand_name_Ford	= 0
            Brand_name_Honda = 0
            Brand_name_Hyundai = 0	
            Brand_name_Jeep	= 0
            Brand_name_KIA= 0
            Brand_name_MG = 0
            Brand_name_Mahindra	= 1
            Brand_name_Maruti = 0
            Brand_name_Mercedes = 0	
            Brand_name_Nissan = 0	
            Brand_name_Renault = 0	
            Brand_name_Skoda = 0	
            Brand_name_Ssangyong = 0	
            Brand_name_Tata	= 0
            Brand_name_Toyota = 0	
            Brand_name_Volkswagen = 0	
            Brand_name_Volvo = 0
        elif Brand_Name == 'Mercedes':
            Brand_name_BMW = 0
            Brand_name_Chevrolet = 0	
            Brand_name_Datsun = 0
            Brand_name_Fiat	= 0
            Brand_name_Ford	= 0
            Brand_name_Honda = 0
            Brand_name_Hyundai = 0	
            Brand_name_Jeep	= 0
            Brand_name_KIA= 0
            Brand_name_MG = 0
            Brand_name_Mahindra	= 0
            Brand_name_Maruti = 0
            Brand_name_Mercedes = 1	
            Brand_name_Nissan = 0	
            Brand_name_Renault = 0	
            Brand_name_Skoda = 0	
            Brand_name_Ssangyong = 0	
            Brand_name_Tata	= 0
            Brand_name_Toyota = 0	
            Brand_name_Volkswagen = 0	
            Brand_name_Volvo = 0
        elif Brand_Name == 'Skoda':
            Brand_name_BMW = 0
            Brand_name_Chevrolet = 0	
            Brand_name_Datsun = 0
            Brand_name_Fiat	= 0
            Brand_name_Ford	= 0
            Brand_name_Honda = 0
            Brand_name_Hyundai = 0	
            Brand_name_Jeep	= 0
            Brand_name_KIA= 0
            Brand_name_MG = 0
            Brand_name_Mahindra	= 0
            Brand_name_Maruti = 0
            Brand_name_Mercedes = 0	
            Brand_name_Nissan = 0	
            Brand_name_Renault = 0	
            Brand_name_Skoda = 1	
            Brand_name_Ssangyong = 0	
            Brand_name_Tata	= 0
            Brand_name_Toyota = 0	
            Brand_name_Volkswagen = 0	
            Brand_name_Volvo = 0
        elif Brand_Name == 'Chevrolet':
            Brand_name_BMW = 0
            Brand_name_Chevrolet = 1	
            Brand_name_Datsun = 0
            Brand_name_Fiat	= 0
            Brand_name_Ford	= 0
            Brand_name_Honda = 0
            Brand_name_Hyundai = 0	
            Brand_name_Jeep	= 0
            Brand_name_KIA= 0
            Brand_name_MG = 0
            Brand_name_Mahindra	= 0
            Brand_name_Maruti = 0
            Brand_name_Mercedes = 0	
            Brand_name_Nissan = 0	
            Brand_name_Renault = 0	
            Brand_name_Skoda = 0	
            Brand_name_Ssangyong = 0	
            Brand_name_Tata	= 0
            Brand_name_Toyota = 0	
            Brand_name_Volkswagen = 0	
            Brand_name_Volvo = 0
        elif Brand_Name == 'Nissan':
            Brand_name_BMW = 0
            Brand_name_Chevrolet = 0	
            Brand_name_Datsun = 0
            Brand_name_Fiat	= 0
            Brand_name_Ford	= 0
            Brand_name_Honda = 0
            Brand_name_Hyundai = 0	
            Brand_name_Jeep	= 0
            Brand_name_KIA= 0
            Brand_name_MG = 0
            Brand_name_Mahindra	= 0
            Brand_name_Maruti = 0
            Brand_name_Mercedes = 0	
            Brand_name_Nissan = 1	
            Brand_name_Renault = 0	
            Brand_name_Skoda = 0	
            Brand_name_Ssangyong = 0	
            Brand_name_Tata	= 0
            Brand_name_Toyota = 0	
            Brand_name_Volkswagen = 0	
            Brand_name_Volvo = 0
        elif Brand_Name == 'Fiat':
            Brand_name_BMW = 0
            Brand_name_Chevrolet = 0	
            Brand_name_Datsun = 0
            Brand_name_Fiat	= 1
            Brand_name_Ford	= 0
            Brand_name_Honda = 0
            Brand_name_Hyundai = 0	
            Brand_name_Jeep	= 0
            Brand_name_KIA= 0
            Brand_name_MG = 0
            Brand_name_Mahindra	= 0
            Brand_name_Maruti = 0
            Brand_name_Mercedes = 0	
            Brand_name_Nissan = 0	
            Brand_name_Renault = 0	
            Brand_name_Skoda = 0	
            Brand_name_Ssangyong = 0	
            Brand_name_Tata	= 0
            Brand_name_Toyota = 0	
            Brand_name_Volkswagen = 0	
            Brand_name_Volvo = 0
        elif Brand_Name == 'KIA':
            Brand_name_BMW = 0
            Brand_name_Chevrolet = 0	
            Brand_name_Datsun = 0
            Brand_name_Fiat	= 0
            Brand_name_Ford	= 0
            Brand_name_Honda = 0
            Brand_name_Hyundai = 0	
            Brand_name_Jeep	= 0
            Brand_name_KIA= 1
            Brand_name_MG = 0
            Brand_name_Mahindra	= 0
            Brand_name_Maruti = 0
            Brand_name_Mercedes = 0	
            Brand_name_Nissan = 0	
            Brand_name_Renault = 0	
            Brand_name_Skoda = 0	
            Brand_name_Ssangyong = 0	
            Brand_name_Tata	= 0
            Brand_name_Toyota = 0	
            Brand_name_Volkswagen = 0	
            Brand_name_Volvo = 0
        elif Brand_Name == 'Ssangyong':
            Brand_name_BMW = 0
            Brand_name_Chevrolet = 0	
            Brand_name_Datsun = 0
            Brand_name_Fiat	= 0
            Brand_name_Ford	= 0
            Brand_name_Honda = 0
            Brand_name_Hyundai = 0	
            Brand_name_Jeep	= 0
            Brand_name_KIA= 0
            Brand_name_MG = 0
            Brand_name_Mahindra	= 0
            Brand_name_Maruti = 0
            Brand_name_Mercedes = 0	
            Brand_name_Nissan = 0	
            Brand_name_Renault = 0	
            Brand_name_Skoda = 0	
            Brand_name_Ssangyong = 1	
            Brand_name_Tata	= 0
            Brand_name_Toyota = 0	
            Brand_name_Volkswagen = 0	
            Brand_name_Volvo = 0
        elif Brand_Name == 'MG':
            Brand_name_BMW = 0
            Brand_name_Chevrolet = 0	
            Brand_name_Datsun = 0
            Brand_name_Fiat	= 0
            Brand_name_Ford	= 0
            Brand_name_Honda = 0
            Brand_name_Hyundai = 0	
            Brand_name_Jeep	= 0
            Brand_name_KIA= 0
            Brand_name_MG = 1
            Brand_name_Mahindra	= 0
            Brand_name_Maruti = 0
            Brand_name_Mercedes = 0	
            Brand_name_Nissan = 0	
            Brand_name_Renault = 0	
            Brand_name_Skoda = 0	
            Brand_name_Ssangyong = 0	
            Brand_name_Tata	= 0
            Brand_name_Toyota = 0	
            Brand_name_Volkswagen = 0	
            Brand_name_Volvo = 0
        elif Brand_Name == 'Volvo':
            Brand_name_BMW = 0
            Brand_name_Chevrolet = 0	
            Brand_name_Datsun = 0
            Brand_name_Fiat	= 0
            Brand_name_Ford	= 0
            Brand_name_Honda = 0
            Brand_name_Hyundai = 0	
            Brand_name_Jeep	= 0
            Brand_name_KIA= 0
            Brand_name_MG = 0
            Brand_name_Mahindra	= 0
            Brand_name_Maruti = 0
            Brand_name_Mercedes = 0	
            Brand_name_Nissan = 0	
            Brand_name_Renault = 0	
            Brand_name_Skoda = 0	
            Brand_name_Ssangyong = 0	
            Brand_name_Tata	= 0
            Brand_name_Toyota = 0	
            Brand_name_Volkswagen = 0	
            Brand_name_Volvo = 1
        elif Brand_Name == 'Jeep':
            Brand_name_BMW = 0
            Brand_name_Chevrolet = 0	
            Brand_name_Datsun = 0
            Brand_name_Fiat	= 0
            Brand_name_Ford	= 0
            Brand_name_Honda = 0
            Brand_name_Hyundai = 0	
            Brand_name_Jeep	= 1
            Brand_name_KIA= 0
            Brand_name_MG = 0
            Brand_name_Mahindra	= 0
            Brand_name_Maruti = 0
            Brand_name_Mercedes = 0	
            Brand_name_Nissan = 0	
            Brand_name_Renault = 0	
            Brand_name_Skoda = 0	
            Brand_name_Ssangyong = 0	
            Brand_name_Tata	= 0
            Brand_name_Toyota = 0	
            Brand_name_Volkswagen = 0	
            Brand_name_Volvo = 0
        else:
            Brand_name_BMW = 0
            Brand_name_Chevrolet = 0	
            Brand_name_Datsun = 0
            Brand_name_Fiat	= 0
            Brand_name_Ford	= 0
            Brand_name_Honda = 0
            Brand_name_Hyundai = 0	
            Brand_name_Jeep	= 0
            Brand_name_KIA= 0
            Brand_name_MG = 0
            Brand_name_Mahindra	= 0
            Brand_name_Maruti = 0
            Brand_name_Mercedes = 0	
            Brand_name_Nissan = 0	
            Brand_name_Renault = 0	
            Brand_name_Skoda = 0	
            Brand_name_Ssangyong = 0	
            Brand_name_Tata	= 0
            Brand_name_Toyota = 0	
            Brand_name_Volkswagen = 0	
            Brand_name_Volvo = 0
        
                
        


        prediction = model.predict([[
            Years,
            Brand_name_BMW, 
            Brand_name_Chevrolet, 
            Brand_name_Datsun,
            Brand_name_Fiat, 
            Brand_name_Ford, 
            Brand_name_Honda,
            Brand_name_Hyundai, 
            Brand_name_Jeep, 
            Brand_name_KIA,
            Brand_name_MG, 
            Brand_name_Mahindra, 
            Brand_name_Maruti,
            Brand_name_Mercedes, 
            Brand_name_Nissan, 
            Brand_name_Renault,
            Brand_name_Skoda, 
            Brand_name_Ssangyong, 
            Brand_name_Tata,
            Brand_name_Toyota, 
            Brand_name_Volkswagen, 
            Brand_name_Volvo,
            Fuel_Type_Petrol, 
            Fuel_Type_Petrol_CNG, 
            Fuel_Type_Petrol_LPG,
            Owner_Type_First_Owner, 
            Owner_Type_Fourth_Owner,
            Owner_Type_Second_Owner, 
            Owner_Type_Sixth_Owner,
            Owner_Type_Third_Owner, 
            Insurance_Type_Comp,
            Insurance_Type_Comprehensive, 
            Insurance_Type_Expired,
            Insurance_Type_Insurance_Expired, 
            Insurance_Type_Third_party,
            Insurance_Type_Zero_Depreciation, 
            Insurance_Type_Zero_Dep,
            RTO_Other_State, 
            Transmission_Type_MANUAL, 
            Kilometers
            ]])
    #     print('Years', 'Brand_name_BMW', 'Brand_name_Chevrolet', 'Brand_name_Datsun',
    #    'Brand_name_Fiat', 'Brand_name_Ford', 'Brand_name_Honda',
    #    'Brand_name_Hyundai', 'Brand_name_Jeep', 'Brand_name_KIA',
    #    'Brand_name_MG', 'Brand_name_Mahindra', 'Brand_name_Maruti',
    #    'Brand_name_Mercedes', 'Brand_name_Nissan', 'Brand_name_Renault',
    #    'Brand_name_Skoda', 'Brand_name_Ssangyong', 'Brand_name_Tata',
    #    'Brand_name_Toyota', 'Brand_name_Volkswagen', 'Brand_name_Volvo',
    #    'Fuel_Type_Petrol', 'Fuel_Type_Petrol_CNG', 'Fuel_Type_Petrol_LPG',
    #    'Owner_Type_First_Owner', 'Owner_Type_Fourth_Owner',
    #    'Owner_Type_Second_Owner', 'Owner_Type_Sixth_Owner',
    #    'Owner_Type_Third_Owner', 'Insurance_Type_Comp',
    #    'Insurance_Type_Comprehensive', 'Insurance_Type_Expired',
    #    'Insurance_Type_Insurance_Expired', 'Insurance_Type_Third_party',
    #    'Insurance_Type_Zero_Depreciation', 'Insurance_Type_Zero_Dep',
    #    'RTO_Other_State', 'Transmission_Type_MANUAL', 'Kilometers')
        output=round(prediction[0],2)

        return render_template('home.html',prediction_text="Your Car price is Rs. {}".format(output))


    return render_template("home.html")



# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5000)


import pandas as pd # type: ignore
import numpy as np # type: ignore
import seaborn as sns # type: ignore
import matplotlib.pyplot as plt # type: ignore
import statistics as st # type: ignore
from statistics import mean # type: ignore
from sklearn import linear_model # type: ignore
from scipy import stats # type: ignore

def dateconvert(string):
    dateint = 0
    monthlist = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    year = int(string[0:4])
    month = int(string[5:7])
    day = int(string[8:10])
    dateint = dateint + 365*(year-2013) + int((year-2012)/4)
    for i in range(month-1):
        dateint = dateint + monthlist[i]
    dateint = dateint + day
    
    return dateint

def riskCalcAlg(State, city, date):
    gun_data_filtered = gun_data.loc[gun_data["state"]==State]
    #print(gun_data_filtered)
    gun_data_filtered2 = gun_data_filtered.loc[gun_data_filtered["city_or_county"]==city]
    #print(gun_data_filtered2)
    
    X = gun_data_filtered2[["intDate"]]
    y = gun_data_filtered2[["risk"]]

    model = linear_model.LinearRegression()

    model.fit(X,y)

    y_pred = model.predict(X)    
    '''
    prints out the graph using plt...if yall can figure out how to implement this then great, but for rn it'll stay commented
    '''
    plt.plot(gun_data["intDate"], y_pred, color='red')
    plt.scatter(X, y) 
    plt.savefig('plt.png')
    plt.show()  
    predrisk = model.intercept_ + model.coef_*(dateconvert(date))
    print(model.intercept_)
    print(model.coef_)
    return round(predrisk[0][0]/meanrisk,3)*100

def runner():
    global gun_dataset, gun_data, gun_datalist, risklist, totalrisk, meanrisk
    pd.read_csv("GunViolence.csv")
    gun_data = gun_dataset.filter(["incident_id", "date", "state", "city_or_county", "n_killed", "n_injured"], axis = 1)
    gun_datalist = []
    for i in range(len(gun_data)):
        gun_datalist.append((dateconvert(gun_data.loc[i,"date"])))

    gun_data["intDate"] = gun_datalist
    
    risklist = []
    totalrisk = 0
    ct = 0
    for i in range(len(gun_data)):
        temp = 10*gun_data.loc[i,"n_killed"]+2*gun_data.loc[i,"n_injured"]
        risklist.append(temp)
        totalrisk = totalrisk + temp
        ct+=1
    #print(risklist)
    meanrisk = totalrisk/ct
    #print(maxrisk)
    gun_data["risk"] = risklist

    print(riskCalcAlg("New Hampshire", "Nashua", "2025/03/25"))
    print("success!")
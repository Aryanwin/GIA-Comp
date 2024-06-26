import pandas as pd
import numpy as np
from pyodide.http import open_url

dataSheet = pd.read_csv(open_url("gun-violence-data_01-2013_03-2018.csv"))
# dataSheet = pd.read_csv(open_url("Agrofood_co2_emission.csv"))

# def testFile(*args, **kwargs):
#     output = Element("output_div")
#     # crimeStates = dataSheet["state"]
#     # output.write(crimeStates[0])
#     output.write("Test")

def testFile(*args, **kwargs):
        state_box = Element("stateBox")
        city_box = Element("cityBox")
        state_input = state_box.value
        city_input = city_box.value
        output = Element("output_div")
        crimeStates = dataSheet["state"]
        crimeCities = dataSheet["city_or_county"]
        matchingList = []
        for i in range(len(crimeStates)):
            if ((crimeStates[i] == state_input) and (crimeCities[i] == city_input)):
                 matchingList.append(i) 
        # output.write(crimeStates[0])
        output.write(matchingList)
        # output.write("Hello")

import pandas as pd
import numpy as np
from pyodide.http import open_url
from pyscript import window, document
from riskCalcAlg import runner

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
    crimeStates = dataSheet["state"]
    crimeCities = dataSheet["city_or_county"]
    runner()
    document.querySelector("#imgOutput").src = "plt.png"

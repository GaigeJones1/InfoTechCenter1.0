print("\n**********************************************\n")

print("Gasoline Branch\n")

import random
from time import sleep

def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    return random.choice(gasLevelList)

def gasStations():
    gasStationsList = ["VP", "shell", "Meijer", "Sams Club", "Marathon", "Mobile", "Speedway", "Circle K"]
    return random.choice(gasStationsList)

def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1, 25), 1)
    milesToGasStationQuarterTank = round(random.uniform(25.1, 50), 1)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("***WARNING YOU ARE ON EMPTY***\n")
        sleep(2)
        print("Calling Triple AAA")
    elif gasLevelIndicator == "Low":
        print("Your gas tank is extremely low, checking GPS for the closest gas station.")
        sleep(2)
        print("The closest gas station is", gasStations(), "which is", milesToGasStationLow, "miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is on a quarter of a tank, checking GPS for gas stations.")
        sleep(2)
        print("The gas station found is", gasStations(), "which is", milesToGasStationQuarterTank, "miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is half a tank full which is plenty to get to your destination.")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is three quarters of a tank full which is plenty to get to your destination.")
    else:
        print("You have a full tank! You are all good to make it to your destination today.")

gasLevelAlert()
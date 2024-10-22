import random
from time import sleep

# Separator for visual clarity
print("\n**********************************************\n")
print("Gasoline Branch\n")


# Function to simulate the gas level reading
def gasLevelGauge():
    # Possible gas levels
    return random.choice(["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"])


# Function to simulate finding a random gas station
def gasStations():
    # List of gas stations
    return random.choice(["VP", "Shell", "Meijer", "Sam's Club", "Marathon", "Mobil", "Speedway", "Circle K"])


# Function to handle gas level alerts and responses
def gasLevelAlert():
    # Get the current gas level and a random gas station
    gasLevelIndicator = gasLevelGauge()
    gasStation = gasStations()

    # Define distances based on the gas level
    distances = {
        "Low": round(random.uniform(1, 25), 1),
        "Quarter Tank": round(random.uniform(25.1, 50), 1)
    }

    # Alert messages based on the gas level
    if gasLevelIndicator == "Empty":
        print("***WARNING YOU ARE ON EMPTY***\n")
        sleep(1)  # Short delay
        print("Calling Triple AAA.")
    elif gasLevelIndicator == "Low":
        print("Your gas tank is extremely low, checking GPS for the closest gas station.")
        sleep(1)
        print(f"The closest gas station is {gasStation}, which is {distances['Low']} miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is on a quarter of a tank, checking GPS for gas stations.")
        sleep(1)
        print(f"The gas station found is {gasStation}, which is {distances['Quarter Tank']} miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is half full, which is enough to get to your destination.")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is three-quarters full, you have plenty of fuel for your trip.")
    else:
        print("You have a full tank! You're good to go for the day.")


# Call the function to check gas level and print alerts
gasLevelAlert()
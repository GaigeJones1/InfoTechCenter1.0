import sys  # Importing sys module to use sys.stdout.write for printing without a newline.
import time  # Importing time module to create a delay using time.sleep.
import random
from time import sleep

# Adding color to the welcome message (using Cyan text color).
print("\033[96m\nWelcome to InfoTechCenter V1.0\n\033[0m")  # Cyan color

timeToSleep = 2 #Variable to set the time library to 2 seconds when called
time.sleep(timeToSleep) #Calling the time sleep library with the variable timeToSleep value

x = 0  # Counter to keep track of the number of iterations in the loop.
ellipsis = 0  # Counter to control the number of dots displayed after the message.

# A while loop that will run 20 times to simulate a booting process.
while x != 20:
    x += 1  # Increment the loop counter by 1 in each iteration.

    # Dynamically updating the message with a varying number of dots at the end (in Yellow).
    message = "\033[93m" + ("Infotech Center System Booting" + "." * ellipsis) + "\033[0m"  # Yellow color

    ellipsis += 1  # Increment the ellipsis counter to increase the number of dots.

    # Using sys.stdout.write with "\r" to overwrite the previous line with the updated message.
    sys.stdout.write("\r" + message)

    time.sleep(0.25)  # Adding a delay of 0.25 seconds to simulate a booting process.

    # Resetting the ellipsis counter to 0 after reaching 3 dots, to keep it between 0 and 3.
    if ellipsis == 4:
        ellipsis = 0

    # When the loop counter reaches 20, the booting process is considered complete.
    if x == 20:
        # Adding color to the final message (using Green text color).
        print("\033[92m\n\nOperating System Booted Up - Retina Scanned - Access Granted\033[0m")  # Green color

# Print decorative lines and a section title for clarity
print("\n**********************************************\n")
print("Weather Branch\n")

# Import necessary libraries

# Define a function that randomly selects a weather condition from a list
def weather():
    weatherForecast = ["snowy", "blizzard", "rainy", "windy", "icy", "sunny"]
    return random.choice(weatherForecast)


# Call the weather function and store the result in weatherAlert
weatherAlert = weather()


# Define the Vehicle Response System (VRS) function to give responses based on the weather condition
def vehicleResponseSystem():
    # Dictionary mapping weather conditions to delay times and speed limits
    weather_responses = {
        "snowy": (30, 55),
        "blizzard": (45, 45),
        "rainy": (15, 65),
        "windy": (5, 75),
        "icy": (50, 30),
        "sunny": (0, None)  # None indicates no speed limit restriction
    }

    delay, speed_limit = weather_responses.get(weatherAlert, (0, None))  # Default is sunny-like behavior

    if speed_limit is not None:
        print(
            f"\nThe National Weather Service has updated our alarm by {delay} minutes because of the forecast of {weatherAlert} weather conditions.")
        sleep(1)
        print(f"\nVRS System has been engaged, only allowing you to drive {speed_limit} mph.")
    else:
        print(
            f"The National Weather Service is calling for {weatherAlert} skies, drive carefully to get to your destination.")
        sleep(1)
        print("\nVRS system has been disengaged.")


# Call the Vehicle Response System function to execute the program logic
vehicleResponseSystem()


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

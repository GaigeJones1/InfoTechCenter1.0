# Print decorative lines and a section title for clarity
print("\n*****************************\n")
print("Weather Branch\n")

# Import necessary libraries: 
# 'random' is used for randomly selecting a weather condition,
# 'sleep' from 'time' introduces delays in output to simulate processing.
import random
from time import sleep


# Define a function that randomly selects a weather condition from a list
def weather():
    weatherForecast = ["snowy", "blizzard", "rainy", "windy", "icy", "sunny"]
    # Randomly choose a condition from the weatherForecast list
    weatherCondition = random.choice(weatherForecast)
    return weatherCondition


# Call the weather function and store the result in weatherAlert
weatherAlert = weather()


# Define the Vehicle Response System (VRS) function to give different responses based on the weather condition
def vehicleResponseSytem():
    # Check if the weather is "snowy"
    if weatherAlert == "snowy":
        print("\nThe National Weather Service has updated our alarm by 30 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        # Pause for 1 second before the next print statement
        sleep(1)
        print("\nVRS System has been engaged only allowing you to drive 55mph.")

    # Check if the weather is "blizzard"
    elif weatherAlert == "blizzard":
        print("\nThe National Weather Service has updated our alarm by 45 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS System has been engaged only allowing you to drive 45mph.")

    # Check if the weather is "rainy"
    elif weatherAlert == "rainy":
        print("\nThe National Weather Service has updated our alarm by 15 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS System has been engaged only allowing you to drive 65mph.")

    # Check if the weather is "windy"
    elif weatherAlert == "windy":
        print("\nThe National Weather Service has updated our alarm by 5 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS System has been engaged only allowing you to drive 75mph.")

    # Check if the weather is "icy"
    elif weatherAlert == "icy":
        print("\nThe National Weather Service has updated our alarm by 50 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS System has been engaged only allowing you to drive 30mph.")

    # If none of the above conditions are met (meaning the weather is "sunny")
    else:
        print("The National Weather Service is calling for", weatherAlert,
              "skies, drive carefully to get to your destination.")
        sleep(1)
        print("\nVRS system has been disengaged")


# Call the Vehicle Response System function to execute the program logic
vehicleResponseSytem()

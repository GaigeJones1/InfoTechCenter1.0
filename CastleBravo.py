# Print decorative lines and a section title for clarity
print("\n*****************************\n")
print("Weather Branch\n")

# Import necessary libraries
import random
from time import sleep


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

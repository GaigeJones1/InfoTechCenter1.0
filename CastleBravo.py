import sys  # Importing sys module to use sys.stdout.write for printing without a newline.
import time  # Importing time module to create a delay using time.sleep.

# Adding color to the welcome message (using Cyan text color).
print("\033[96m\nWelcome to InfoTechCenter V1.0\n\033[0m")  # Cyan color

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

    time.sleep(.5)  # Adding a delay of 0.5 seconds to simulate a booting process.

    # Resetting the ellipsis counter to 0 after reaching 3 dots, to keep it between 0 and 3.
    if ellipsis == 4:
        ellipsis = 0

    # When the loop counter reaches 20, the booting process is considered complete.
    if x == 20:
        # Adding color to the final message (using Green text color).
        print("\033[92m\n\nOperating System Booted Up - Retina Scanned - Access Granted\033[0m")  # Green color


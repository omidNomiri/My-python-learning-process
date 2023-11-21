hours = float(input("Please enter your hour: "))
minutes = float(input("Please enter your minute: "))
seconds = float(input("Please enter your second: "))

seconds = seconds + 60 * minutes + 3600 * hours

print(seconds)

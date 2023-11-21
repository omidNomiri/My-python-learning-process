seconds = int(input("Please enter your second: "))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = (seconds % 3600) % 60

print(f"{hours}:{minutes}:{seconds}")
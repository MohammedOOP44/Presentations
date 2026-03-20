seconds = int(input("Enter the seconds: "))
hours = seconds // 3600
minutes = (seconds % 3600) // 60

print("these seconds mean: " + str(hours) + " hours and " + str(minutes) + " minutes")

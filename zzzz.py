from datetime import datetime

# Assuming the time is in 24-hour format
time_str = "14:06"

# Convert the time string to datetime object
time_obj = datetime.strptime(time_str, "%H:%M")

# Convert to 12-hour format and determine AM/PM
time_12hr_str = time_obj.strftime('%I:%M %p')

print("Time in 12-hour format:", time_12hr_str)
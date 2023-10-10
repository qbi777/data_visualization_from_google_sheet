import gspread
from oauth2client.service_account import ServiceAccountCredentials
import matplotlib.pyplot as plt

file = gspread.service_account(filename = "service_account.json")
workbook = file.open("pythonedit")
sheet = workbook.worksheet("ARM")

data = sheet.get_all_records()

# Extract data into separate lists
temperatures = [record['Temperature(\'c)'] for record in data]
heart_rates = [record['Heart Rate(BPM)'] for record in data]

# Create a time variable (assuming data is ordered by time)
time = list(range(1, len(data) + 1))

# Create a line graph to visualize temperature and heart rate over time
plt.figure(figsize=(10, 6))
plt.plot(time, temperatures, label='Temperature (°C)', marker='o', linestyle='-')
plt.plot(time, heart_rates, label='Heart Rate (BPM)', marker='x', linestyle='-')

# Customize the graph
plt.xlabel("Time")
plt.ylabel("Values")
plt.title("Temperature and Heart Rate Over Time")
plt.legend()

# Show the graph
plt.grid(True)
plt.show()

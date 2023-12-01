import pandas as pd
import matplotlib.pyplot as plt

# Read temperature data from the CSV file
data = pd.read_csv('temperature_data.csv', skiprows=1)


# Separate data for each rack
racks = {}

for index, entry in data.iterrows():
    rack = entry[0]
    if(rack>2):
        continue
    temperature = entry[2]
    if rack not in racks:
        racks[rack] = {'x': [], 'y': []}
    
    racks[rack]['x'].append(len(racks[rack]['x']))
    racks[rack]['y'].append(temperature)

# Plot each rack separately
for rack, values in racks.items():
    plt.plot(values['x'], values['y'], label=f'Rack {rack}')

# Add labels and legend
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.legend()

# Save the plot as a PNG file
plt.savefig('temperature_plot.png')

# Display the plot
plt.show()

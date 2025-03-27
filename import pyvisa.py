import pyvisa
import numpy as np
import matplotlib.pyplot as plt

rm = pyvisa.ResourceManager()
gaussmeter = rm.open_resource("GPIB0::12::INSTR") #Will be changed to specific device adress

def read_magnetic_field():
    try:
        response = gaussmeter.query("RDGFIELD?") #command to read field (check manual)
        return float(response)
    except Exception as e:
        print(f"error reading field: {e}")
        return None
    
    #sample data collection (replace with real current values)
current_values = np.linspace(0, 10, 10) #simulated current values from 0 to 10A
magnetic_fields = []

for current in current_values:
    input(f"Set current to {current}A and press Enter to take reading...")
    field_value = read_magnetic_field()
    if field_value is not None:
        magnetic_fields.append(field_value)
    else:
        magnetic_fields.append(0)


plt.plot(current_values, magnetic_fields, marker='o', linestyle='-')
plt.xlabel("Current (A)")
plt.ylabel("Magentic Field (Gauss)")
plt.title("Magnetic Field vs. Current")
plt.grid(True)
plt.show()


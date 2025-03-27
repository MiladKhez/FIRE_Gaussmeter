import numpy as np
import matplotlib.pyplot as plt

# Simulated function to replace real Gaussmeter readings
def read_magnetic_field():
    return np.random.uniform(100, 200)  # Fake field values between 100-200 Gauss

# Simulated current values
current_values = np.linspace(0, 10, 10)
magnetic_fields = [read_magnetic_field() for _ in current_values]

# Plot results
plt.plot(current_values, magnetic_fields, marker='o', linestyle='-')
plt.xlabel("Current (A)")
plt.ylabel("Magnetic Field (Gauss)")
plt.title("Simulated Magnetic Field vs. Current")
plt.grid(True)
plt.show()

import pyvisa

rm = pyvisa.ResourceManager()
print("Available devices:", rm.list_resources())

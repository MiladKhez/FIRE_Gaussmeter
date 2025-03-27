import pyvisa

# Initialize the VISA Resource Manager
rm = pyvisa.ResourceManager()

# Connect to the Gaussmeter using the correct address
gaussmeter = rm.open_resource('ASRL5::INSTR')

# Set the serial communication settings to match the Gaussmeter
gaussmeter.baud_rate = 57600  # Set baud rate
gaussmeter.data_bits = 8       # Set data bits (typically 8)
gaussmeter.parity = pyvisa.constants.Parity.none  # No parity
gaussmeter.stop_bits = pyvisa.constants.StopBits.one  # One stop bit
gaussmeter.timeout = 5000  # Timeout set to 5 seconds

# Query the Gaussmeter to retrieve its identity
try:
    print(gaussmeter.query("*IDN?"))  # This should return the identity of the device
except Exception as e:
    print(e)

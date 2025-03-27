from serial import *
from time import *
import serial.tools.list_ports
import ast

ports = sorted(serial.tools.list_ports.comports())

for port in ports:
    print(port.description)

class Instrument():
    def __init__(self, com_port='COM5',
                baudrate=57600, 
                bytesize=serial.SEVENBITS, 
                parity=serial.PARITY_ODD, 
                stopbits=serial.STOPBITS_ONE, 
                timeout=5):
        self.com_port=com_port
        self.baudrate=baudrate
        self.bytesize=bytesize
        self.parity=parity
        self.stopbits=stopbits
        self.timeout=timeout
        self.inst=None

    def connect(self):
        if self.inst is None:
            self.inst = serial.Serial(self.com_port, 
                                      baudrate=self.baudrate, 
                                      bytesize=self.bytesize,
                                      parity=self.parity,
                                      stopbits=self.stopbits,
                                      timeout=self.timeout)
            if self.inst.is_open:
                inst = self.inst
                print(f"Connected to {inst.name}")

                self.sendCommand('*IDN?')

                sleep(1)

                response = self.read(show=False)
                print(f"Instrument ID: {response}")
        else:
            try:
                self.inst.is_open
                print("Instrument already open!")
            except Exception as e:
                print(f"Error: {e}")

    def read(self, show=True):
        response = self.inst.read_all().decode('ascii', errors='ignore')
        if show:
            print(response)
        return response

    def sendCommand(self, command):
        if self.inst is not None:
            try:
                self.inst.write(f'{command}\n'.encode('ascii'))
            except Exception as e:
                print(f'Error sending command: {e}')

    def measureProbe(self, delay=1e-1):
        self.sendCommand('RDGFIELD?')
        sleep(delay)
        magnitude = self.read(show=False)
        return magnitude

gaussmeter = Instrument()
gaussmeter.connect()

measurements={}
t1=time()
while True:
    magnitude = ast.literal_eval(gaussmeter.measureProbe())
    t2=time()
    measurements[t2 - t1]=magnitude
    print(f"{t2 - t1:.2f}: {str(magnitude)}             ", end='\r')
    if t2 - t1 >= 10:
        break

for t in measurements:
    print(f'{t}: {measurements[t]}')

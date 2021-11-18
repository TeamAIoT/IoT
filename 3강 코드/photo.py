import smbus
import time

address = 0x48
A0 = 0x40
A1 = 0x41
bus = smbus.SMBus(1)

while True:
    bus.write_byte(address,A0)
    value = bus.read_byte(address)
    bus.write_byte(address,A1)
    value2 = bus.read_byte(address)
    print('AIN0 = ',value)
    print('AIN1 = ',value2)
    time.sleep(0.1)
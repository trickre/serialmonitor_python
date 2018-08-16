# Serialmonitor_Python

import serial

def main():
    sp = serial.Serial("COM3",timeout=10)
    sp.baudrate = 9600
    sp.read_until(b"!")
    recv = sp.read(100)
    print(recv)

if(__name__ == "__main__"):
    main()
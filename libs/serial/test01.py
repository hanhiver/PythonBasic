import serial

try:
    portx='/dev/ttyS0'

    bps = 115200

    timex = 5

    ser = serial.Serial(portx, bps, timeout= timex)

    result = ser.write('Hello! Serial Port!'.encode())
    print("Write {} bites.".format(result))

    ser.close()

except Exception as e:
    print("ERROR: ", e)



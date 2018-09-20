from bottle import route, run, template
import time

import Adafruit_GPIO.SPI as SPI
import MAX6675.MAX6675 as MAX6675

# Raspberry Pi software SPI configuration.
# CLK = 25
# CS  = 24
# DO  = 18
# sensor = MAX6675.MAX6675(CLK, CS, DO)

# Raspberry Pi hardware SPI configuration.
#SPI_PORT   = 0
#SPI_DEVICE = 0
#sensor = MAX6675.MAX6675(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))1

@route('/bbq/sensors/temp/<sensorId>')
def temp(sensorId):
    return template('sensor {{sensorId}} value', sensorId=sensorId)

@route('/bbq/sensors/max6675/')
def max6675():
	temp = sensor.readTempC()
	print 'Thermocouple Temperature: {0:0.3F}°C / {1:0.3F}°F'.format(temp, c_to_f(temp))
    return 'Thermocouple Temperature: {0:0.3F}°C / {1:0.3F}°F'.format(temp, c_to_f(temp))

# Define a function to convert celsius to fahrenheit.
def c_to_f(c):
        return c * 9.0 / 5.0 + 32.0
run(host='localhost', port=8080)

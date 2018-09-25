import wiringpi2 as wiringpi  
import time

wiringpi.pwmSetMode(0) # PWM_MODE_MS = 0

wiringpi.wiringPiSetupGpio()  

wiringpi.pinMode(18, 2)      # pwm only works on GPIO port 18  

wiringpi.pwmSetClock(6)  # this parameters correspond to 25kHz
wiringpi.pwmSetRange(128)

wiringpi.pwmWrite(18, 0)   # minimum RPM
time.sleep(1)
wiringpi.pwmWrite(18, 128)  # maximum RPM
time.sleep(1)

wiringpi.pwmWrite(18, 0)

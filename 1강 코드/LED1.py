import RPi.GPIO as GPIO
import time
LedPin = 17

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LedPin,GPIO.OUT)
    
def main():
    while True:
        print("LED ON\n")
        GPIO.output(LedPin,False)
        time.sleep(5)
        print("LED OFF\n")
        GPIO.output(LedPin,True)
        time.sleep(5)
def destroy():
    GPIO.output(LedPin,GPIO.HIGH)
    GPIO.cleanup()
    
if __name__ == "__main__":
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()
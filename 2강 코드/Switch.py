import RPi.GPIO as GPIO
from time import sleep

led = 17
switch = 18
state = True
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(18,GPIO.IN)
def swLed(ev=None):
    global state
    state = not state
    GPIO.output(17,state)
    if state:
        print("led on")
    else :
        print("led off")

def main():
    GPIO.add_event_detect(switch,GPIO.FALLING,callback=swLed)
    while True:
        sleep(1)
def destroy():
    GPIO.cleanup()
if __name__ == '__main__':
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()
    
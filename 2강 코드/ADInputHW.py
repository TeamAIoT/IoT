import RPi.GPIO as GPIO
import time
import smbus
def MAP(x,in_min,in_max,out_min,out_max):
    return (x-in_min)*(out_max-out_min)/(in_max-in_min)+out_min

led_pin = 17
address = 0x48
A0 = 0x40
bus = smbus.SMBus(1)

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led_pin,GPIO.OUT)
    GPIO.output(led_pin,GPIO.HIGH)
    global pwm_led
    pwm_led = GPIO.PWM(led_pin,500)
    pwm_led.start(100)
    
    
    
def destroy():
    GPIO.cleanup()
def main():
    while True:
        bus.write_byte(address,A0)
        value = bus.read_byte(address)
        pwm = int(MAP(value,0,255,0,100))
        pwm_led.ChangeDutyCycle(pwm)
        
        print("LED Brightness : %d"%(pwm))
        time.sleep(0.1)
if __name__ == "__main__":
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()
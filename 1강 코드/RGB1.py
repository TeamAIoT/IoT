import RPi.GPIO as GPIO
import time

COLOR = [0xFF0000, 0x00FF00,0x0000FF,0xFFFF00,0xFF00FF,0x00FFFF]

pins = {'Red':17,'Green':18,'Blue':19}

def setup():
    global p_R,p_G,p_B
    GPIO.setmode(GPIO.BCM)
    
    for i in pins:
        GPIO.setup(pins[i], GPIO.OUT)
        GPIO.output(pins[i],GPIO.HIGH)
    p_R = GPIO.PWM(pins['Red'],2000)      
    p_G = GPIO.PWM(pins['Green'],2000)
    p_B = GPIO.PWM(pins['Blue'],2000)
    p_R.start(0)
    p_G.start(0)
    p_B.start(0)
    
def MAP(x,in_min,in_max,out_min,out_max):
    return (x-in_min)*(out_max-out_min)/(in_max-in_min)+out_min

def setColor(color):
    R_val = (color & 0xFF0000)>>16
    G_val = (color & 0x00FF00)>>8
    B_val = (color & 0x0000FF)>>0
    
    R_val = MAP(R_val,0,255,0,100)
    G_val = MAP(G_val,0,255,0,100)
    B_val = MAP(B_val,0,255,0,100)
    
    p_R.ChangeDutyCycle(R_val)
    p_G.ChangeDutyCycle(G_val)
    p_B.ChangeDutyCycle(B_val)
    
    print("color_msg : R = %s, G = %s, B = %s"%(R_val,G_val,B_val))
def destroy():
    p_R.stop()
    p_G.stop()
    p_B.stop()
    for i in pins:
        GPIO.output(pins[i],GPIO.HIGH)
        GPIO.cleanup()
def main():
    while True:
        for color in COLOR:
            setColor(color)
            time.sleep(2)
if __name__ == "__main__":
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()
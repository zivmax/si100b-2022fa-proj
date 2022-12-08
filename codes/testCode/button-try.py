import RPi.GPIO as GPIO
import time


BtnPin = 31
LedPin = 33
Led_status = False


def main():

    setup()

    loop()


def setup():

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LedPin, GPIO.OUT)
    GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.output(LedPin, False)


def swLED(self):

    global Led_status
    Led_status = not Led_status

    GPIO.output(LedPin, Led_status)

    if Led_status == False:
        print('LED Off')

    else:
        print('LED On')


def loop():

    GPIO.add_event_detect(BtnPin, GPIO.FALLING)
    GPIO.add_event_callback(BtnPin, swLED, bouncetime = 250)

    while True:
        time.sleep(1)

if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("")

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from send_status import sendStatus
import time

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering

class StatusSelection:
    
    def __init__(self, gpio, emoji, message):
        self.__gpio = gpio
        self.__emoji = emoji
        self.__message = message
        self.__selected = False
        
        GPIO.setup(self.__gpio, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.__gpio, GPIO.RISING, callback=self.select, bouncetime=500)

    def getGPIO(self):
        return self.__gpio

    def getEmoji(self):
        return self.__emoji

    def getMessage(self):
        return self.__message

    def isSelected(self):
        return self.__selected

    def select(self, channel):
        if GPIO.input(self.__gpio) == GPIO.HIGH and self.__selected == False:
            time.sleep(.300) #sleep half a second and make sure that the switch is resting on the correct status
            if GPIO.input(self.__gpio) == GPIO.HIGH and self.__selected == False:
                print("GPIO: " + str(self.__gpio) + " | EMOJI: " + str(self.__emoji) + " | MESSAGE: " + self.__message)
                sendStatus(self)
                self.__selected = True
           
        if GPIO.input(self.__gpio) == GPIO.LOW:
           self.__selected = False

        return
    

    

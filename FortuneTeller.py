import random
import serial
import adafruit_thermal_printer
import RPi.GPIO as GPIO
import time

#Creates the list of fortunes to be chosen from.
fortunes = [
    'Fortune 1',
    'Fortune 2',
    'Fortune 3',
]

GPIO.setmode(GPIO.BOARD) #Use the physical GPIO number
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Change pin if necessary
GPIO.setwarnings(False) #Ignore warnings

def button():	
    while True: # Run forever
        if GPIO.input(18) == GPIO.HIGH:
            time.sleep(1)
            getfortune()

def getfortune():

    #Initiates necessary printer functions
    uart = serial.Serial("/dev/serial0", baudrate=19200, timeout=3000)
    ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.69)
    printer = ThermalPrinter(uart, auto_warm_up=False)
    printer.warm_up()

    #Edit the text below to adjust the receipt design
    printer.feed(2) #Blank line
    printer.underline = adafruit_thermal_printer.UNDERLINE_THIN #Add a thin underline
    printer.justify = adafruit_thermal_printer.JUSTIFY_CENTER #Center the text
    printer.print(' *.. Fortune 2 Go ..* ') #First line of text
    printer.feed(2) #Blank line
    printer.underline = None #Removes underline
    printer.justify = adafruit_thermal_printer.JUSTIFY_LEFT #Left alight text
    printer.print(random.choice(fortunes)) #Second line of text will be a random fortune
    printer.feed(2) #Blank line
    printer.feed(2) #Blank line
    
    print("button was pushed!")

button()
GPIO.cleanup() #GPIO clean up

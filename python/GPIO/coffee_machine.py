#!/usr/bin/env python3
# coding: utf-8
# You should ALWAYS only use one and only one Instance of CoffeeMachine class

import RPi.GPIO as GPIO
from time import sleep
from functools import partial
import spidev

class CoffeeMachine():

    # we should make a conf file to setup pin...
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(32, GPIO.OUT, initial=GPIO.LOW)
        self.standart_time = 0.1

        # Make coffe
        self.pin_single_coffee_button = 7

        # Make rotation volume
        self.pin_right_volume = 29
        self.pin_left_volume = 16

        # Push button intensity
        self.pin_intensity = 11

        self.pin_volume_captor = 18 #?

        self.actuator_pin_list = [self.pin_volume_captor, self.pin_single_coffee_button, self.pin_right_volume, self.pin_left_volume, self.pin_intensity]

        self.volume_captor = 1  # to do: implement class
        self.intensity_captor = 6


        GPIO.setup(self.actuator_pin_list, GPIO.OUT, initial=GPIO.LOW)
        #GPIO.setup(self.captor_pin_list, GPIO.IN)

    def rotate(pin1, pin2, standart_time):
        print("Rotation on pins :",pin1,pin2)
        GPIO.output(pin1, GPIO.HIGH)
        sleep(standart_time * 0.5)
        GPIO.output(pin2, GPIO.HIGH)
        sleep(standart_time * 0.5)
        GPIO.output(pin1, GPIO.LOW)
        sleep(standart_time * 0.5)
        GPIO.output(pin2, GPIO.LOW)

    def push_button(pin, standart_time):
        print("Push on pin :",pin,standart_time)
        GPIO.output(pin, GPIO.HIGH)
        sleep(standart_time* 0.5)
        GPIO.output(pin, GPIO.LOW)

    def make_coffee(self, volume, intensity):
        print("Making Coffee...")
        print("Volume Wanted    :",volume)
        print("Intensity Wanted :",intensity)

        problem_intensity=False
        problem_volume=False

        try:
            self.set_intensity(intensity)
        except Exception as e:
            problem_intensity=True
            print(str(e))

        try:
            self.set_volume(volume)
        except Exception as e:
            problem_volume=True
            print(str(e))

        try:
            CoffeeMachine.push_button(self.pin_single_coffee_button, self.standart_time)
        except Exception as e:
            print(str(e))

        print("Making Coffee Done !")
        if problem_intensity:
            print("But there was a problem reading intensity captor (default Intensity was used)")
        if problem_volume:
            print("But there was a problem reading intensity captor (default Volume was used)")
        return True

    def ReadChannel(channel):
        spi = spidev.SpiDev()
        spi.open(0, 0)
        adc = spi.xfer2([1, (8 + channel) << 4, 0])
        data = ((adc[1] & 3) << 8) + adc[2]
        spi.close()
        return data

    def ConvertVolts(data, places):
        volts = (data * 3.3) / float(1023)
        volts = round(volts, places)
        return volts

    def ConvertTemp(data, places):

        # ADC Value
        # (approx)  Temp  Volts
        #    0      -50    0.00
        #   78      -25    0.25
        #  155        0    0.50
        #  233       25    0.75
        #  310       50    1.00
        #  465      100    1.50
        #  775      200    2.50
        # 1023      280    3.30

        temp = ((data * 330) / float(1023)) - 50
        temp = round(temp, places)
        return temp

    def read_values(self, pin_to_read):
        print("\tReading Values....",pin_to_read)
        channels = list(range(8))
        # Read the light sensor data
        light_levels = [0 for i in range(8)]
        light_volts = [0 for i in range(8)]

        bin = [0 for i in range(8)]

        for i, nb in enumerate(channels):
            light_levels[i] = CoffeeMachine.ReadChannel(nb)
            light_volts[i] = CoffeeMachine.ConvertVolts(light_levels[i],2)
            if light_volts[i] > 2:
                bin[i] = 1
        print("\tValues from Captors :",*bin)
        print("I RETRUN :",bin[pin_to_read-1])

        # Return boolean value of captor that we are looking at.
        return bin[pin_to_read-1]

    def set_intensity(self, intensity):
        print("Setting Intensity",intensity,"...")
        GPIO.output(32, GPIO.HIGH) # relai "selection" -> captor alimentation
        rotation_count=0

        # push_button
        # while we're not detecting any signal, move selector
        while not self.read_values(self.intensity_captor):
            rotation_count+=1
            sleep(0.2)
            CoffeeMachine.push_button(self.pin_intensity, self.standart_time)
            sleep(0.1)
            if rotation_count > 6:
                # We were not able to get detect captor: We don't know where we are
                GPIO.output(32,GPIO.LOW)
                raise ValueError('Volume captor not detected')

        # We are now on pin 3 (but volume =2 because pin1 isn't any volume.)
        print("we are on pin3")
        if intensity<2:
            rotation_to_make = intensity + 4
        else:
            rotation_to_make = intensity - 2
        print(rotation_to_make)
        for i in range(rotation_to_make):
            print("PUSH")
            # move to intensity selector choosen
            sleep(0.2)
            CoffeeMachine.push_button(self.pin_intensity,self.standart_time)

        GPIO.output(32,GPIO.LOW)
        print("Setting Intensity Done")
        return True

    def set_volume(self, volume):
        print("Setting Volume",volume,"...")
        GPIO.output(32, GPIO.HIGH) # relai "selection" -> captor alimentation
        rotation_count=0
        #rotate_button
        # while we're not detecting any signal, move selector
        while not self.read_values(self.volume_captor):
            rotation_count+=1
            sleep(0.3)
            CoffeeMachine.rotate(self.pin_right_volume, self.pin_left_volume, self.standart_time)
            sleep(0.3)
            if rotation_count > 6:
                GPIO.output(32,GPIO.LOW)
                # We were not able to get detect captor: We don't know where we are
                raise ValueError('Volume captor not detected')
        # We are now on pin 3
        if volume==4:
            rotation_to_make = 3
        else:
            if volume==3:
                rotation_to_make = 4
            else:
                if volume==2:
                    rotation_to_make = 0
                else:
                    if volume==1:
                        rotation_to_make = 1
                    else:
                        if volume==0:
                            rotation_to_make = 2

        for i in range(rotation_to_make):
            # move to volume selector choosen
            sleep(0.2)
            CoffeeMachine.rotate(self.pin_right_volume, self.pin_left_volume, self.standart_time)

        GPIO.output(32, GPIO.LOW)
        print("Setting Volume Done !")
        return True

    # You should ALWAYS only use one and only one Instance of this class
    def clear_pin(self):
        print("Cleanup...")
        GPIO.output(self.actuator_pin_list, GPIO.LOW)
        GPIO.cleanup()
        print("Cleanup Done !")

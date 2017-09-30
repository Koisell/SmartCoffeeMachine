#!/usr/bin/python

import spidev
import time
import os

class MCP3008():

    def __init__():
        # Open SPI bus
        spi = spidev.SpiDev()
        spi.open(0, 0)

    # Function to read SPI data from MCP3008 chip
    # Channel must be an integer 0-7
    def ReadChannel(channel):
        adc = spi.xfer2([1, (8 + channel) << 4, 0])
        data = ((adc[1] & 3) << 8) + adc[2]
        return data

    # Function to convert data to voltage level,
    # rounded to specified number of decimal places.


    def ConvertVolts(data, places):
        volts = (data * 3.3) / float(1023)
        volts = round(volts, places)
        return volts

    # Function to calculate temperature from
    # TMP36 data, rounded to specified
    # number of decimal places.


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

    # Define sensor channels
    light_channel = 5
    temp_channel = 6

    # Define delay between readings
    delay = 1

    while True:
        channels = list(range(6))
        # Read the light sensor data
        light_levels = [0 for i in range(6)]
        light_volts = [0 for i in range(6)]
        #light_level = ReadChannel(light_channel)
        #light_volts = ConvertVolts(light_level, 2)
        bin = [0 for i in range(6)]
        # Read the temperature sensor data
        #temp_level = ReadChannel(temp_channel)
        #temp_volts = ConvertVolts(temp_level, 2)
        #temp = ConvertTemp(temp_level, 2)
        for i, nb in enumerate(channels):
            light_levels[i] = ReadChannel(nb)
            light_volts[i] = ConvertVolts(light_levels[i],2)
            if light_volts[i] > 2:
                bin[i] = 1
    # Print out results
    #    print("Light: ({}V)".format(light_volts))
    #    print("Temp : ({}V)".format(temp_volts))
        print(*bin)
        # Wait before repeating loop
        time.sleep(delay)

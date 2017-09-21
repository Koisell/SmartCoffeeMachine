import time
import RPi.GPIO as GPIO


class SRF05():

    def __init__(self, pin_trigger, pin_echo):
        GPIO.setmode(GPIO.BCM)
        self.pin_trigger = pin_trigger
        self.pin_echo = pin_echo
        print ("Ultrasonic Measurement")

        # Set pins as output and input
        GPIO.setup(self.pin_trigger,GPIO.OUT)  # Trigger
        GPIO.setup(self.pin_echo,GPIO.IN)      # Echo

        # return true if there is a cup detetected at a distance < distance_seuil
        # distance seuil is in cm !
    def check_cup_presence(self, distance_seuil):
        # Set trigger to False (Low)
        GPIO.output(self.pin_trigger, False)
        # Allow module to settle
        time.sleep(0.5)


        # Send 10us pulse to trigger
        GPIO.output(self.pin_trigger, True)
        time.sleep(0.00001)
        GPIO.output(self.pin_trigger, False)
        start = time.time()
        while GPIO.input(self.pin_echo)==0:
          pulse_start = time.time()

        pulse_end = time.time()
        while GPIO.input(self.pin_echo)==1:
          pulse_end = time.time()

        # Calculate pulse length
        elapsed = pulse_end - pulse_start

        # Distance pulse travelled in that time is time
        # multiplied by the speed of sound (cm/s)
        distance = elapsed * 34300

        # That was the distance there and back so half the value
        distance = distance / 2

        print ("Distance : ",distance)
        # Reset GPIO settings
        GPIO.cleanup()
        return distance<distance_seuil

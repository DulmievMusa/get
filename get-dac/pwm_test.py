import RPi.GPIO as GPIO 

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_freq, dyn_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.dyn_range = dyn_range
        self.verbose = verbose
        self.pwm_freq = pwm_freq
        GPIO.setup(self.gpio_pin, GPIO.OUT, initial = 0)

        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_freq)

        
        

        self.pwm.start(0)

    def deinit(self):
        # GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()

    def set_vol(self, vol):
        
        #GPIO.output(self.gpio_pin, 1)
        self.pwm.ChangeDutyCycle(vol/self.dyn_range*100)


if __name__ == "__main__":
    try:
        GPIO.setmode(GPIO.BCM)


        

        dac = PWM_DAC(12, 500, 3.29, True)

        while True:
            try:
                vol = float(input("введите напряжение в вольтах: "))
                dac.set_vol(vol)

            except ValueError:
                print("вы ввели не число. трай эгэин\n")

    finally:
        dac.deinit()

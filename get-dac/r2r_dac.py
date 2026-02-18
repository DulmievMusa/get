import RPi.GPIO as GPIO




def decimal2binary(number):
    return [int(bit) for bit in bin(number)[2:].zfill(8)]

def number_to_dac(number):
    GPIO.output(dac_bits, decimal2binary(number))


class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()
    
    def set_number(self, number):
        GPIO.output(dac_bits, decimal2binary(number))

    def set_voltage(self, number):
        if not (0.0 <= voltage <= dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} B)")
            print("Устанавливаем 0.0 В")
            self.set_number(int(voltage / dynamic_range * 255))
        
        self.set_number(int(voltage / dynamic_range * 255))




if __name__ == "__main__":
    dac_bits = [16, 20, 21, 25, 26, 17, 27, 22]
    dynamic_range = 3.3

    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()

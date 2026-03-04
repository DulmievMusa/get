import pwm_dacc as pd
import signal_generator as sg
import time
import numpy

amplitude = 3.15
signal_frequency = 10
sampling_frequency = 1000
k = -1

def func(freq, time):
    value = 2 / numpy.pi * numpy.arcsin(numpy.sin(2*numpy.pi * freq * time))
    value += 1
    value /= 2
    return value

if __name__ == "__main__":
    try:
        amplitude = 3.15
        signal_frequency = 10
        sampling_frequency = 1000
        dac = pd.PWM_DAC(12, 4000, 3.3, True)
        n = 0
        while True:
            voltage = func(signal_frequency, time.time())
            n += 1
            sg.wait_for_samp_per(sampling_frequency)
            dac.set_vol(voltage)
    except ValueError:
        print("Число введено неправильно!")

    finally:
        dac.deinit()
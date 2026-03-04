import r2r_dac as r2r
import signal_generator as sg
import time
import numpy

amplitude = 3.15
signal_frequency = 2
sampling_frequency = 1000
value = 1
k = 1
voltage = 1


def func(freq, time):
    value = 2 / numpy.pi * numpy.arcsin(numpy.sin(2*numpy.pi * freq * time))
    value += 1
    value /= 2
    return value


if __name__ == "__main__":
    try:
        amplitude = 3.15
        signal_frequency = 2
        sampling_frequency = 1000
        dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.15, True)
        n = 0
        while True:
            voltage = func(signal_frequency, time.time())
            n += 1
            sg.wait_for_sampling_period(sampling_frequency)
            dac.set_voltage(voltage)
    except ValueError:
        print("Число введено неправильно!")

    finally:
        dac.deinit()

import numpy as np
import time
import r2r_dac as r2r

def get_sin_wave_amplitude(freq, time):
    return (np.sin(2 * np.pi * freq * time) + 1) / 2

def wait_for_samp_per(sampling_frequency):
    time.sleep(1.0/sampling_frequency)

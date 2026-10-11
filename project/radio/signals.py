"""Basic signal generators."""
import numpy as np


def time_axis(duration, fs):
    """Sample times t_n = n / fs for n = 0, 1, ..., covering `duration` seconds."""
    return np.arange(int(round(duration * fs))) / fs


# Lesson 1
def tone(freq, duration, fs, amplitude=1.0, phase=0.0):
    """Return samples of amplitude * cos(2*pi*freq*t + phase).

    freq      frequency in Hz
    duration  length in seconds
    fs        sample rate in samples per second
    phase     phase in radians

    Returns a NumPy array with round(duration * fs) samples.
    """
    raise NotImplementedError("Lesson 1 exercise")


SPEED_OF_LIGHT = 299_792_458.0  # m/s


# Lesson 2
def wavelength(freq):
    """Wavelength in metres of a radio wave at `freq` Hz: lambda = c / f."""
    raise NotImplementedError("Lesson 2 exercise")


# Lesson 2
def quarter_wave_antenna(freq):
    """Length in metres of a quarter-wave antenna for `freq` Hz."""
    raise NotImplementedError("Lesson 2 exercise")

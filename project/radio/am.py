"""Amplitude modulation."""
import numpy as np


# Lesson 3
def am_modulate(message, fc, fs, mu, carrier_amplitude=1.0):
    """Amplitude-modulate a carrier with `message`.

    message  NumPy array of samples, normalised so that max |message| = 1
    fc       carrier frequency in Hz
    fs       sample rate of `message` in samples per second
    mu       modulation index (depth), e.g. 0.5 for 50%

    Returns s[n] = Ac * (1 + mu * message[n]) * cos(2*pi*fc*t_n).
    """
    raise NotImplementedError("Lesson 3 exercise")


# Lesson 3
def estimate_modulation_index(signal, fc, fs):
    """Estimate mu from an AM signal by measuring its envelope.

    Split the signal into chunks one carrier period long, take the peak of
    |signal| in each chunk as the envelope, then apply
    mu = (E_max - E_min) / (E_max + E_min).
    """
    raise NotImplementedError("Lesson 3 exercise")

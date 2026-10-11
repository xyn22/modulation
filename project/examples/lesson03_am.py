"""Lesson 3: your first AM transmitter.
    python -m examples.lesson03_am
"""
import matplotlib.pyplot as plt

from radio.am import am_modulate, estimate_modulation_index
from radio.audio import save_wav
from radio.signals import time_axis, tone

FS = 48_000
FC = 6_000
MU = 0.7

message = tone(150, 2.0, FS)
s = am_modulate(message, FC, FS, MU)
save_wav("lesson03_am.wav", s, FS)
print("Saved lesson03_am.wav: a 6 kHz carrier whose loudness pulses 150 times a second.")
print(f"Modulation index used: {MU}, estimated from the signal: {estimate_modulation_index(s, FC, FS):.3f}")

n = int(0.02 * FS)
t = time_axis(2.0, FS)[:n] * 1000
plt.plot(t, s[:n], label="AM signal", linewidth=0.8)
plt.plot(t, 1 + MU * message[:n], "r--", label="Envelope 1 + mu*m(t)")
plt.plot(t, -(1 + MU * message[:n]), "r--")
plt.title(f"AM signal: fc = {FC} Hz, message 150 Hz, mu = {MU}")
plt.xlabel("Time (ms)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()

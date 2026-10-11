"""Lesson 1: hear and see a pure tone. Run from the project folder:
    python -m examples.lesson01_tone
"""
import matplotlib.pyplot as plt

from radio.audio import save_wav
from radio.signals import time_axis, tone

FS = 48_000

x = tone(440, 2.0, FS, amplitude=0.5)
save_wav("lesson01_440Hz.wav", x, FS)
print("Saved lesson01_440Hz.wav: play it, this is the note A (440 Hz).")

n = int(0.01 * FS)
t = time_axis(2.0, FS)[:n]
plt.plot(t * 1000, x[:n], marker=".", markersize=3)
plt.title("440 Hz tone: first 10 ms (each dot is one sample)")
plt.xlabel("Time (ms)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

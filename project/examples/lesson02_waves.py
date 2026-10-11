"""Lesson 2: a slow message and a fast carrier, and why carriers must be fast.
    python -m examples.lesson02_waves
"""
import matplotlib.pyplot as plt

from radio.audio import save_wav
from radio.signals import quarter_wave_antenna, time_axis, tone

FS = 48_000

for name, f in [("Voice (1 kHz)", 1e3), ("AM radio (1 MHz)", 1e6),
                ("FM radio (100 MHz)", 100e6), ("Wi-Fi (2.4 GHz)", 2.4e9)]:
    print(f"{name:20s} quarter-wave antenna: {quarter_wave_antenna(f):12.3f} m")

message = tone(300, 2.0, FS, amplitude=0.5)
carrier = tone(6000, 2.0, FS, amplitude=0.5)
save_wav("lesson02_message.wav", message, FS)
save_wav("lesson02_carrier.wav", carrier, FS)
print("Saved lesson02_message.wav (300 Hz, low) and lesson02_carrier.wav (6 kHz, high).")

n = int(0.01 * FS)
t = time_axis(2.0, FS)[:n] * 1000
fig, (a, b) = plt.subplots(2, 1, sharex=True)
a.plot(t, message[:n]); a.set_title("Message, 300 Hz"); a.set_ylabel("Amplitude")
b.plot(t, carrier[:n], color="orange"); b.set_title("Carrier, 6 kHz"); b.set_ylabel("Amplitude")
b.set_xlabel("Time (ms)")
plt.tight_layout()
plt.show()

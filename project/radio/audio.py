"""Audio helpers. Provided for you: not an exercise."""
import wave

import numpy as np


def save_wav(path, signal, fs):
    """Write a signal in the range [-1, 1] to a 16-bit mono WAV file.

    Louder signals are scaled down to fit, so nothing clips.
    """
    signal = np.asarray(signal, dtype=float)
    peak = np.max(np.abs(signal))
    if peak > 1:
        signal = signal / peak
    pcm = (signal * 32767).astype(np.int16)
    with wave.open(str(path), "wb") as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(int(fs))
        f.writeframes(pcm.tobytes())

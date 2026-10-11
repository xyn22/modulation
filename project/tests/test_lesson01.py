import numpy as np

from radio.signals import time_axis, tone

FS = 48_000


def test_length():
    assert len(tone(440, 0.5, FS)) == 24_000


def test_starts_at_peak_with_zero_phase():
    assert np.isclose(tone(440, 0.01, FS)[0], 1.0)


def test_amplitude():
    x = tone(100, 0.1, FS, amplitude=0.3)
    assert np.isclose(np.max(np.abs(x)), 0.3, atol=1e-3)


def test_frequency_by_counting_zero_crossings():
    # A sinusoid at f Hz crosses zero 2f times per second.
    x = tone(250, 1.0, FS, phase=0.1)
    crossings = np.count_nonzero(np.diff(np.sign(x)) != 0)
    assert crossings == 500


def test_phase_shift_turns_cos_into_sin():
    # cos(theta - pi/2) = sin(theta)
    t = time_axis(0.01, FS)
    expected = np.sin(2 * np.pi * 300 * t)
    assert np.allclose(tone(300, 0.01, FS, phase=-np.pi / 2), expected)

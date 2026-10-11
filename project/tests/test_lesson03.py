import numpy as np
import pytest

from radio.am import am_modulate, estimate_modulation_index
from radio.signals import time_axis

FS = 48_000
FC = 8_000
FM = 200


def message(duration=0.1):
    return np.cos(2 * np.pi * FM * time_axis(duration, FS))


def test_matches_formula():
    m = message()
    t = time_axis(0.1, FS)
    expected = 2.0 * (1 + 0.5 * m) * np.cos(2 * np.pi * FC * t)
    assert np.allclose(am_modulate(m, FC, FS, 0.5, carrier_amplitude=2.0), expected)


def test_zero_depth_is_plain_carrier():
    t = time_axis(0.1, FS)
    assert np.allclose(am_modulate(message(), FC, FS, 0.0), np.cos(2 * np.pi * FC * t))


def test_envelope_limits():
    s = am_modulate(message(), FC, FS, 0.5)
    assert np.isclose(np.max(s), 1.5, atol=0.01)


@pytest.mark.parametrize("mu", [0.2, 0.5, 0.8, 1.0])
def test_estimate_modulation_index(mu):
    s = am_modulate(message(), FC, FS, mu)
    assert np.isclose(estimate_modulation_index(s, FC, FS), mu, atol=0.02)

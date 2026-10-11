import numpy as np

from radio.signals import quarter_wave_antenna, wavelength


def test_wavelength_of_am_broadcast():
    assert np.isclose(wavelength(1e6), 299.79, atol=0.01)


def test_wavelength_of_voice_frequency():
    assert np.isclose(wavelength(1e3), 299_792.458)


def test_quarter_wave_antenna_for_fm_radio():
    assert np.isclose(quarter_wave_antenna(100e6), 0.7495, atol=1e-4)


def test_works_on_arrays():
    freqs = np.array([1e6, 100e6])
    assert np.allclose(quarter_wave_antenna(freqs), wavelength(freqs) / 4)

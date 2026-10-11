# Project: a software AM radio

Over the lessons you build a complete AM radio in Python, one function at a time:
a transmitter that puts audio onto carriers, several "stations" sharing one signal,
noise, and finally a receiver that tunes to one station and plays its audio back.
Everything runs at audio sample rates, so you can listen to every stage.
A later extension turns it into an acoustic modem that sends text between two
devices through a speaker and a microphone.

## Setup

From this `project` folder:

```bash
python -m venv .venv
# Windows:  .venv\Scripts\activate      macOS/Linux:  source .venv/bin/activate
pip install -r requirements.txt
```

## How each lesson works

1. Read the **Code** section at the end of the lesson page.
2. Implement the functions marked with that lesson in `radio/` (they currently raise `NotImplementedError`).
3. Check your work: `pytest tests/test_lesson01.py` (or `pytest` for everything).
4. Run the lesson's example to hear and see the result: `python -m examples.lesson01_tone`.
5. Stuck? Each lesson page has a hidden reference solution.

## Milestones

| Lesson | You implement | Result |
| --- | --- | --- |
| 1 | `signals.tone` | Generate and play a pure tone |
| 2 | `signals.wavelength`, `signals.quarter_wave_antenna` | Why carriers must be fast, in numbers |
| 3 | `am.am_modulate`, `am.estimate_modulation_index` | Your first AM transmitter |
| ... | demodulation, filters, FFT, tuning | A working receiver |

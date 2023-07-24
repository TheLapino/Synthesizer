import numpy as np
from math import pi

from src.oscillators.BaseOscillator import BaseOscillator
from src.visualiser.visualiser import visualiseSignal

class SawtoothWaveOscillator(BaseOscillator):

    def generateSound(self, duration):
        numberSamples = int(self.sampleRate * duration)
        t = np.linspace(0, duration, numberSamples, endpoint=False)

        period = self.sampleRate / self.freq
        phase = (t * self.freq) % 1
        wave = 2 * phase - 1



        release_duration = 0.2  # Duration of the release phase in seconds
        release_samples = int(release_duration * self.sampleRate)

        decay = np.exp(-np.linspace(0, 5, release_samples))
        wave[-release_samples:] *= decay
        return wave

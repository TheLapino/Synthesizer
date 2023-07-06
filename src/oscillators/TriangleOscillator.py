import numpy as np
from math import pi

from .BaseOscillator import BaseOscillator


class TriangleWaveOscillator(BaseOscillator):

    def generateSound(self, duration):
        numberSamples = int(self.sampleRate * duration)
        t = np.linspace(0, duration, numberSamples, endpoint=False)
        phase = t * self.freq
        wave = 2 * np.abs(2 * (t * self.freq - np.floor(t * self.freq + 0.5))) - 1

        release_duration = 0.2  # Duration of the release phase in seconds
        release_samples = int(release_duration * self.sampleRate)

        decay = np.exp(-np.linspace(0, 5, release_samples))
        wave[-release_samples:] *= decay
        return wave

import numpy as np
from math import pi

from .BaseOscillator import BaseOscillator


class TriangleWaveOscillator(BaseOscillator):

    def generateSound(self, duration):
        numberSamples = int(self.sampleRate * duration)
        t = np.linspace(0, duration, numberSamples, endpoint=False)
        phase = t * self.freq
        wave = 2 * np.abs(2 * (t * self.freq - np.floor(t * self.freq + 0.5))) - 1

        return wave

import numpy as np
from math import pi

from .BaseOscillator import BaseOscillator


class SquareWaveOscillator(BaseOscillator):

    def generateSound(self, duration):
        numberSamples = int(self.sampleRate * duration)
        t = np.linspace(0, duration, numberSamples, endpoint=False)
        wave = self.amp * np.sign(np.sin(2*pi*t*self.freq + self.phase))
        return wave

    def generateSoundRealTime(self):
        t = 0.0
        while True:
            sample = self.amp * np.sign(np.sin(2*pi*t*self.freq + self.phase))
            t += 1.0 / self.sampleRate
            yield sample

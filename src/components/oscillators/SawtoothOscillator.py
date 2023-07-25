import numpy as np
from math import pi

from .BaseOscillator import BaseOscillator


class SawtoothWaveOscillator(BaseOscillator):

    def generateSound(self, duration):
        numberSamples = int(self.sampleRate * duration)
        t = np.linspace(0, duration, numberSamples, endpoint=False)

        period = self.sampleRate / self.freq
        phase = (t * self.freq) % 1
        wave = 2 * phase - 1
        return wave
    
    def generateSoundRealTime(self):
        t = 0.0
        while True:
            phase = (t * self.freq) % 1
            sample = 2 * phase - 1
            t += 1.0 / self.sampleRate
            yield sample
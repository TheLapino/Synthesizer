import numpy as np
from math import pi

from src.components.oscillators.BaseOscillator import BaseOscillator


class TriangleWaveOscillator(BaseOscillator):

    def generateSound(self, duration):
        numberSamples = int(self.sampleRate * duration)
        t = np.linspace(0, duration, numberSamples, endpoint=False)
        phase = t * self.freq
        wave = 2 * np.abs(2 * (phase - np.floor(phase + 0.5))) - 1
        return wave

    def generateSoundRealTime(self):
        t = 0.0
        while True:
            phase = t * self.freq
            sample = 2 * np.abs(2 * (phase - np.floor(phase + 0.5))) - 1
            t += 1.0 / self.sampleRate
            yield sample


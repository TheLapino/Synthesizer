import numpy as np
from math import pi

from src.components.oscillators.IOscillator import IOscillator


class SinWaveOscillator(IOscillator):

    def generateSound(self, duration):
        numberSamples = int(self.sampleRate * duration)
        t = np.linspace(0, duration, numberSamples, endpoint=False)
        wave = self.amp * np.sin(2*pi*t*self.freq + self.phase)
        return wave


    def generateSoundRealTime(self):
        t = 0.0
        while True:
            sample = self.amp * np.sin(2*pi*t*self.freq + self.phase)
            sample *= self.volume
            t += 1.0 / self.sampleRate
            yield sample * self.volume
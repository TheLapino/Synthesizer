import numpy as np
from math import pi

from src.components.oscillators.IOscillator import IOscillator


class SinWaveOscillator(IOscillator):

    def generateSound(self, duration):
        numberSamples = int(self.sampleRate * duration)
        t = np.linspace(0, duration, numberSamples, endpoint=False)
        wave = self.amp * np.sin(2*pi*t*self.freq + self.phase)
        return wave

    def _getValue(self):
        sample = self.amp * np.sin(2*pi*self.t*self.freq + self.phase)
        return sample
    


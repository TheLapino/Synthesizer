import numpy as np
from math import pi

from src.components.oscillators.BaseOscillator import BaseOscillator


class SinWaveOscillator(BaseOscillator):

    def generateSound(self, duration):
        numberSamples = int(self.sampleRate * duration)
        t = np.linspace(0, duration, numberSamples, endpoint=False)
        wave = self.amp * np.sin(2*pi*t*self.freq + self.phase)
        return wave

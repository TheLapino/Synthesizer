import numpy as np
from .BaseOscillator import BaseOscillator
from math import pi
import matplotlib.pylab as plt

class SinWaveOscillator(BaseOscillator):

    def generateSound(self, duration):
        numberSamples = int(self.sampleRate * duration)
        step = duration / numberSamples
        t = np.linspace(0, duration, numberSamples)
        wave = self.amp * np.sin(2*pi*t*self.freq + self.phase)
        return wave

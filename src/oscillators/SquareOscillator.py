import numpy as np
from .BaseOscillator import BaseOscillator
from math import pi
import sys
sys.path.append('../src/visualiser')

from visualiser import visualiseSignal

class SquareWaveOscillator(BaseOscillator):

    def generateSound(self, duration):
        numberSamples = int(self.sampleRate * duration)
        t = np.linspace(0, duration, numberSamples, endpoint=False)
        wave = self.amp * np.sign(np.sin(2*pi*t*self.freq + self.phase))

        release_duration = 0.2  # Duration of the release phase in seconds
        release_samples = int(release_duration * self.sampleRate)

        decay = np.exp(-np.linspace(0, 5, release_samples))
        wave[-release_samples:] *= decay
        visualiseSignal(t, wave)
        return wave

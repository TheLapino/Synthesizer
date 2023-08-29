import numpy as np

from src.components.oscillators.IOscillator import IOscillator


class TriangleWaveOscillator(IOscillator):

    def generateSound(self, duration):
        numberSamples = int(self.sampleRate * duration)
        t = np.linspace(0, duration, numberSamples, endpoint=False)
        phase = t * self.freq
        wave = 2 * np.abs(2 * (phase - np.floor(phase + 0.5))) - 1
        return wave
    
    def _getValue(self):
        phase = self.t * self.freq
        sample = 2 * np.abs(2 * (phase - np.floor(phase + 0.5))) - 1
        return sample




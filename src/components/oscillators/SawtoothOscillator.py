import numpy as np

from src.components.oscillators.IOscillator import IOscillator


class SawtoothWaveOscillator(IOscillator):

    def generateSound(self, duration):
        numberSamples = int(self.sampleRate * duration)
        t = np.linspace(0, duration, numberSamples, endpoint=False)

        period = self.sampleRate / self.freq
        phase = (t * self.freq) % 1
        wave = 2 * phase - 1
        return wave
    

    def _getValue(self):
        phase = (self.t * self.freq) % 1
        sample = 2 * phase - 1
        return sample
    
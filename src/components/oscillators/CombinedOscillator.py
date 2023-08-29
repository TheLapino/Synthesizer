import numpy as np
from math import ceil

from src.components.oscillators.IOscillator import IOscillator


class CombinedOscillator(IOscillator):

    def __init__(self, oscillators: [IOscillator], sampleRate = 44100):
        self.oscillators = oscillators
        self.sampleRate = sampleRate
        self.maxValueCoeff = self.__getMaxValueCoeff()
        self.oscGenerators = [osc.generateSoundRealTime() for osc in self.oscillators]
        

    def generateSound(self, duration):
        noSamples = duration * self.sampleRate

        samples = np.zeros(noSamples)
        for osc in self.oscillators:
            samples += osc.generateSound(duration)
        
        return samples[1:]

    def generateSoundRealTime(self):
        while True:
            sample = 0
            for oscGenerator in self.oscGenerators:
                sample += next(oscGenerator)
            sample /= self.maxValueCoeff
            yield sample


    def freqSetter(self, freq):
        for osc in self.oscillators:
            osc.freqSetter(freq)

    def __getMaxValueCoeff(self):
        maxPeriod = self.__getMaxPeriod()

        samples = self.generateSound(maxPeriod)

        maxValueCoeff = np.max(np.abs(samples))
        return maxValueCoeff


    def __getMaxPeriod(self):
        allFreqs = np.array([osc.freqGetter() for osc in self.oscillators])
        minFreq = np.min(allFreqs)
        return int(ceil(1 / minFreq))
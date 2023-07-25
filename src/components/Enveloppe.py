import numpy as np


class EnveloppeADSR:
    def __init__(self, attackTime=0.1, decayTime=0.05, releaseTime=0.1, sustainAmp=0.7, sampleRate=44100):
        self.attackTime = attackTime
        self.decayTime = decayTime
        self.releaseTime = releaseTime
        self.sustainAmp = sustainAmp
        self.sampleRate = sampleRate

        self.attackSteps = int(self.attackTime * self.sampleRate)
        self.decaySteps = int(self.decayTime * self.sampleRate)
        self.releaseSteps = int(self.releaseTime * self.sampleRate)

    def apply(self, signal) -> np.array:


        attack = np.linspace(0, 1, self.attackSteps)
        decay = np.linspace(1, self.sustainAmp, self.decaySteps)
        release = np.linspace(self.sustainAmp, 0, self.releaseSteps)

        signal[:self.attackSteps] *= attack
        signal[self.attackSteps:self.attackSteps+self.decaySteps] *= decay
        signal[self.attackSteps+self.decaySteps:-self.releaseSteps] *= self.sustainAmp
        signal[-self.releaseSteps:] *= release


        return signal

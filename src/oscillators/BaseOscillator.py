import numpy as np


class BaseOscillator:
    def __init__(self, freq, amp=1, phase=0, sampleRate=44100):
        self.freq = freq
        self.amp = amp
        self.phase = phase
        self.sampleRate = sampleRate

    
    def generateSound(self, duration=0.5):
        pass
        

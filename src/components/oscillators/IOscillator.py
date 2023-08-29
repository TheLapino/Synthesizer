import numpy as np


class IOscillator:
    def __init__(self, freq=1, amp=1, phase=0, octaveShift=0, volume=1.0, sampleRate=44100):
        self.freq = freq * (2**octaveShift)
        self.amp = amp
        self.phase = phase
        self.octaveShift = octaveShift
        self.volume = volume
        self.sampleRate = sampleRate
        self.t = 0.0

    
    def generateSound(self, duration=0.5):
        pass


    def generateSoundRealTime(self):
        while True:
            sampleValue = self._getValue() * self.volume
            self.t += 1.0 / self.sampleRate
            yield sampleValue 

    def _getValue(self):
        return 0.0

    def freqSetter(self, freq):
        self.freq = freq * (2**self.octaveShift)

    def freqGetter(self):
        return self.freq
    
    def volumeGetter(self):
        return self.volume
        

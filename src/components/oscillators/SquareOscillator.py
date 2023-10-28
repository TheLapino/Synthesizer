import numpy as np
from math import pi
from scipy.signal import butter, lfilter

from src.components.oscillators.IOscillator import IOscillator



class SquareWaveOscillator(IOscillator):

    def __init__(self, freq=1, amp=1, phase=0, octaveShift=0, volume=1.0, sampleRate=44100):
        super().__init__(freq=1, amp=1, phase=0, octaveShift=0, volume=1.0, sampleRate=44100)
        self.signalFullPeriod = self.generateSoundFullPeriod()
        self.full_period_index = len(self.signalFullPeriod)

    def generateSound(self, duration):
        numberSamples = int(self.sampleRate * duration)
        t = np.linspace(0, duration, numberSamples, endpoint=False)
        wave = self.amp * np.sign(np.sin(2*pi*t*self.freq + self.phase))
        return wave
    
    def _getValue(self):
        sample = self.amp * np.sign(np.sin(2*pi*self.t*self.freq + self.phase))
        return sample
    
    def generateSoundRealTime(self):
        t = 0
        while True:
            sampleValue = self.signalFullPeriod[t % self.full_period_index]# * self.volume
            t += 1
            yield sampleValue 

    
    def freqSetter(self, freq):
        super().freqSetter(freq)
        self.signalFullPeriod = self.generateSoundFullPeriod()
        self.full_period_index = len(self.signalFullPeriod)

    
    def _getValueWithTime(self, time):
        sample = self.amp * np.sign(np.sin(2*pi*time*self.freq + self.phase))
        return sample


    def generateSoundFullPeriod(self):
        period = 1 / self.freq
        two_period = 2 * period
        sampling_rate_for_freq = int(self.sampleRate * two_period)
        t = np.linspace(0, two_period, sampling_rate_for_freq)
        samples = np.array([self._getValueWithTime(time) for time in t])

        CUTOFF = 1500

        samples_cutoff = butter_lowpass_filter(samples, CUTOFF, 44100, 2)

        start_index = len(samples) // 4
        end_index = 3 * len(samples) // 4

        samples_cutoff = samples_cutoff[start_index:end_index]

        min_val = np.min(samples_cutoff)
        max_val = np.max(samples_cutoff)
        samples_cutoff = 2 * (samples_cutoff - min_val) / (max_val - min_val) - 1

        return samples_cutoff



def butter_lowpass(cutoff, fs, order=1):
    return butter(order, cutoff, fs=fs, btype='low', analog=False)

def butter_lowpass_filter(data, cutoff, fs, order=1):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y
import pyaudio
import numpy as np
from components.NotesController import NotesController

class SynthController:
    def __init__(self, oscillator, bufferSize= 32):
        self.oscillator = oscillator
        self.bufferSize = bufferSize
        self.NotesController = NotesController()
        self.oscillator
        self.OscGenerator = self.oscillator.generateSoundRealTime()

        p = pyaudio.PyAudio()
        self.stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=True, frames_per_buffer=self.bufferSize)


    def getSamples(self, generator, buffer_size):
        samples = [next(generator) for _ in range(buffer_size)]
        return np.array(samples)


    def playSound(self, generator):
        samples = self.getSamples(generator, self.bufferSize)
        self.stream.write(samples.astype(np.float32).tobytes())


    def play(self):
        while True:
            freq = self.NotesController.poll()
            self.oscillator.freqSetter(freq)
            self.playSound(self.OscGenerator)
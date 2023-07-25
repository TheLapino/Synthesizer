import pyaudio
import numpy as np

from NotesController import NotesController

class SynthController:
    def __init__(self, oscillator, bufferSize= 16):
        self.oscillator = oscillator
        self.bufferSize = bufferSize
        self.NotesController = NotesController()

        p = pyaudio.PyAudio()
        self.stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=True, frames_per_buffer=self.bufferSize)


    def get_samples(self, generator, buffer_size):
        samples = [next(generator) for _ in range(buffer_size)]
        return np.array(samples)


    def play_sound(self, generator):
        samples = self.get_samples(generator, self.bufferSize)
        self.stream.write(samples.astype(np.float32).tobytes())


    def play():
        pass
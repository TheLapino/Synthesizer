import pyaudio

from NotesController import NotesController

class SynthController:
    def __init__(self, oscillator, bufferSize= 16):
        self.oscillator = oscillator
        self.bufferSize = bufferSize

        p = pyaudio.PyAudio()
        self.stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=True, frames_per_buffer=self.bufferSize)


    def play():
        pass
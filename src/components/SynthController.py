import pyaudio
import numpy as np

from components.NotesController import NotesController
from components.Enveloppe import EnveloppeADSR

class SynthController:
    def __init__(self, oscillator, enveloppeADSR: EnveloppeADSR, bufferSize = 32, root="C", octave=4):
        self.oscillator = oscillator
        self.enveloppeADSR = enveloppeADSR
        self.bufferSize = bufferSize
        self.NotesController = NotesController(root, octave)
        self.OscGenerator = self.oscillator.generateSoundRealTime()
        self.EnveloppeGenerator = self.enveloppeADSR.generateEnveloppeAmps()

        p = pyaudio.PyAudio()
        self.stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=True, frames_per_buffer=self.bufferSize)


    def getSamples(self):
        samples = [next(self.OscGenerator) for _ in range(self.bufferSize)]
        
        return np.array(samples)
    
    def getSamplesEnveloppeAmp(self):
        amps = [next(self.EnveloppeGenerator) for _ in range(self.bufferSize)]
        return np.array(amps)

    def playSound(self):
        samples = 1 * self.getSamples()
        amps = self.getSamplesEnveloppeAmp()
        samples *= amps
        self.stream.write(samples.astype(np.float32).tobytes())


    def play(self):
        lastFreq = 0
        while True:

            freq, note = self.NotesController.poll()

            if lastFreq != freq and freq != 0:
                self.enveloppeADSR.resetEnveloppe()
                self.enveloppeADSR.noteIsPressed()
                self.oscillator.freqSetter(freq)
                print(f"{note}: {freq}")

            if lastFreq != freq and freq == 0:
                self.enveloppeADSR.noteIsNotPressed()
                if self.enveloppeADSR.releaseEnded():
                    self.oscillator.freqSetter(freq)

            
            self.playSound()
            lastFreq = freq
import pyaudio
import numpy as np
import matplotlib.pyplot as plt

from src.components.notes.NotesController import NotesController
from src.components.notes.Note import Note
from src.components.modifiers.Enveloppe import EnveloppeADSR
from src.components.oscillators.IOscillator import IOscillator
class SynthController:
    def __init__(self, oscillator: IOscillator, enveloppeADSR: EnveloppeADSR, bufferSize=32, root="C", octave=4):
        self.oscillator = oscillator
        self.enveloppeADSR = enveloppeADSR
        self.bufferSize = bufferSize
        self.NotesController = NotesController(root, octave)
        self.OscGenerator = self.oscillator.generateSoundRealTime()
        self.EnveloppeGenerator = self.enveloppeADSR.generateEnveloppeAmps()

        self.signal = np.empty(1)

        p = pyaudio.PyAudio()
        self.stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=True, frames_per_buffer=self.bufferSize)


    def getSamples(self):
        samples = [next(self.OscGenerator) for _ in range(self.bufferSize)]
        return np.array(samples)
    
    def getSamplesEnveloppeAmp(self):
        amps = [next(self.EnveloppeGenerator) for _ in range(self.bufferSize)]
        return np.array(amps)


    def playSound(self):
        samples = self.getSamples()
        amps = self.getSamplesEnveloppeAmp()
        samples *= amps
        self.signal = np.append(self.signal, samples)
        self.stream.write(samples.astype(np.float32).tobytes())


    def play(self):
        lastFreq = 0
        while True:

            #freq, note = self.NotesController.poll()

            note = self.NotesController.poll()
            
            if note.getFreq() == -1:
                break

            if lastFreq != note.getFreq() and note.getFreq() != 0:
                self.enveloppeADSR.resetEnveloppe()
                self.enveloppeADSR.noteIsPressed()
                self.oscillator.freqSetter(note.getFreq())
                print(f"{note.getName()}: {note.getFreq()}")

            if lastFreq != note.getFreq() and note.getFreq() == 0:
                self.enveloppeADSR.noteIsNotPressed()
                if self.enveloppeADSR.releaseEnded():
                    self.oscillator.freqSetter(note.getFreq())

            
            self.playSound()
            lastFreq = note.getFreq()
        self.showSignal()
        

    def showSignal(self):

        t = [i for i in range(self.signal.size)]
        plt.plot(t, self.signal)
        plt.show()


from components.oscillators.SineOscillator import SinWaveOscillator
from components.oscillators.SquareOscillator import SquareWaveOscillator
from components.oscillators.TriangleOscillator import TriangleWaveOscillator
from components.oscillators.SawtoothOscillator import SawtoothWaveOscillator
from components.Enveloppe import EnveloppeADSR
from visualiser.visualiser import visualiseSignal
from components.NotesController import NotesController
from components.notes.NotesFrequenciesMapper import NotesFrequenciesMapper
from components.SynthController import SynthController
from components.notes.NotesOctaveMapper import NotesOctaveMapper

import wave
import struct
import numpy as np
import sounddevice as sd
import keyboard
import pyaudio



SAMPLE_RATE = 44100
DURATION = 2
BUFFER_SIZE = 32

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=True, frames_per_buffer=BUFFER_SIZE)


def main():

    oscillator = SquareWaveOscillator(261.63)

    enveloppe = EnveloppeADSR(attackTime=0.001, decayTime=0.005, releaseTime=0.2, sustainAmp=0.8)
    
    synthctrl = SynthController(oscillator,enveloppe, root="C", octave=3)

    print("--------------------Now playing--------------------")
    synthctrl.play()



if __name__ == "__main__":
    main()

from src.components.oscillators.SineOscillator import SinWaveOscillator
from src.components.oscillators.SquareOscillator import SquareWaveOscillator
from src.components.oscillators.TriangleOscillator import TriangleWaveOscillator
from src.components.oscillators.SawtoothOscillator import SawtoothWaveOscillator
from src.components.Enveloppe import EnveloppeADSR
from src.components.NotesController import NotesController
from src.components.notes.NotesFrequenciesMapper import NotesFrequenciesMapper
from src.components.SynthController import SynthController
from src.components.notes.NotesOctaveMapper import NotesOctaveMapper

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

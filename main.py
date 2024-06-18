from src.components.oscillators.SineOscillator import SinWaveOscillator
from src.components.oscillators.SquareOscillator import SquareWaveOscillator
from src.components.oscillators.TriangleOscillator import TriangleWaveOscillator
from src.components.oscillators.SawtoothOscillator import SawtoothWaveOscillator
from src.components.oscillators.CombinedOscillator import CombinedOscillator
from src.components.modifiers.Enveloppe import EnveloppeADSR
from src.components.SynthController import SynthController
from src.visualiser.visualiser import visualiseSignal


import numpy as np


SAMPLE_RATE = 44100
DURATION = 4
BUFFER_SIZE = 64

def main():

    oscillator1 = SawtoothWaveOscillator(octaveShift=0, volume=0.2)
    oscillator2 = TriangleWaveOscillator(octaveShift=0, volume=0.8)
    oscillator3 = SquareWaveOscillator(octaveShift=0, volume=0.5)
    oscillator4 = SinWaveOscillator(octaveShift=-1, volume=1)
    oscillator5 = SawtoothWaveOscillator(octaveShift=-2, volume=0.6)

    cOscillator = CombinedOscillator( [oscillator1])

    enveloppe = EnveloppeADSR(attackTime=0.001, decayTime=0.2, releaseTime=0.5, sustainAmp=0.8)

    synthctrl = SynthController(cOscillator, enveloppe, root="C", octave=3, bufferSize=BUFFER_SIZE)


    print("--------------------Now playing--------------------")
    synthctrl.play()


def test():
    oscillator3 = SquareWaveOscillator(octaveShift=0, volume=0.5)
    enveloppe = EnveloppeADSR(attackTime=0.1, decayTime=0.2, releaseTime=5., sustainAmp=0.8)

    synthctrl = SynthController(oscillator3, enveloppe, root="C", octave=3, bufferSize=BUFFER_SIZE)

    print("--------------------Now playing--------------------")
    synthctrl.play()


def visualise(signal):
    t = np.linspace(0, DURATION, int(SAMPLE_RATE * DURATION), endpoint=False)
    visualiseSignal(t, signal)

def generateSample(oscGen):
    signal = [next(oscGen) for _ in range(DURATION * SAMPLE_RATE)]
    return signal



if __name__ == "__main__":
    main()
    #test()

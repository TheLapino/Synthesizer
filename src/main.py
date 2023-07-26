import wave
import struct
import numpy as np
import sounddevice as sd

from src.components.oscillators.SineOscillator import SinWaveOscillator
from src.components.oscillators.SquareOscillator import SquareWaveOscillator
from src.components.oscillators.TriangleOscillator import TriangleWaveOscillator
from src.components.oscillators.SawtoothOscillator import SawtoothWaveOscillator
from src.components.Enveloppe import EnveloppeADSR
from src.visualiser.visualiser import visualiseSignal


SAMPLE_RATE = 44100
DURATION = 2

def main():

    oscillator = SquareWaveOscillator(261.63)
    enveloppe = EnveloppeADSR()


    signal = enveloppe.apply(oscillator.generateSound(2))


    visualise(signal)

    sd.play(signal, SAMPLE_RATE)
    sd.wait()



def visualise(signal):
    t = np.linspace(0, 2, int(SAMPLE_RATE * DURATION), endpoint=False)
    visualiseSignal(t, signal)

def normalizeSignal(signal):
    max_amplitude = max(abs(signal))
    signal = signal / max_amplitude
    return signal

def saveWaveFile(signal):
    wav_file=wave.open("test_audio.wav","w")

    nchannels = 1
    sampwidth = 2
    nframes = len(signal)
    comptype = "NONE"
    compname = "not compressed"
    wav_file.setparams((nchannels, sampwidth, SAMPLE_RATE, nframes, comptype, compname))

    for sample in signal:
        wav_file.writeframes(struct.pack('h', int( sample * 32767.0 )))

    wav_file.close()


if __name__ == "__main__":
    main()
    print("Done!")

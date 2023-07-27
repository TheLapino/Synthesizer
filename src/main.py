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

    oscillator = SawtoothWaveOscillator(261.63)

    synthctrl = SynthController(oscillator, root="C", octave=3)

    synthctrl.play()



def get_samples(generator, buffer_size=BUFFER_SIZE):
    samples = [next(generator) for _ in range(buffer_size)]
    return np.array(samples)


def play_sound(generator):
    samples = get_samples(generator)
    stream.write(samples.astype(np.float32).tobytes())


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


def sayHi(key):
    print(key)


if __name__ == "__main__":
    main()

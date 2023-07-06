from components.oscillators.SineOscillator import SinWaveOscillator
from components.oscillators.SquareOscillator import SquareWaveOscillator
from components.oscillators.TriangleOscillator import TriangleWaveOscillator
from components.oscillators.SawtoothOscillator import SawtoothWaveOscillator
from components.Enveloppe import EnveloppeADSR
from visualiser.visualiser import visualiseSignal
import wave
import struct
import numpy as np
import sounddevice as sd

sample_rate = 44100
duration = 2
def main():

    oscillator = SquareWaveOscillator(261.63)
    oscillatorC = SinWaveOscillator(261.63)
    oscillatorCC = TriangleWaveOscillator(261.63)
    oscillatorE = TriangleWaveOscillator(329.63)
    oscillatorG = TriangleWaveOscillator(392.00)

    enveloppe = EnveloppeADSR()

    wave_val = enveloppe.apply(oscillator.generateSound(duration) + oscillatorC.generateSound(duration) + oscillatorCC.generateSound(duration))
    #wave_valE = enveloppe.apply(oscillatorE.generateSound(duration))
    #wave_valG = enveloppe.apply(oscillatorG.generateSound(duration))

    #wave_val = wave_valC + 0.8*wave_valE + 0.8*wave_valG

    max_amplitude = max(abs(wave_val))
    wave_val = wave_val / max_amplitude

    #wave_val = np.append(wave_valC, [wave_valE, wave_valG])

    #visualise(wave_val)


    sd.play(wave_val, sample_rate)
    sd.wait()


def visualise(signal):
    t = np.linspace(0, 2, int(sample_rate * duration), endpoint=False)
    visualiseSignal(t, signal)


def save_wave_file(signal):
    wav_file=wave.open("test_audio.wav","w")

    nchannels = 1
    sampwidth = 2
    nframes = len(signal)
    comptype = "NONE"
    compname = "not compressed"
    wav_file.setparams((nchannels, sampwidth, sample_rate, nframes, comptype, compname))

    for sample in signal:
        wav_file.writeframes(struct.pack('h', int( sample * 32767.0 )))

    wav_file.close()



if __name__ == "__main__":
    main()
from oscillators.SineOscillator import SinWaveOscillator
from oscillators.SquareOscillator import SquareWaveOscillator
from oscillators.TriangleOscillator import TriangleWaveOscillator
import wave
import struct
import numpy as np

sample_rate = 44100
def main():

    #oscillator = SquareWaveOscillator(2)
    oscillator = TriangleWaveOscillator(220)

    wave_val = oscillator.generateSound(2)

    max_amplitude = max(abs(wave_val))

    wave_val = wave_val / max_amplitude

    wav_file=wave.open("test_audio.wav","w")

    nchannels = 1
    sampwidth = 2
    nframes = len(wave_val)
    comptype = "NONE"
    compname = "not compressed"
    wav_file.setparams((nchannels, sampwidth, sample_rate, nframes, comptype, compname))

    for sample in wave_val:
        wav_file.writeframes(struct.pack('h', int( sample * 32767.0 )))

    wav_file.close()



if __name__ == "__main__":
    main()
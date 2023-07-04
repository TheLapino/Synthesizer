from oscillators.SineOscillator import SinWaveOscillator
import wave
import struct
import numpy as np

sample_rate = 44100
def main():
    oscillatorC = SinWaveOscillator(261.63)
    oscillatorE = SinWaveOscillator(329.63)
    oscillatorG = SinWaveOscillator(392.00)

    wave_valC = oscillatorC.generateSound(0.3)
    wave_valE = oscillatorE.generateSound(0.3)
    wave_valG = oscillatorG.generateSound(0.6)
    
    wave_val = np.append(wave_valC, wave_valE)
    wave_val = np.append(wave_val, wave_valG)


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
from audio.fourier import Fourier
from audio.input import input_audio
from audio.signal_gen import SignalGenerator
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
import math

def main():
    rate, funny_square = input_audio("./audio/samples/funny_square.wav")

    if(rate != 44100):
        print("Its over, rate =", rate)

    funny_square_wave = SignalGenerator(duration=0.05)
    sine_wave = SignalGenerator(duration=0.05)
    triangle_wave = SignalGenerator(duration=0.05)
    square_wave = SignalGenerator(duration=0.05)
    saw_wave = SignalGenerator(duration=0.05)

    funny_square_wave.add_wave(funny_square)
    sine_wave.add_sine(256, 10)
    triangle_wave.add_triangle(256, 10)
    square_wave.add_square(256, 10)
    saw_wave.add_saw(256, 10)

    funny_square_wave.plot()

    funny_square_fourier = Fourier(funny_square_wave.wave, 44100)
    sine_fourier = Fourier(sine_wave.wave, 44100)
    triangle_fourier = Fourier(triangle_wave.wave, 44100)
    square_fourier = Fourier(square_wave.wave, 44100)
    saw_fourier = Fourier(saw_wave.wave, 44100)

    funny_square_fourier.plot_spectrum()
    plt.show()

def test_input_audio(filename):
    rate, sound = input_audio(filename)
    
    sound = sound[70000 : 72205]
    
    plt.plot(sound)
    plt.show()
    
    sound_wave = SignalGenerator(duration=0.05)
    sound_wave.add_wave(sound)

    sound_fourier = Fourier(sound_wave.wave, rate)
    peaks = sound_fourier.peaks()
    peak_amps = sound_fourier.peak_amplitudes()
    notes = [Fourier.freq_to_note(freq) for freq in peaks]
    
    print(notes)
    print(peaks)
    plt.scatter(range(1, len(peaks) + 1), peaks) 
    
    sound_fourier.plot_spectrum()
    plt.show()

def test_reverse_fourier(filename, begin = 0, end=44100):
    rate, sound = input_audio(filename)
    
    sound = sound[begin : end]
    
    sound_wave = SignalGenerator(duration=0.05)
    sound_wave.add_wave(sound)

    sound_wave.plot()
    plt.show()

    sound_fourier = Fourier(sound_wave.wave, rate)
    peaks = sound_fourier.peaks()
    peak_amps = sound_fourier.peak_amplitudes()
    
    sound_revfour = SignalGenerator(duration=5)
    
    sound_revfour.reverse_fourier(peaks, peak_amps)
    
    print(peaks)
    print([Fourier.freq_to_note(freq) for freq in peaks])
    
    sound_revfour.write_to_file("./audio/out/out.wav")

def test_file_write():
    square = SignalGenerator(duration=1)
    square.add_square(256, 10)
    square.write_to_file("./audio/out/out.wav")

def test_triangle_formula(): # test triangle formula at 128 Hz
    triangle_approx = SignalGenerator(duration=1)
    index = 1
    
    while 128 * index < 20000:
        triangle_approx.add_sine(128 * index, (-1) ** ((index - 1) / 2) * (8 / math.pi ** 2) * (1 / index ** 2))
        index += 2
    
    triangle_approx.plot()
    plt.show()
    triangle_approx.write_to_file("./audio/out/out.wav")
    
    triangle_real = SignalGenerator(duration=1)
    triangle_real.add_triangle(128, 1)
    triangle_real.write_to_file("./audio/out/triangle.wav")
    
    tri_approx_fourier = Fourier(triangle_approx.wave, 44100)
    tri_real_fourier = Fourier(triangle_real.wave, 44100)
    
    tri_approx_fourier.plot_spectrum()    
    tri_real_fourier.plot_spectrum()
    
    plt.show()
        
    
test_reverse_fourier("./audio/samples/churchbell.wav", 1000, 45100)

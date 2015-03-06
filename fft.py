from pylab import plot, show, title, axis, xlabel, ylabel, subplot, savefig
from scipy import fft, arange, ifft
from numpy import sin, linspace, pi
from scipy.io.wavfile import read,write

def plotAudio(data, fs, time):
 y=data[fs * time:fs * (time + 1),1]
 
 t = linspace(time, time + 1, y.size)
 subplot(2, 1, 1)
 plot(t, y)
 xlabel('Time')
 ylabel('Amplitude')
 
 subplot(2, 1, 2)
 plot(abs(fft(y)))
 axis([0,3000,0,6000])
 xlabel('Freq (Hz)')
 ylabel('|Y(freq)|')
 show()

(fs,data) = read('test.wav')


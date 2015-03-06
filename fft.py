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
 Y = abs(fft(y))
 plot(Y)
 printify(Y)
 axis([0,3000,0,1000])
 xlabel('Freq (Hz)')
 ylabel('|Y(freq)|')
 show()

def printify(Y):
 l = []
 for i in range(1,Y.size - 1):
  if Y[i] > 200:
    l.append(i)
 print l
  

(fs,data) = read('test.wav')


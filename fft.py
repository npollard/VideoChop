from pylab import plot, show, title, axis, xlabel, ylabel, subplot, savefig
from scipy import fft, arange, ifft
from numpy import sin, linspace, pi
from scipy.io.wavfile import read,write

def plotAudio(data, fs, time):
 y=data[fs * time:fs * (time + 1),1]
 Y = abs(fft(y))
 print time, ": ", Y[1350]
  

(fs,data) = read('test.wav')
duration = data[:,1].size/fs
print "time:", duration, "seconds"

for t in range(1, duration - 2):
 plotAudio(data, fs, t)
 

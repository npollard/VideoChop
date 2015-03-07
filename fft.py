from pylab import plot, show, title, axis, xlabel, ylabel, subplot, savefig
from scipy import fft, arange, ifft
from numpy import sin, linspace, pi
from scipy.io.wavfile import read,write

def plotAudio(data, fs, time):
 y=data[fs * time:fs * (time + 1),1]
 Y = abs(fft(y))
 
 t = linspace(time, time + 1, y.size)
 subplot(2, 1, 1)
 plot(t, y)
 xlabel('Time')
 ylabel('Amplitude')
 
 subplot(2, 1, 2)
 plot(abs(fft(y)))
 axis([0,3000,0,1000])
 xlabel('Freq (Hz)')
 ylabel('|Y(freq)|')
 show()

def printAudio(data, fs, time):
 y=data[fs * time:fs * (time + 1),1]
 Y = abs(fft(y))
 print time, ": ", Y[1360]

def rank(data, fs, threshold):
 l = []
 for t in range(1, duration - 2):
  y=data[fs * t:fs * (t + 1),1]
  Y = abs(fft(y))
  l.append([t, sum(Y[670:680])/10 + sum(Y[1340:1360])/20 + sum(Y[2000:2050])/50])
 print "airhorn detected:", map(lambda y: y[0], filter(lambda x: x[1] > threshold, l))

(fs,data) = read('test.wav')
duration = data[:,1].size/fs
print "time:", duration, "seconds"


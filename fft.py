import sys, re
import subprocess as sp
from pylab import plot, show, title, axis, xlabel, ylabel, subplot, savefig
from scipy import fft, arange, ifft
from numpy import array, sin, linspace, pi
from scipy.io.wavfile import read,write

def plotAudio(data, fs, time):
 y=data[fs * time:fs * (time + 1), 1]
 Y = abs(fft(y))
 
 t = linspace(time, time + 1, y.size)
 subplot(2, 1, 1)
 plot(t, y)
 xlabel('Time')
 ylabel('Amplitude')
 
 subplot(2, 1, 2)
 plot(abs(fft(y)))
 #axis([0,3000,0,1000])
 xlabel('Freq (Hz)')
 ylabel('|Y(freq)|')
 show()


def rate(data, fs):
 duration = data.size/fs
 print "time:", duration, "seconds"
 r00 = 670
 r01 = 680
 r10 = 1340
 r11 = 1360
 r20 = 2000
 r21 = 2050
 l = []
 for t in range(1, duration - 2):
  y=data[fs * t:fs * (t + 1)]
  Y = abs(fft(y))
  l.append([t, sum(Y[r00:r01])/(r01 - r00) + sum(Y[r10:r11])/(r11 - r10) + sum(Y[r21:r20])/(r21 - r20)])
 print "ranges: [" + str(r00) + ":" + str(r01) + "] [" + str(r10) + ":" + str(r11) + "] [" + str(r20) + ":" + str(r21) + "]"
 return l

def rateSingle(data, fs, freq):
 duration = data[:].size/fs
 print "time:", duration, "seconds"
 l = []
 for t in range(1, duration - 2):
  y=data[fs * t:fs * (t + 1)]
  Y = abs(fft(y))
  l.append([t, Y[freq]])
 return l


def sortTimes(l):
 for t in sorted(l, key = lambda x: x[1]):
   print t

def filterTimes(l, threshold):
 print "threshold: " + str(threshold)
 raw_times = map(lambda y: y[0], filter(lambda x: x[1] > threshold, l))
 print raw_times

def getWavPath(videoPath):
 return re.match('([\w_-]+\.)\w+', videoPath).group(1) + "wav"

videoPath = sys.argv[1]
wavPath = getWavPath(videoPath)
sp.call(["avconv", "-i", videoPath, "-ab", "160k", "-ac", "1", "-ar", "160000", "-vn", wavPath])

(fs,data) = read(wavPath)
if len(data.shape) > 1:
  data = array(map(lambda x: x[0] + x[1], data))

l = rateSingle(data, fs, 300)
thresh = sorted(l, key = lambda x: x[1], reverse=True)[0][1]/2
filterTimes(l, thresh)






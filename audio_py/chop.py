import os, re, sys
import subprocess as sp
from scipy import fft, arange, ifft
from numpy import array, sin, linspace, pi
from scipy.io.wavfile import read,write

def rateSingle(data, fs, freq1, freq2, freq3):
 duration = data[:].size/fs
 print "time:", duration, "seconds"
 l = []
 for t in range(1, duration - 2):
  y=data[fs * t:fs * (t + 1)]
  Y = abs(fft(y))
  l.append([t, (Y[freq1] ** 2 + Y[freq2] ** 2 + Y[freq3] ** 2) ** (0.5)])
 return l


def sortTimes(l):
 for t in sorted(l, key = lambda x: x[1]):
   print t


def filterTimes(l, threshold):
 print "threshold: " + str(threshold)
 raw_times = map(lambda y: y[0], filter(lambda x: x[1] > threshold, l))
 times = []
 for i in range(0, len(raw_times) - 1):
  if (raw_times[i] + 1 != raw_times[i+1]):
   times.append(raw_times[i])
 times.append(raw_times.pop())
 print "TIMES:", times
 return times

 
def changeExtension(videoPath, ext):
 return re.match('(.*[/\][\w_-]+\.)\w+', videoPath).group(1) + ext


def getChoppedPath(videoPath, i):
 m = re.match('(.*[/\][\w_-]+)(\.\w+)', videoPath)
 return m.group(1) + "_" + str(i).zfill(3) + m.group(2)


def isMTS(videoPath):
 return re.match("(?i).*\.mts$", videoPath) is not None


def timeify(time):
 return str(time / (60 ** 2)).zfill(2) + ":" + str(time / 60 % 60).zfill(2) + ":" + str(time % 60).zfill(2)


def chopVideo(videoPath, times):
 for i in range(0, len(times)):
  start = 0;
  if (i != 0):
   start = times[i - 1]
  duration = times[i] - start
  choppedPath = getChoppedPath(videoPath, i)
  print "CHOPPING: " + str(choppedPath) + " (" + timeify(start) + ", " + timeify(duration) + "), (" + str(start) + ", " + str(times[i]) + ")"
  sp.call(["avconv", "-i", videoPath, "-y", "-ss", timeify(start), "-t", timeify(duration), "-codec", "copy", choppedPath])
 sp.call(["avconv", "-i", videoPath, "-y", "-ss", timeify(times.pop()), "-codec", "copy", getChoppedPath(videoPath, len(times) + 1)])

def chopify(videoPath, freq1, freq2, freq3):
 wavPath = changeExtension(videoPath, "wav")
 sp.call(["avconv", "-i", videoPath, "-ab", "160k", "-ac", "1", "-ar", "160000", "-vn", wavPath])
 (fs,data) = read(wavPath)
 os.remove(wavPath)

 l = rateSingle(data, fs, freq1, freq2, freq3)
 thresh = sorted(l, key = lambda x: x[1], reverse=True)[0][1]/2
 times = filterTimes(l, thresh)

 if (isMTS(videoPath)):
  mp4Path = changeExtension(videoPath, "mp4")
  sp.call(["avconv", "-i", videoPath, "-vcodec", "copy", "-acodec", "copy", mp4Path])
  chopVideo(mp4Path, times)
  os.remove(mp4Path)
 else:
  chopVideo(videoPath, times)




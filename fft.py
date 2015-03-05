from pylab import plot, show, title, axis, xlabel, ylabel, subplot, savefig
from scipy import fft, arange, ifft
from numpy import sin, linspace, pi
from scipy.io.wavfile import read,write

def plotSpectru(y,Fs):
 n = len(y) # lungime semnal
 k = arange(n)
 T = n/Fs
 frq = k/T # two sides frequency range
 frq = frq[range(n/2)] # one side frequency range

 Y = abs(fft(y)) # fft computing and normalization
 Y = Y[range(n/2)]
 
 plot(frq,Y,'r') # plotting the spectrum
 axis([0,3000,0,6000])
 xlabel('Freq (Hz)')
 ylabel('|Y(freq)|')

Fs,data=read('test.wav')
y=data[:,1]
lungime=len(y)
timp=len(y)/44100.
t=linspace(0,timp,len(y))

subplot(2,1,1)
plot(t,y)
xlabel('Time')
ylabel('Amplitude')
subplot(2,1,2)
plotSpectru(y,Fs)
show()


from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
data = np.memmap("signals/readed_data.pcm", dtype='h', mode='r')
print(data[0:1000])
data = data[0:1000]
ps = np.abs(np.fft.fft(data))**2
print(np.fft.fft(data))

time_step = 1 / 30
freqs = np.fft.fftfreq(data.size, time_step)
idx = np.argsort(freqs)
print(max(freqs))
plt.plot(freqs[idx], ps[idx])
plt.show()


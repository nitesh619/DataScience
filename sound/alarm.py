from scipy.fftpack import fft
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

fs, data = wavfile.read('alarm01.wav')
np.set_printoptions(threshold=np.nan)
a = data.T[1]

print(a)
print(data.shape)
print(a.shape)

plt.plot(a, 'b')
plt.show()
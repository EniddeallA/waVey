# GTTS : Google Text-to-Speech (API)
from gtts import gTTS
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from glob import glob
import librosa as lr

tts = gTTS('test', lang='en')
tts.save('./saved/hello.mp3')

data_dir = './saved'
audio_files = glob(data_dir + '/*.mp3')

audio, sfreq = lr.load(audio_files[0])
time = np.arange(0, len(audio)) / sfreq

fig, ax = plt.subplots()
ax.plot(time, audio)
ax.set(xlabel='Time (s)', ylabel='Sound Amplitude')
plt.show()
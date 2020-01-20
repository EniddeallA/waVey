# GTTS : Google Text-to-Speech (API)
from gtts import gTTS
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from glob import glob
import librosa as lr
import sys

class textToWave:
    def __init__(self, text, lang, WaveColor, BgColor) :
        self.text = text
        self.lang = lang
        self.inputPath = './sounds/'
        self.outputPath = './plots/'        
        self.audio = self.inputPath + self.text +'.mp3'
        self.WaveColor = WaveColor
        self.BgColor = BgColor
        self.Outputwave = self.outputPath + self.text + '_' + self.WaveColor + '_' + self.BgColor + '.png'
    
    def textToAudioToWave(self):
        tts = gTTS(self.text, lang=self.lang)
        tts.save(self.audio)
        audio_files = glob(self.audio)
        audio, sfreq = lr.load(audio_files[0])
        time = np.arange(0, len(audio)) / sfreq
        fig, ax = plt.subplots()
        ax.plot(time, audio, color=self.WaveColor)
        plt.axis('off')
        plt.savefig(self.Outputwave, facecolor=self.BgColor)

############# EDIT HERE ##############
text = 'Hello World!'
lang = 'en'
WaveColor = 'white'
BgColor = 'black'
######################################

tw = textToWave(text, lang, WaveColor, BgColor)
tw.textToAudioToWave()
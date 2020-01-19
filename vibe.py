# GTTS : Google Text-to-Speech (API)
from gtts import gTTS
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from glob import glob
import librosa as lr

class textToWave:
    def __init__(self, text, lang) :
        self.text = text
        self.lang = lang
        self.inputPath = './sounds/'
        self.outputPath = './plots/'        
        self.audio = self.inputPath + self.text +'.mp3'
        self.wave = self.outputPath + self.text +'.png'
    
    def textToAudioToWave(self):
        tts = gTTS(self.text, self.lang)
        tts.save(self.audio)
        audio_files = glob(self.audio)
        audio, sfreq = lr.load(audio_files[0])
        time = np.arange(0, len(audio)) / sfreq
        fig, ax = plt.subplots()
        ax.plot(time, audio)
        plt.axis('off')
        plt.savefig(self.wave)
        
tw = textToWave('hello world', 'en')
tw.textToAudioToWave()
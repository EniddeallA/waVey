# VibeCheck

This is a fun side project about converting texts to sound waves using python.

#### How does it work ?

First I use the [gTTS](https://pypi.org/project/gTTS/) Library to interface with Google Translate's text-to-speech API that way I can extract the audio and save it to an mp3 file, then I use [LibROSA](https://librosa.github.io/librosa/) package to extract the waveform and the sampling rate / frequency, the I use [matplotlib](https://matplotlib.org/) library to generate the plot of the sound wave in terms of time and frequency.

#### Additional / Fun tweaks :
      ➕You can use any language supported by Google Translate
      ➕You can change the sound waves color
      ➕You can change the Background Color of the resulted image to match the sound waves color ;)
  
  
#### How to use ?
   1. Clone the repository.
   2. Get to the 'vibe.py' file.
   3. Edit the parameters Like this :
   
   ![alt text](https://github.com/EniddeallA/waVey/Screen%Shot%2020-01-20%at%6.32.08%AM.png)
   
   4. Run the program :
   
    python vibe.py 
   5. You'll find The sound file(.mp3) in the [sounds](https://github.com/EniddeallA/waVey/tree/master/sounds) folder and the sound waves plot(.png) in the [plots](https://github.com/EniddeallA/waVey/tree/master/plots) folder.
   6. Enjoy playing around with it for better aesthetics 😆

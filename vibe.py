# GTTS : Google Text-to-Speech (API)
from gtts import gTTS

tts = gTTS('test', lang='en')
tts.save('./saved/hello.mp3')
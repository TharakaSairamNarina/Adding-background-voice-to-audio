from pydub import AudioSegment
import contextlib
import wave
import os

def length_audio(file_name):
    with contextlib.closing(wave.open(file_name,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
    return int(duration)

sound1 = AudioSegment.from_wav("main_audio.wav")
sound2 = AudioSegment.from_wav("Background_audio.wav")
temp=sound2
len1=length_audio('main_audio.wav')
len2=length_audio('Background_audio.wav')
times=len2//len1
for i in range(times):
    temp+=sound2


combined_sounds = sound1.overlay(temp)
combined_sounds=combined_sounds.set_channels(1)
combined_sounds.export("path to be saved-filename.wav", format="wav")
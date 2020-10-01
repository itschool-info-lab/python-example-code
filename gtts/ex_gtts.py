# -*- coding: utf-8 -*-
from gtts import gTTS
__author__ = 'info-lab'

tts = gTTS(
    text='안녕하세요',
    lang='ko', slow=False
)
tts.save('ex_ko.mp3')

tts1 = gTTS(
    text='Hello',
    lang='en', slow=False
)
tts1.save('ex_en.mp3')

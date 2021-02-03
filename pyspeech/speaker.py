import gtts
import langdetect
import os
import vlc
class Speaker:
    def __init__(self,phrase,hard=False,lang=None):
        if hard:
            if not lang:
                raise ValueError('Hard mode without language')
            self.lang=lang
        else:
            self.lang=langdetect.detect(phrase)
        self.g=gtts.gTTS(phrase)
        self.g.lang=self.lang
    def say(self):
        self.g.save('sample.mp3')
        media=vlc.MediaPlayer('sample.mp3')
        media.play()
    def save(self,where):
        self.g.save(where)
        

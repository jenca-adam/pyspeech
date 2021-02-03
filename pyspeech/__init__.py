from . import speaker
def say(phrase,lang=None,hard=False):
    s=speaker.Speaker(phrase,hard=hard,lang=lang)
    s.say()
    return s
def save(phrase,where,lang=None,hard=False):
    s=speaker.Speaker(phrase,hard=hard,lang=lang)
    s.save(where)
    return s


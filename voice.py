import pyttsx

engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-20)
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()

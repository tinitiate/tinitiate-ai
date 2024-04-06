import pyttsx3


def voice_list():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for v in voices:
        print(v)

# voice_list()
# https://freesound.org/people/UNIVERSFIELD/?

def voice2file():
    engine = pyttsx3.init()
    # engine.say(“Your text here”)
    engine.save_to_file("Asset 1, We detect a large Byeyo in your area, check your surroundings", "test.mp3")
    engine.runAndWait()
    
def voiceList():
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    rate = engine.getProperty('rate')
    volume = engine.getProperty('volume')

    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', rate-15)
    for voice in voices:
        for intonation  in ["+f5", "+f6", "+f7", "+f8"]:
            print(voice.id, intonation)
            engine.setProperty('voice', voice.id + intonation)
            engine.setProperty('volume', volume+.30)
            engine.say("Asset 1!")
            engine.setProperty('volume', volume)
            engine.say("We detect a large Bio in your area! check your surroundings!")
            engine.runAndWait()

            input("Press enter to continue ...")

# voiceList()


def voiceList1():
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    rate = engine.getProperty('rate')
    volume = engine.getProperty('volume')

    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', rate-15)

    for intonation  in ["+f5", "+f6", "+f7", "+f8"]:
        print(voices[1].id, intonation)
        engine.setProperty('voice', voices[1].id + intonation)
        engine.setProperty('volume', volume+1)
        # engine.say("Asset 1!")
        engine.setProperty('rate', rate-20)
        engine.setProperty('volume', volume)
        engine.say("welcome to this day venky!")
        
        engine.runAndWait()

        input("Press enter to continue ...")

voiceList1()
import speech_recognition as aa
import pyttsx3 as pt
import pywhatkit as pw
import datetime as dt
import wikipedia as wiki
import pyjokes as pj

listener = aa.Recognizer()
machine = pt.init()
machine.say("I am your Assistant")
machine.say("What can I do for you")
vo = machine.getProperty('voices')
machine.setProperty('voice', vo[1].id)

def talk(text):
    machine.say(text)
    machine.runAndWait()

def delay():
    sun = 60 - snd.second
    return sun

def input_instruction():
    instruction = ""
    try:
        with aa.Microphone(device_index=0) as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source)
            speech = listener.listen(source)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "jarvis" in instruction:
                instruction = instruction.replace("Jarvis", "")
                print(instruction)
    except aa.UnknownValueError:
        pass
    except aa.RequestError as e:
        print("NULL:{0}".format(e))
        return None
    return instruction

def play_Jarvis():
    a = 0
    global instruction
    instruction = input_instruction()
    print(instruction)
    while True:
        instruction = input_instruction()
        print(instruction)
        if instruction is not None and "bye" in instruction:
            talk("Thank you Have a pleasant day")
            break
        elif instruction is not None and "play" in instruction:
            song = instruction.replace("play", "")
            talk("playing " + song)
            pw.playonyt(song)
        elif instruction is not None and "time" in instruction:
            time = dt.datetime.now().strftime("%I:%M %p")
            talk("current time is " + time)
        elif instruction is not None and "date" in instruction:
            date = dt.datetime.now().strftime("%d/%m/%Y")
            talk("today's date is " + date)
        elif instruction is not None and "how are you" in instruction:
            talk("I am fine, how about you")
        elif instruction is not None and "what is your name" in instruction:
            talk("I am Jarvis, How can I help you?")
        elif instruction is not None and "what is"  in instruction:
            human = instruction.replace("what is", "")
            info = wiki.summary(human, 1)
            print(info)
            talk(info)
        elif instruction is not None and "who is"  in instruction:
            human = instruction.replace("who is", "")
            info = wiki.summary(human, 1)
            print(info)
            talk(info)
        elif instruction is not None and ("bored" in instruction or "depressed" in instruction or "irritated" in instruction):
            snd = dt.datetime.now()
            if snd.minute in [58, 59]:
                a = snd.hour + 1
            else:
                a = snd.hour
            pw.sendwhatmsg("+918015551189", "Your Son is tensed look after him", a, snd.minute + 2)
            talk("Message sent successfully!")
        elif 'joke' in instruction:
            talk(pj.get_joke())
        else:
            talk("Please repeat the instruction")

play_Jarvis()

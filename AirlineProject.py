
import pyttsx3          # This is library which converts text into speech
import speech_recognition as sr     # It converts human speech in written format.
import datetime      # Use to identify the current time
import sys    # for exit our code

engine = pyttsx3.init('sapi5')       # This is API ,it recognize voice
voices = engine.getProperty('voices')    # Get current details of voice
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)      # It set our voice which we are choose ...[0] for david and [1] for zara..here we choose david
engine.setProperty('rate',150)    # It controls speed of a voice.

def speak(audio):
    engine.say(audio)
    engine.runAndWait()     # Take a break

def wishMe():      # It send some greetings like Good morning,Good afternoon ....It depends on a current time.
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<17:
        speak("Good afternoon")
    else:
        speak("Good evening")

    speak("....welcome to spiceJet airlines.......")
    r = sr.Recognizer()
    r.pause_threshold = 1
    speak("........Kindly follow the covid guidelines.......")

def takeCommand():        # It takes input as a user and returns as a string output.

    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Please tell your last four digit of vaccination certificate ")
        r.pause_threshold = 1
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query= r.recognize_google(audio, language='en-in')  # we use here google for voice recognition
        print(f"user said: {query}")    # Formated string use to take query.

    except Exception as e:
        print(e)
        speak("can you say that again please...")
        print("can..say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
# while True:
    if 1:
        query=takeCommand().lower()
file1 = "log file.txt"              # Data Of those who are fully vaccinated
file2 = "log file2.txt"             # Data of those who are partially vaccinated(only one dose is complete)
with open("log file.txt")  as f:
    b=f.read()
with open("log file2.txt")  as f:
    c=f.read()
# we use here conditions.
    if query in b:
      speak("you are fully vaccinated..! so you can go ")


    elif query in c:
      speak("you only taken 1 vaccine..! so sheadule your vaccine as soon as possible")

    else:
      speak("sorry still you are not taken single dose also .....so you not allow to go")



from plyer import notification       # plyer module which is use for send the notification on display .
def notifyMe(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "E:\\GTT Python training\\project code\\python-project--main\\three.ico",  #path of icon in ico format
        timeout = 30
    )

if __name__ == "__main__":
    notifyMe("***Thank You So Much***","Happy Journey")
if __name__ == "__main__":
    notifyMe("Sorry !! ","you only take 1st dose so vaccinate your 2nd dose ASAP")
if __name__ == "__main__":
    notifyMe("Sorry!!","schedule your vaccination on COWIN website as early as possible....stay safe!! ")

engine.runAndWait()

speak(" Thank you so much sir for Visit here ....take care and be stay safe")
sys.exit()


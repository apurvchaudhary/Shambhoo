"""
Main script
"""
import subprocess
from datetime import datetime

import speech_recognition as sr


class Shambhoo:

    def recognise(self):
        """
        speech recognizer
        :return: text/None
        """
        r = sr.Recognizer()
        mic = sr.Microphone()
        try:
            with mic as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                transcript = r.recognize_google(audio)
        except:
            self.say("Sorry, could not get you")
        else:
            return transcript

    def say(self, text):
        """
        method of text to speech
        :param text: str
        :return: None
        """
        subprocess.call(['say', text])

    def main(self):
        """
        main method
        :return: None
        """
        self.say("Hi Sir this is Shambhoo, How are you doing, How can I help you ?")
        phrase = self.recognise()
        if phrase:
            if "time" in phrase and "now" in phrase:
                time_now = datetime.now().strftime("%HH:%MM")
                self.say(f"Currently time is {time_now}")
            else:
                self.say(f"Your command was {phrase}, but right now i could not complete it.")
        else:
            self.say("Sorry !!!")


if __name__ == "__main__":
    s = Shambhoo()
    # calling main from instance
    s.main()

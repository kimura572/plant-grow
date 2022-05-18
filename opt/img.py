import speech_recognition as sr
from asari.api import Sonar

# def mimi():
#   r = sr.Recognizer()
#   with sr.Microphone() as source:
#     r.adjust_for_ambient_noise(source)
#     print("Listening...")
#     audio = r.listen(source)
#     try:
#       query = r.recognize_google(audio, language='ja-JP')
#       sonar = Sonar()
#       res = sonar.ping(text=query)
#       hiryo = res['classes'][1]['confidence']-res['classes'][0]['confidence']
#     except Exception:
#       print("Error")
#   return query, res['top_class'], hiryo

def mimi():
  query,res,hiryo=1,2,3
  return query, res, hiryo
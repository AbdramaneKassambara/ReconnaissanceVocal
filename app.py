import speech_recognition as sr
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Dites quelque chose...")
    audio = recognizer.listen(source)
try:
    text = recognizer.recognize_google(audio)
    print("Texte :", text)
except sr.UnknownValueError:
    print("Impossible de comprendre l'audio.")
import spacy
nlp = spacy.load("fr_core_news_sm")
doc = nlp(text)
for ent in doc.ents:
    print(f"{ent.text}: {ent.label_}")
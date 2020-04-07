import speech_recognition as sr

s_r = sr.Recognizer()
with sr.Microphone(device_index=9) as source:
	print("Скажите что-нибудь")
	audio = s_r.listen(source)

try:
	q = s_r.recognize_google(audio, language="ru-RU")
	print("Вы сказали: " + q.lower())
except sr.UnknownValueError:
	print("Извините, я не понимаю вас")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

import pyttsx3
text_speech = pyttsx3.init()

# to get current rate of the speech
# rate = text_speech.getProperty('rate')

# to set a rate property
text_speech.setProperty('rate',125)

# to change voice, male for index [0], female for index [1]
voices = text_speech.getProperty('voices')
text_speech.setProperty('voice',voices[1].id)

# answer = input("Enter the word you want to speech:")

# to read a text from a file
with open('text.txt','r') as f:
    text = f.readlines()

# to remove line breaks and re in the text
cleaned_text = list(map(lambda x: x.strip('\n'), text))
print(cleaned_text)

# text into speech  and save it as a mp3 file
text_speech.say(cleaned_text)

text_speech.save_to_file(cleaned_text,'output.mp3')
text_speech.runAndWait()



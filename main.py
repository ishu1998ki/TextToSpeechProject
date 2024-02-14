import pyttsx3
import PyPDF2

text_speech = pyttsx3.init()

# to get current rate of the speech
# rate = text_speech.getProperty('rate')

# to set a rate property
text_speech.setProperty('rate',125)

# to change voice, male for index [0], female for index [1]
voices = text_speech.getProperty('voices')
text_speech.setProperty('voice',voices[1].id)

# creating a pdf file object
pdfFileObj = open('ass.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfReader(pdfFileObj)

# printing number of pages in pdf file
# print("Number of pages in this pdf = " +len(pdfReader.pages))

# creating a page object
pageObj = pdfReader.pages[1]

# to extract content in the page
extractedText = pageObj.extract_text()

# to remove line breaks in the text
cleaned_text = list(map(lambda x: x.strip('\n'), extractedText))

# Join the characters to form a single string
result_string = ''.join(cleaned_text)
print(result_string)
# print(cleaned_text)
text_speech.say(result_string)

text_speech.save_to_file(result_string,'output.mp3')
text_speech.runAndWait()

# closing the pdf file object
pdfFileObj.close()



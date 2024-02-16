import pyttsx3
import PyPDF2

text_speech = pyttsx3.init()

# to get current rate of the speech
# rate = text_speech.getProperty('rate')

# to set a rate property
text_speech.setProperty('rate', 125)

# to change voice, male for index [0], female for index [1]
voices = text_speech.getProperty('voices')
text_speech.setProperty('voice', voices[1].id)

# creating a pdf file object
pdfFileObj = open('ass.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfReader(pdfFileObj)

lengthOfPDF = len(pdfReader.pages)
# printing number of pages in pdf file
print("Number of pages in this pdf = " + str(lengthOfPDF))

# creating a loop for read pages one by one, and create a separate
# audio files for each page.

for i in range(lengthOfPDF):
    pageObj = pdfReader.pages[i]
    extractedText = pageObj.extract_text()
    # remove newlines
    cleaned_text = list(map(lambda x: x.strip('\n'), extractedText))
    result_string = ''.join(cleaned_text)
    # saving in separate audio file
    text_speech.save_to_file(result_string, "page_"+str(i)+'.mp3')

text_speech.runAndWait()

# closing the pdf file object
pdfFileObj.close()
print("Successfull!")

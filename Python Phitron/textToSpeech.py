# Make Speaker
import pyttsx3
import PyPDF2
# Book 
book = open('cc.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(book)  
pages = len(pdfReader.pages)  
print(pages)
speaker = pyttsx3.init()

# page number
page = pdfReader.pages[8]
text = page.extract_text()

speaker.say(text)
speaker.runAndWait()
import PyPDF2


def pdf_reader(path):
    
    file = open(path,"rb")
    pdfReader = PyPDF2.PdfFileReader(file)
    clean_text = ""
    for page in range(pdfReader.numPages):
        text = pdfReader.getPage(page).extractText()
        clean_text = clean_text + text.strip().replace("\n"," ")
    
    return clean_text

            
        


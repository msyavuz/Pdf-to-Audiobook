import PySimpleGUI as sg
from numpy import size
from tts import text_to_audio
from pdf import pdf_reader


sg.theme("DarkTanBlue")



layout = [[sg.Text("Please choose a pdf file to convert: "), sg.FileBrowse(auto_size_button=True,key="filepath")],
          [sg.Text("Please choose a language: "), sg.Combo(["English","Turkish"],default_value="English",key="lang",readonly=True)],
          [sg.Text("Please enter audiobooks name: "), sg.Input(key="name",size=(30,30))],
          [sg.Checkbox("Slow reading",key="slow",tooltip="Enables the slow reading option for text to speech")],
          [sg.Text("This may take a while please be patient."),sg.Button("Convert")]   
         ]


window = sg.Window("Pdf to Audiobook",layout,size=(500,150),element_justification="c")


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    elif event == "Convert":
        filepath=values["filepath"]
        name=values["name"]
        if values["lang"]=="English":
            lang="en"
        elif values["lang"]=="Turkish":
            lang="tr"
        slow=values["slow"]
        text = pdf_reader(filepath)
        text_to_audio(text,lang,name,slow)

window.close()



    







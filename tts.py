from gtts import gTTS


def text_to_audio(text,lang,name,slow=False):
    
    audio = gTTS(text=text,lang=lang,slow=slow)
    audio.save(f"{name}.mp3")
    
    

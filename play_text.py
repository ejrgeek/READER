from gtts import gTTS
import subprocess as sp


def play(string):
    text = gTTS(string, lang='pt-BR')
    text.save('text.mp3')

    # Mudar de acordo com a necessidade
    sp.call(['rhythmbox', 'text.mp3'])

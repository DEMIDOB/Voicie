import telebot
import requests
import speech_recognition as sr

from os import path, system

r = sr.Recognizer()


def get_oga_content(filepath, token):
    recieved = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(token, filepath))
    if recieved.status_code != 200:
        return False
    return recieved.content


def save_tmp_oga(content):
    tmp_oga_file = open('tmp.oga', 'wb')
    tmp_oga_file.write(content)
    tmp_oga_file.close()
    return True


def convert_voice_to_wav():
    in_filename = 'tmp.oga'
    out_filename = 'voice.wav'
    command = "ffmpeg -y -i " + in_filename + " " + out_filename
    system(command)


def recognize():
    AUDIO_FILE = path.abspath("voice.wav")

    #print(AUDIO_FILE)

    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)

    ret = r.recognize_google(audio, language="ru-RU")
    return ret


def handle_voice(message, bot, token):
    # Get the voice message's file contents in .oga format
    oga_content = get_oga_content(bot.get_file(message.voice.file_id).file_path, token)

    # Save it to 'tmp.oga'
    save_tmp_oga(oga_content)

    # Converting to wav using ffmpeg and saving the result to 'voice.wav'
    convert_voice_to_wav()

    # Recognizing speech
    recognized = "rec"
    try:
        recognized = recognize().lower()
    except:
        print("smth bad")
    return recognized
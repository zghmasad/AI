from gtts import gTTS
import os

def get_text_input():
    return input("Enter the text you want to convert to speech: ")

def text_to_speech_gtts(text, output_file):
    tts = gTTS(text=text, lang='en')
    tts.save(output_file)
    print(f'Audio content written to file {output_file}')

def main():
    text = get_text_input()
    output_file = "output.mp3"
    text_to_speech_gtts(text, output_file)

if __name__ == "__main__":
    main()

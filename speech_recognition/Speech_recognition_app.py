import tkinter as tk
from tkinter import scrolledtext
import threading
import speech_recognition as sr

class ASRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Real-Time ASR for Deaf Individuals")
        self.root.geometry("600x400")

        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 14))
        self.text_area.pack(expand=True, fill='both')

        self.customize_button = tk.Button(root, text="Customize", command=self.customize)
        self.customize_button.pack(side=tk.BOTTOM)

        self.start_button = tk.Button(root, text="Start Listening", command=self.start_listening)
        self.start_button.pack(side=tk.BOTTOM)

    def customize(self):
        custom_window = tk.Toplevel(self.root)
        custom_window.title("Customize Text")

        tk.Label(custom_window, text="Font Size:").pack()
        self.font_size = tk.IntVar(value=14)
        tk.Spinbox(custom_window, from_=8, to=48, textvariable=self.font_size, command=self.update_font).pack()

        tk.Label(custom_window, text="Text Color:").pack()
        self.text_color = tk.StringVar(value="black")
        tk.Entry(custom_window, textvariable=self.text_color).pack()
        tk.Button(custom_window, text="Apply", command=self.update_color).pack()

    def update_font(self):
        new_font_size = self.font_size.get()
        self.text_area.config(font=("Arial", new_font_size))

    def update_color(self):
        new_color = self.text_color.get()
        self.text_area.config(fg=new_color)

    def start_listening(self):
        self.listening_thread = threading.Thread(target=self.capture_audio)
        self.listening_thread.start()

    def capture_audio(self):
        recognizer = sr.Recognizer()
        mic = sr.Microphone()

        with mic as source:
            print("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            self.update_text_area(text)
        except sr.UnknownValueError:
            self.update_text_area("Sorry, I did not understand that.")
        except sr.RequestError as e:
            self.update_text_area(f"Could not request results; {e}")

    def update_text_area(self, text):
        self.text_area.insert(tk.END, text + "\n")
        self.text_area.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ASRApp(root)
    root.mainloop()

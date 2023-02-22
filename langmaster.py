import tkinter as tk
from googletrans import Translator
import pytesseract
import cv2

class LangMasterTranslation(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("LangMaster Translation")
        self.geometry("1024x768")

        self.translator = Translator()

        self.lang_var = tk.StringVar()
        self.lang_var.set("English (Default)")
        self.language_options = [
        ("Afrikaans", "af"),
        ("Albanian", "sq"),
        ("Amharic", "am"),
        ("Arabic", "ar"),
        ("Armenian", "hy"),
        ("Azerbaijani", "az"),
        ("Basque", "eu"),
        ("Belarusian", "be"),
        ("Bengali", "bn"),
        ("Bosnian", "bs"),
        ("Bulgarian", "bg"),
        ("Catalan", "ca"),
        ("Cebuano", "ceb"),
        ("Chichewa", "ny"),
        ("Chinese (Simplified)", "zh-CN"),
        ("Chinese (Traditional)", "zh-TW"),
        ("Corsican", "co"),
        ("Croatian", "hr"),
        ("Czech", "cs"),
        ("Danish", "da"),
        ("Dutch", "nl"),
        ("English", "en"),
        ("Esperanto", "eo"),
        ("Estonian", "et"),
        ("Filipino", "tl"),
        ("Finnish", "fi"),
        ("French", "fr"),
        ("Frisian", "fy"),
        ("Galician", "gl"),
        ("Georgian", "ka"),
        ("German", "de"),
        ("Greek", "el"),
        ("Gujarati", "gu"),
        ("Haitian Creole", "ht"),
        ("Hausa", "ha"),
        ("Hawaiian", "haw"),
        ("Hebrew", "he"),
        ("Hindi", "hi"),
        ("Hmong", "hmn"),
        ("Hungarian", "hu"),
        ("Icelandic", "is"),
        ("Igbo", "ig"),
        ("Indonesian", "id"),
        ("Irish", "ga"),
        ("Italian", "it"),
        ("Japanese", "ja"),
        ("Kannada", "kn"),
        ("Kazakh", "kk"),
        ("Khmer", "km"),
        ("Korean", "ko"),
        ("Kurdish (Kurmanji)", "ku"),
        ("Kyrgyz", "ky"),
        ("Lao", "lo"),
        ("Latin", "la"),
        ("Latvian", "lv"),
        ("Lithuanian", "lt"),
        ("Luxembourgish", "lb"),
        ("Macedonian", "mk"),
        ("Malagasy", "mg"),
        ("Malay", "ms"),
        ("Malayalam", "ml"),
        ("Maltese", "mt"),
        ("Maori", "mi"),
        ("Marathi", "mr"),
        ("Mongolian", "mn"),
        ("Myanmar (Burmese)", "my"),
        ("Nepali", "ne"),
        ("Norwegian", "no"),
        ("Pashto", "ps"),
        ("Persian", "fa"),
        ("Polish", "pl"),
        ("Portuguese", "pt"),
        ("Punjabi", "pa"),
        ("Romanian", "ro"),
        ("Russian", "ru"),
        ("Samoan", "sm"),
        ("Scots Gaelic", "gd"),
        ("Serbian", "sr"),
        ("Sesotho", "st"),
        ("Shona", "sn"),
        ("Sindhi", "sd"),
        ("Sinhala", "si"),
        ("Slovenian", "sl"),
        ("Somali", "so"),
        ("Spanish", "es"),
        ("Sundanese", "su"),
        ("Swahili", "sw"),
        ("Swedish", "sv"),
        ("Tajik", "tg"),
        ("Tamil", "ta"),
        ("Telugu", "te"),
        ("Thai", "th"),
        ("Turkish", "tr"),
        ("Ukrainian", "uk"),
        ("Urdu", "ur"),
        ("Uzbek", "uz"),
        ("Vietnamese", "vi"),
        ("Welsh", "cy"),
        ("Xhosa", "xh"),
        ("Yiddish", "yi"),
        ("Yoruba", "yo"),
        ("Zulu", "zu")
        ]
        
        self.input_text = tk.Text(self, height=5, width=50)
        self.input_text.pack(side="left", fill="both", expand=True)
        self.input_text.insert(tk.END, "Enter text to translate...")

        self.output_text = tk.Text(self, height=5, width=50)
        self.output_text.pack(side="right", fill="both", expand=True)
        self.output_text.insert(tk.END, "Translation will appear here...")

        self.language_dropdown = tk.OptionMenu(self, self.lang_var, *[lang[0] for lang in self.language_options])
        self.language_dropdown.pack(side="top", fill="both")

        self.voice_search_button = tk.Button(self, text="Voice Search", command=self.voice_search, font=("Helvetica", 16))
        self.voice_search_button.pack(side="bottom")

        self.translate_image_btn = tk.Button(self, text="Translate from Image", command=self.translate_img, font=("Helvetica", 16))
        self.translate_image_btn.pack(side="bottom")

        self.translate_button = tk.Button(self, text="Translate", command=self.translate, font=("Helvetica", 16))
        self.translate_button.pack(side="bottom")
        import darkdetect

        if darkdetect.isDark():
            self.config(bg="gray20")
            self.input_text.config(bg="gray20", fg="white")
            self.output_text.config(bg="gray20", fg="white")
            self.translate_button.config(bg="gray20", fg="white")
            self.voice_search_button.config(bg="gray20", fg="white")
            self.translate_image_btn.config(bg="gray20", fg="white")
            self.language_dropdown.config(bg="gray20", fg="white")
        
    def translate(self):
        input_text = self.input_text.get("1.0", "end")
        dest = [lang[1] for lang in self.language_options if lang[0] == self.lang_var.get()][0]
        output_text = self.translator.translate(input_text, dest=dest).text
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, output_text)
    def voice_search(self):
        import speech_recognition as sr
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            self.input_text.delete("1.0", tk.END)
            self.input_text.insert("1.0", text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

    def translate_img(self):
        from tkinter import filedialog
        file_path = filedialog.askopenfilename()
        image = cv2.imread(file_path)
        try:
            pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
            text = pytesseract.image_to_string(image)
            self.input_text.delete("1.0", tk.END)
            self.input_text.insert(tk.END, text)
        except pytesseract.TesseractNotFoundError:
            import tkinter as tk
            root = tk.Tk()
            root.wm_title = "Tesseract not found"
            root.title = "Tesseract not found"
            label = tk.Label(root, text="The tesseract package needs to be installed. Would you like to install the tesseract package?").pack()
            def yes():
                import os
                os.system('powershell Start-BitsTransfer -Source "https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.0.20221222.exe" -Destination "%temp%\\tesseract-ocr-w64-setup-5.3.0.20221222.exe"')
                os.system("%temp%\\tesseract-ocr-w64-setup-5.3.0.20221222.exe")
            def no():
                root.destroy()
            yesbutton = tk.Button(root, text="Yes", command=yes, font=("Helvetica", 12)).pack()
            nobutton = tk.Button(root, text="No", command=no, font=("Helvetica", 12)).pack()
            root.mainloop()


app = LangMasterTranslation()
app.mainloop()

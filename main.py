from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit, QPushButton, QComboBox, QMessageBox
from PyQt5 import uic
import googletrans
import textblob
import sys

class TranslatorApp(QMainWindow):
    def __init__(self):
        super(TranslatorApp, self).__init__()

        uic.loadUi("app.ui", self)
        Window_Width = 692
        Window_Height = 303
        self.setFixedSize(Window_Width, Window_Height)

        self.from_text = self.findChild(QTextEdit, "from_text")
        self.to_text = self.findChild(QTextEdit, "to_text")
        self.translate_btn = self.findChild(QPushButton, "translate_btn")
        self.clear_btn = self.findChild(QPushButton, "clear_btn")
        self.paste_btn = self.findChild(QPushButton, "paste_btn")
        self.copy_btn = self.findChild(QPushButton, "copy_btn")
        self.from_comb = self.findChild(QComboBox, "comboBox")
        self.to_comb = self.findChild(QComboBox, "comboBox_2")

        self.languages = googletrans.LANGUAGES
        # print(self.languages)
        self.language_list = list(self.languages.values())
        # print(self.language_list)
        # print(len(self.language_list))
        self.from_comb.addItems(self.language_list)
        self.to_comb.addItems(self.language_list)

        self.from_comb.setCurrentText("english")
        self.to_comb.setCurrentText("amharic")

        self.translate_btn.clicked.connect(self.translate)
        self.clear_btn.clicked.connect(self.clear)
        self.paste_btn.clicked.connect(self.paste)
        self.copy_btn.clicked.connect(self.copy)

        self.show()

    def translate(self):
        try:
            for key, value in self.languages.items():
                if (value == self.from_comb.currentText()):
                    from_lang_key = key

            for key, value in self.languages.items():
                if (value == self.to_comb.currentText()):
                    to_lang_key = key

            words = textblob.TextBlob(self.from_text.toPlainText())
            words = words.translate(from_lang=from_lang_key, to=to_lang_key)

            self.to_text.setText(str(words))

        except Exception as e:
            QMessageBox.critical(self, "Translator", str(e))

    def clear(self):
        self.from_text.setText("")
        self.to_text.setText("")

    def copy(self):
        pass

    def paste(self):
        pass

app = QApplication(sys.argv)
window = TranslatorApp()
app.exec_()
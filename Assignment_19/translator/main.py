import sys
from functools import partial
import gtts
from PySide6.QtWidgets import QApplication, QMainWindow,QMessageBox
from ui_main_window import Ui_MainWindow

class Translator(QMainWindow):
     def __init__(self):
          super().__init__()
          with open("Assignment_19/translator/Translate.txt","r") as database_translate:
               temp = database_translate.read().split("\n")
               self.words_bank = []
               for line in range(0,len(temp) - 1,2):
                   my_dictionary = {"english":temp[line],"persian":temp[line+1]}
                   self.words_bank.append(my_dictionary)
          self.message_box = QMessageBox()
          self.ui = Ui_MainWindow()
          self.ui.setupUi(self)
          self.mode = ""

     def choice_mode(self, mode_translate):
          self.mode = mode_translate

     def translate(self):
          if window.mode == "":
               window.message_box.setWindowTitle("Error")
               window.message_box.setText("Please select your translate language.")
               window.message_box.exec()
          elif self.mode == "Persian to English":
               input_text = self.ui.input_text.text()
               input_words = input_text.split(" ")

               output_words = []
               for input_word in input_words:
                  translated_word = self.translate_persian_word(input_word)
                  output_words.append(translated_word)

               output_text = " ".join(output_words)
               self.ui.output_text.setText(output_text)

          elif self.mode == "English to Persian":
               input_text = self.ui.input_text.text()
               input_words = input_text.split(" ")

               output_words = []
               for input_word in input_words:
                  translated_word = self.translate_english_word(input_word)
                  output_words.append(translated_word)

               output_text = " ".join(output_words)
               self.ui.output_text.setText(output_text)

     def translate_persian_word(self, input_word):
          for word in self.words_bank:
               if input_word == word["persian"]:
                    return word["english"]
          return input_word

     def translate_english_word(self, input_word):
          for word in self.words_bank:
               if input_word == word["english"]:
                    return word["persian"]
          return input_word

if __name__ == "__main__":
     app = QApplication(sys.argv)
     
     window = Translator()
     
     window.ui.rdbtn_pr_en.clicked.connect(partial(window.choice_mode, "Persian to English"))
     window.ui.rdbtn_en_pr.clicked.connect(partial(window.choice_mode, "English to Persian"))

     window.ui.btn_translate.clicked.connect(partial(window.translate))

     window.show()

     app.exec()

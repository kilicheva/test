import string
from googletrans import Translator

class Translate:
    def __init__(self, word_obj='яблоко'):
        self.translator = Translator()
        self.word = word_obj


    def translator_text(self):
        if self.word[0].upper() in string.ascii_uppercase:
            translate_word = self.translator.translate(self.word, dest='ru').text
            return translate_word
        elif self.word[0].upper() in string.ascii_uppercase:
            translate_word = self.translator.translate(self.word, dest='en').text
            return translate_word

translator1 = Translate('яблоко')
print(translator1.translator_text())
translator2 = Translate('technology')
print(translator2.translator_text())
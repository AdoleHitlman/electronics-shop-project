from src.item import Item


class LanguageMixin:
    SUPPORTED_LANGS = ['EN', 'RU']

    def __init__(self):
        self._language = 'EN'

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        if value not in self.SUPPORTED_LANGS:
            raise AttributeError("property 'language' of 'KeyBoard' object has no setter")
        self._language = value

    def change_lang(self):
        langs = self.SUPPORTED_LANGS
        curr_lang = self.language
        next_lang = langs[(langs.index(curr_lang) + 1) % len(langs)]
        self.language = next_lang
        return self


class Keyboard(Item, LanguageMixin):
    def __str__(self):
        return self.name



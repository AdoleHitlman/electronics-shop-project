from src.keyboard import Keyboard

kb = Keyboard('Runo', 1000, 5)

def test_language():
    assert str(kb.language) == "EN"

def test_change_lang():
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"


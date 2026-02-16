from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

roman_text = "ye gaana bahut accha hai"
devanagari_text = transliterate(roman_text, sanscript.ITRANS, sanscript.DEVANAGARI)
print(devanagari_text)  # ये गाना बहुत अच्छा है

class MorseTranslator:
    _CHARS_TO_MORSE = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
        "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
        "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
        "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
        "Z": "--..",
        "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
        "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
        ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.", "!": "-.-.--",
        "/": "-..-.", "(": "-.--.", ")": "-.--.-", "&": ".-...", ":": "---...",
        ";": "-.-.-.", "=": "-...-", "+": ".-.-.", "-": "-....-", "_": "..--.-",
        '"': '.-..-.', "$": '...-..-', "@": '.--.-.'
    }
    _MORSE_TO_CHARS = {value: key for key, value in _CHARS_TO_MORSE.items()}

    def __init__(self, *, dot=".", dash="-", separator=" ", space="/"):
        self.dot = dot
        self.dash = dash
        self.separator = separator
        self.space = space

    def encode(self, text):
        fragments = []
        for char in text.upper():
            fragment = self.space if char == " " else MorseTranslator._CHARS_TO_MORSE.get(char, "#")
            fragment = fragment.replace(".", self.dot).replace("-", self.dash)
            fragments.append(fragment)
        return self.separator.join(fragments)

    def decode(self, code):
        fragments = code.split(self.separator)
        chars = []
        for fragment in fragments:
            fragment = fragment.replace(self.dot, ".").replace(self.dash, "-")
            char = " " if fragment == self.space else MorseTranslator._MORSE_TO_CHARS.get(fragment, "#")
            chars.append(char)
        return "".join(chars)

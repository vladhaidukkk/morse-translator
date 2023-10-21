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
        fragments = [
            self.space if char == " " else MorseTranslator._CHARS_TO_MORSE.get(char, "#")
            .replace(".", self.dot)
            .replace("-", self.dash)
            for char in text.upper()
        ]
        return self.separator.join(fragments)

    def decode(self, code):
        if not code:
            return ""
        fragments = code.split(self.separator)
        chars = [
            " " if fragment == self.space else MorseTranslator._MORSE_TO_CHARS.get(
                fragment.replace(self.dot, ".").replace(self.dash, "-"), "#"
            )
            for fragment in fragments
        ]
        return "".join(chars)

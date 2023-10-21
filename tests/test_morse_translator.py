import unittest
from parameterized import parameterized
from morse_translator import MorseTranslator


class TestMorseTranslator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.default_translator = MorseTranslator()
        cls.modified_translator = MorseTranslator(dot="+", dash="=", separator="_", space="&")

    @parameterized.expand([
        ("", ""),
        ("A", ".-"),
        ("ABC", ".- -... -.-."),
        ("ABC XYZ", ".- -... -.-. / -..- -.-- --.."),
        ("0 19 .,? $@", "----- / .---- ----. / .-.-.- --..-- ..--.. / ...-..- .--.-."),
        ("Abc dE", ".- -... -.-. / -.. ."),
        ("abc de", ".- -... -.-. / -.. ."),
        ("{", "#"),
        ("{}", "# #"),
        ("{1}", "# .---- #"),
    ])
    def test_default_encoding(self, text, expected):
        self.assertEqual(expected, self.default_translator.encode(text))

    @parameterized.expand([
        ("", ""),
        ("A", "+="),
        ("ABC", "+=_=+++_=+=+"),
        ("ABC XYZ", "+=_=+++_=+=+_&_=++=_=+==_==++"),
        ("0 19 .,? $@", "=====_&_+====_====+_&_+=+=+=_==++==_++==++_&_+++=++=_+==+=+"),
        ("Abc dE", "+=_=+++_=+=+_&_=++_+"),
        ("abc de", "+=_=+++_=+=+_&_=++_+"),
        ("{", "#"),
        ("{}", "#_#"),
        ("{1}", "#_+====_#"),
    ])
    def test_modified_encoding(self, text, expected):
        self.assertEqual(expected, self.modified_translator.encode(text))

    @parameterized.expand([
        ("", ""),
        (".-", "A"),
        (".- -... -.-.", "ABC"),
        (".- -... -.-. / -..- -.-- --..", "ABC XYZ"),
        ("----- / .---- ----. / .-.-.- --..-- ..--.. / ...-..- .--.-.", "0 19 .,? $@"),
        ("A", "#"),
        ("A.--", "#"),
        ("A .--", "#W"),
    ])
    def test_default_decoding(self, code, expected):
        self.assertEqual(expected, self.default_translator.decode(code))

    @parameterized.expand([
        ("", ""),
        ("+=", "A"),
        ("+=_=+++_=+=+", "ABC"),
        ("+=_=+++_=+=+_&_=++=_=+==_==++", "ABC XYZ"),
        ("=====_&_+====_====+_&_+=+=+=_==++==_++==++_&_+++=++=_+==+=+", "0 19 .,? $@"),
        ("A", "#"),
        ("A+==", "#"),
        ("A_+==", "#W"),
    ])
    def test_modified_decoding(self, code, expected):
        self.assertEqual(expected, self.modified_translator.decode(code))


if __name__ == "__main__":
    unittest.main()

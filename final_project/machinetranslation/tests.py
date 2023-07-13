from translator import english_to_french, french_to_english
import unittest

class TranslatorTests(unittest.TestCase):
    def test_englishToFrench_hello(self):
        english_text = "Hello"
        french_text = english_to_french(english_text)
        expected_text = "Bonjour"
        self.assertEqual(french_text, expected_text)

    def test_englishToFrench_bonjour(self):
        english_text = "Bonjour"
        french_text = english_to_french(english_text)
        expected_text = "Hello"
        self.assertEqual(french_text, expected_text)

    def test_frenchToEnglish_bonjour(self):
        french_text = "Bonjour"
        english_text = french_to_english(french_text)
        expected_text = "Hello"
        self.assertEqual(english_text, expected_text)

    def test_frenchToEnglish_hello(self):
        french_text = "Hello"
        english_text = french_to_english(french_text)
        expected_text = "Bonjour"
        self.assertEqual(english_text, expected_text)

if __name__ == '__main__':
    unittest.main()
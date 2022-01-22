import unittest
from .ethnicity import Ethnicity


class TestEthnicity(unittest.TestCase):

    slavs_tokenizer = Ethnicity('славян(е*)?')
    germans_tokenizer = Ethnicity('германц(ы|ев*)')


    def test_lower_slavs(self):

        doc = 'Именительный: славяне;'   \
              'родительный: славян;'     \
              'дательный: славянам;'     \
              'винительный: славян;'     \
              'творительный: славянами;' \
              'предложный: о славянах;'

        tokens = [token for token in self.slavs_tokenizer.tokenize(doc)]
        self.assertEqual(6, len(tokens))


    def test_upper_slavs(self):
        doc = 'Именительный: Славяне;'   \
              'родительный: Славян;'     \
              'дательный: Славянам;'     \
              'винительный: Славян;'     \
              'творительный: Славянами;' \
              'предложный: о Славянах;'

        tokens = [token for token in self.slavs_tokenizer.tokenize(doc)]
        self.assertEqual(6, len(tokens))


    def test_lower_germans(self):

        doc = 'Именительный: германцы;'   \
              'родительный: германцев;'   \
              'дательный: германцам;'     \
              'винительный: германцев;'   \
              'творительный: германцами;' \
              'предложный: о германцах;'

        tokens = [token for token in self.germans_tokenizer.tokenize(doc)]
        self.assertEqual(6, len(tokens))


    def test_upper_germans(self):
        doc = 'Именительный: Германцы;'   \
              'родительный: Германцев;'   \
              'дательный: Германцам;'     \
              'винительный: Германцев;'   \
              'творительный: Германцами;' \
              'предложный: о Германцах;'

        tokens = [token for token in self.germans_tokenizer.tokenize(doc)]
        self.assertEqual(6, len(tokens))


    def test_to_string(self):
        self.assertEqual('славяне',  str(self.slavs_tokenizer))
        self.assertEqual('германцы', str(self.germans_tokenizer))


    def test_yaml(self):
        arr = Ethnicity.all()
        self.assertTrue(len(arr) > 100)


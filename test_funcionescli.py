from unittest import TestCase


class Test(TestCase):
    def test_valido_dni(self):
        from funcionescli import validoDNI
        self.assertTrue(validoDNI('00000000T'))

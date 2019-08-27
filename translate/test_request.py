#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from translate import translate


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.example = 'bla-bla'
        self.good_response = translate('Hello')

    @unittest.expectedFailure
    def test_error(self):
        self.assertEqual(translate('')['code'], 200)

    def test_good_response(self):
        self.assertEqual(self.good_response['code'], 200)
        self.assertMultiLineEqual(''.join(self.good_response['text']), 'Привет')

    def test_raises(self):
        with self.assertRaises(KeyError):
            translate('')['text']

    def test_code_response(self):
        self.assertEqual(translate('Hello', 'yy')['code'], 501)
        self.assertEqual(translate('Hello', key='bla-bla-bla')['code'], 401)
        self.assertEqual(translate(f'{self.example * 2000}')['code'], 413)


if __name__ == '__main__':
    unittest.main()

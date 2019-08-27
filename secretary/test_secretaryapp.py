#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json
import unittest
import app
from unittest.mock import patch


documents = []
directories = {}

path_documents = os.path.join('fixtures', 'documents.json')
path_directories = os.path.join('fixtures', 'directories.json')

with open(path_documents, 'rt', encoding='utf8') as file:
    documents.extend(json.load(file))
with open(path_directories, 'rt', encoding='utf8') as file:
    directories.update(json.load(file))


@patch('app.documents', documents, create=True)
@patch('app.directories', directories, create=True)
class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.example_doc_except = {'type': 'pass', 'number': '0000',}

    def test_check_value(self):
        self.assertTrue(app.check_document_existance('10006'))
        self.assertFalse(app.check_document_existance('0a0a0a0a'))

    @patch('builtins.input', lambda *args: '10006')
    def test_get_value(self):
        self.assertMultiLineEqual(app.get_doc_owner_name(), 'Аристарх Павлов')
        self.assertEqual(app.get_doc_shelf(), '2')

    def test_include(self):
        self.assertCountEqual(app.get_all_doc_owners_names(), [docs["name"] for docs in documents])

    @patch('builtins.input', side_effect=['666', 'book', 'NameX', '13'])
    def test_add_items(self, mock_input):
        self.assertEqual(app.add_new_doc(), '13')
        self.assertGreaterEqual(len(documents), 4)
        self.assertIn('666', directories['13'])
        self.assertIn('666', [docs['number'] for docs in documents])

    def test_raises(self):
        self.assertRaises(KeyError, app.show_document_info, self.example_doc_except)

    @patch('builtins.input', side_effect=['11-2', '3'])
    @patch('builtins.print', lambda *args: None)
    def test_move(self, mock_input):
        app.move_doc_to_shelf()
        self.assertIn('11-2', directories['3'])

    def test_remove_from_shelf(self):
        app.remove_doc_from_shelf('666')
        self.assertNotIn('666', directories['13'])

    @patch('builtins.input', lambda *args: '2207 876234')
    def test_delete_doc(self):
        self.assertTupleEqual(app.delete_doc(), ('2207 876234', True))
        self.assertNotIn('2207 876234', [doc['number'] for doc in documents])


if __name__ == '__main__':
    unittest.main()

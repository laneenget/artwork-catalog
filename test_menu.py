from unittest import TestCase
from menu import Menu

class TestMenu(TestCase):

    def setUp(self):

        self.menu = Menu()

        def a():
            pass

        def b():
            pass

        self.a = a
        self.b = b

        self.menu.add_command('a', 'command a', a)
        self.menu.add_command('b', 'command b', b)

    def test_add_command(self):
        self.assertDictEqual({'a': 'command a', 'b': 'command b'}, self.menu.descriptions)
        self.assertDictEqual({'a': self.a, 'b': self.b}, self.menu.functions)

    def test_is_valid(self):
        self.assertTrue(self.menu.is_valid('a'))
        self.assertTrue(self.menu.is_valid('b'))

    def test_not_valid(self):
        self.assertFalse(self.menu.is_valid('c'))
        self.assertFalse(self.menu.is_valid('puppy'))
        self.assertFalse(self.menu.is_valid(123))

    def test_get_action(self):
        self.assertEqual(self.a, self.menu.get_action('a'))
        self.assertEqual(self.b, self.menu.get_action('b'))

    def test_get_no_action(self):
        self.assertIsNone(self.menu.get_action('c'))
        self.assertIsNone(self.menu.get_action('puppy'))
        self.assertIsNone(self.menu.get_action(123))

    def test_str(self):
        menu_string = 'a: command a\nb: command b'
        self.assertEqual(menu_string, str(self.menu))
# test_noisy_animal.py

import unittest
from io import StringIO
import sys
from noisy_animal import NoisyAnimal

class TestNoisyAnimal(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def tearDown(self):
        self.held.close()
        sys.stdout = self.held

    def test_cat_loud(self):
        animal = NoisyAnimal('cat')
        animal.make_noise()
        self.assertEqual(sys.stdout.getvalue(), "meow\nmeow\n")

    def test_dog_loud(self):
        animal = NoisyAnimal('dog')
        animal.make_noise()
        self.assertEqual(sys.stdout.getvalue(), "woof\nwoof\n")

    def test_leopard_loud(self):
        animal = NoisyAnimal('leopard')
        animal.make_noise()
        self.assertEqual(sys.stdout.getvalue(), "growl\ngrowl\n")

    def test_cat_quiet(self):
        animal = NoisyAnimal('cat')
        animal.make_noise(loud=False)
        self.assertEqual(sys.stdout.getvalue(), "meow\n")

    def test_dog_quiet(self):
        animal = NoisyAnimal('dog')
        animal.make_noise(loud=False)
        self.assertEqual(sys.stdout.getvalue(), "woof\n")

    def test_leopard_quiet(self):
        animal = NoisyAnimal('leopard')
        animal.make_noise(loud=False)
        self.assertEqual(sys.stdout.getvalue(), "growl\n")

    def test_owl_loud(self):
        animal = NoisyAnimal('owl')
        animal.make_noise()
        self.assertEqual(sys.stdout.getvalue(), "hoot\nhoot\n")

    def test_eagle_loud(self):
        animal = NoisyAnimal('eagle')
        animal.make_noise()
        self.assertEqual(sys.stdout.getvalue(), "caw\ncaw\n")

    def test_hadedah_loud(self):
        animal = NoisyAnimal('hadedah')
        animal.make_noise()
        self.assertEqual(sys.stdout.getvalue(), "squawk\nsquawk\n")

    def test_owl_quiet(self):
        animal = NoisyAnimal('owl')
        animal.make_noise(loud=False)
        self.assertEqual(sys.stdout.getvalue(), "hoot\n")

    def test_eagle_quiet(self):
        animal = NoisyAnimal('eagle')
        animal.make_noise(loud=False)
        self.assertEqual(sys.stdout.getvalue(), "caw\n")

    def test_hadedah_quiet(self):
        animal = NoisyAnimal('hadedah')
        with self.assertRaises(Exception) as context:
            animal.make_noise(loud=False)
        self.assertTrue('no such thing' in str(context.exception))

if __name__ == '__main__':
    unittest.main()

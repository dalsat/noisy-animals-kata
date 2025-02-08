# noisy_animal.py

class NoisyAnimal:
    def __init__(self, species):
        self.species = species

    def make_noise(self, loud=True):
        if self.is_bird() and not loud:
            self.make_bird_noise(False)
        if loud:
            if self.mammal_noise():
                for _ in range(2):
                    print(self.mammal_noise())
            if self.is_bird():
                self.make_bird_noise(True)
        elif self.species in ['cat', 'dog', 'leopard']:
            print(self.mammal_noise())

    def mammal_noise(self):
        return {
            'cat': 'meow',
            'dog': 'woof',
            'leopard': 'growl'
        }.get(self.species)

    def make_bird_noise(self, is_loud=True):
        if self.species == 'hadedah':
            print('squawk')
        elif self.species == 'eagle':
            print('caw')
        else:
            print('hoot')
        if is_loud:
            if self.species == 'owl':
                print('hoot')
            if self.species == 'eagle':
                print('caw')
            if self.species == 'hadedah':
                print('squawk')
        else:
            if self.species == 'hadedah':
                raise Exception('there is no such thing as a quiet hadedah!')

    def is_bird(self):
        return self.species in ['owl', 'eagle', 'hadedah']

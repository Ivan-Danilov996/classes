class Animal:
    weights = {}
    all_weight = 0
    most_weight = 0
    most_weight_name = ''

    def __init__(self, name, weight):
        self.weight = weight
        self.name = name
        self.add_weights()

    def feed(self):
        print(self.name, 'fed')

    def add_weights(self):
        self.weights[self.name] = self.weight

    def get_all_weigth(self):
        for name, weight in self.weights.items():
            self.all_weight += weight
        print(self.all_weight)

    def get_most_weigth(self):
        for name, weight in self.weights.items():
            if self.most_weight < weight:
                self.most_weight = weight
                self.most_weight_name = name
        print(self.most_weight_name, self.most_weight)


class Cloven_hoofed(Animal):
    def milk(self):
        print(self.name, 'milked')


class Bird(Animal):
    def collect_eggs(self):
        print(self.name, 'eggs harvested successfully')


class Goose(Bird):
    vote = 'krya'


class Cow(Cloven_hoofed):
    vote = 'moo'


class Goat(Cloven_hoofed):
    vote = 'be'


class Sheep(Cloven_hoofed):
    vote = 'be'

    def to_cut(self):
        print(self.name, 'tonsured')


class Chicken(Bird):
    vote = 'krya'


class Duck(Bird):
    vote = 'krya'


white = Goose('White', 5)
gray = Goose('Gray', 4)
manka = Cow('Manka', 500)
barashek = Sheep('Barashek', 30)
kudryavy = Sheep('Kudryavy', 30)
ko_ko = Chicken('Ko_ko', 2)
kukareku = Chicken('Kukareku', 1)
horns = Goat('Horns', 20)
hooves = Goat('Рooves', 25)
kryackva = Duck('Kryackva', 5)

white.feed()
manka.milk()
print(Animal.weights)
white.get_all_weigth()
white.get_most_weigth()
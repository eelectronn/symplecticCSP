class Alphabet:
    def __init__(self, num):
        self.num = num

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.num == other.num

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return not self < other and self != other

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other


class Ordinary(Alphabet):
    def __lt__(self, other):
        if isinstance(other, Barred):
            return True
        return self.num < other.num

    def __str__(self):
        return str(self.num)

    def clone(self):
        return Ordinary(self.num)

    __repr__ = __str__
    # def __repr__(self):
    #     return 'Ordinary('+str(self.num)+')'


class Barred(Alphabet):
    def __lt__(self, other):
        if isinstance(other, Ordinary):
            return False
        return self.num > other.num

    def __str__(self):
        return u'\u0305' + str(self.num)

    def clone(self):
        return Barred(self.num)

    __repr__ = __str__
    # def __repr__(self):
    #     return 'Barred('+str(self.num)+')'

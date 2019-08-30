"""
Module containing definition of Alphabet class
"""


class Alphabet:
    """
    This class defines the generalized alphabet and its behaviour.
    """
    def __init__(self, num):
        """
        Initialization function for Alphabet

        :type num: int
        :param num: Number that is to be decorated with a specific type of alphabet
        """
        self.num = num

    def __eq__(self, other):
        """
        Function to check equality of the two Alphabet objects, using ==

        :type other: Alphabet
        :param other: alphabet object that we are comparing with.
        :return: True if both alphabet object are equal, and False otherwise.
        """
        if type(self) != type(other):
            return False
        return self.num == other.num

    def __ne__(self, other):
        """
        Function to check inequality of two Alphabet objects, using !=

        :type other: Alphabet
        :param other: alphabet object that we are comparing with.
        :return: True if both alphabet object are not equal, and False otherwise.
        """
        return not self == other

    def __gt__(self, other):
        """
        Function to check invoker object is greater than the other Alphabet object, using >

        :type other: Alphabet
        :param other: alphabet object that we are comparing with.
        :return: True if invoker is greater than other, False otherwise.
        """
        return not self < other and self != other

    def __le__(self, other):
        """
        Function to check if invoker is less than or equal to the other Alphabet object, using <=

        :type other: Alphabet
        :param other: alphabet object that we are comparing with.
        :return: True if invoker is less than or equal to the other, False otherwise.
        """
        return self < other or self == other

    def __ge__(self, other):
        """
        Function to check if invoker is greater than of equal to the other Alphabet object, using >=

        :type other: Alphabet
        :param other: alphabet object that we are comparing with.
        :return: True if invoker is greater than or equal to the other, False otherwise.
        """
        return self > other or self == other


class Ordinary(Alphabet):
    """
    This class defines the Ordinary alphabet, which is a specialization of Alphabet.
    """
    def __lt__(self, other):
        """
        Function to check if invoker is less than the other Alphabet object, using <

        :type other: Alphabet
        :param other: alphabet object that we are comparing with.
        :return: True if invoker is less than the other, False otherwise.
        """
        if isinstance(other, Barred):
            return True
        return self.num < other.num

    def __str__(self):
        """
        Function to get the string representation of the Ordinary object.

        :return: string representation of invoking object.
        :rtype: str
        """
        return str(self.num)

    def clone(self):
        """
        Function to make a copy of the invoking Ordinary object.

        :return: Copy of invoking object
        :rtype: Ordinary
        """
        return Ordinary(self.num)

    __repr__ = __str__


class Barred(Alphabet):
    """
    This class defines the Barred alphabet, which is a specialization of Alphabet.
    """
    def __lt__(self, other):
        """
        Function to check if invoker is less than the other Alphabet object, using <

        :type other: Alphabet
        :param other: alphabet object that we are comparing with.
        :return: True if invoker is less than the other, False otherwise.
        """
        if isinstance(other, Ordinary):
            return False
        return self.num > other.num

    def __str__(self):
        """
        Function to get the string representation of the Barred object.

        :return: string representation of invoking object.
        :rtype: str
        """
        return u'\u0305' + str(self.num)

    def clone(self):
        """
        Function to make a copy of the invoking Barred object.

        :return: Copy of invoking object
        :rtype: Barred
        """
        return Barred(self.num)

    __repr__ = __str__

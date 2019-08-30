"""
This module contains definition of Tableau class.
"""


class Tableau:
    """
    This class defines a young tableau and provide functions to operate on it.
    """
    def __init__(self, body):
        """
        Initialization function for Tableau object.

        :param body: body of tableau.
        """
        for i in range(len(body)-1):
            if len(body[i]) < len(body[i+1]):
                raise Exception('invalid shape')
        self.body = body
        shape = []
        for row in body:
            shape.append(len(row))
        self.shape = shape
        self.shapeTranspose = Tableau.get_shape_transpose(self.shape.copy())

    @staticmethod
    def get_shape_transpose(shape):
        """
        Function to compute the transpose of a given shape.

        :param shape: shape for which we need to calculate transpose.
        :return: list representing transpose shape.
        :rtype: list
        """
        shape_transpose = []
        if len(shape) == 0:
            return shape_transpose
        while shape[0] > 0:
            count = 0
            for i in range(len(shape)):
                if shape[i] > 0:
                    count += 1
                    shape[i] -= 1
                else:
                    break
            shape_transpose.append(count)
        return shape_transpose

    def __str__(self):
        """
        Function to get string representation of the Tableau object.

        :return: string representation of the Tableau object.
        :rtype: str
        """
        string = ''
        for row in self.body:
            for entry in row:
                string += str(entry) + '\t'
            string += '\n'
        return string

    def add_new_box(self, i, element):
        """
        Function to add a new box at the end of a row.

        :param i: row index.
        :param element: element to be added in new box.
        :return: None
        """
        if len(self.body) <= i:
            self.body.append([])
            self.shape.append(0)
        self.body[i].append(element)
        self.shape[i] += 1
        if len(self.shapeTranspose) < self.shape[0]:
            self.shapeTranspose.append(0)
        self.shapeTranspose[len(self.body[i])-1] += 1

    def del_row_lastbox(self, i):
        """
        Function to delete the last box in the row.

        :param i: row index
        :return: None
        """
        j = self.shape[i]-1
        if len(self.body) >= i:
            if len(self.body[i]) >= j:
                temp = self.body[i][j]
                del self.body[i][j]
                if len(self.body[i]) == 0:
                    del self.body[i]
                self.shape[i] -= 1
                if self.shape[i] == 0:
                    del self.shape[i]
                self.shapeTranspose[j] -= 1
                if self.shapeTranspose[j] == 0:
                    del self.shapeTranspose[j]
                return {'bumped_element': temp}

    def clone(self):
        """
        Function to creat a copy of the invoking Tableau object

        :return: copy of invoking tableau object.
        :rtype: Tableau
        """
        body_copy = []
        for row in self.body:
            row_copy = []
            for entry in row:
                row_copy.append(entry.clone())
            body_copy.append(row_copy)
        return Tableau(body_copy)

    def __eq__(self, other):
        """
        Function to check if two Tableau object are same in the sense that they have same entries and same location for all location of boxes, using ==

        :param other: Tableau object with which invoking Tableau object is being compared.
        :return: True if both Tableau object are same. False otherwise.
        """
        if len(self.body) != len(other.body):
            return False
        for i in range(len(self.body)):
            if len(self.body[i]) != len(other.body[i]):
                return False
            for j in range(len(self.body[i])):
                if self.body[i][j] != other.body[i][j]:
                    return False
        return True

    def __ne__(self, other):
        """
        Function to check if two Tableau object are not same.

        :param other: :param other: Tableau object with which invoking Tableau object is being compared.
        :return: False if both Tableau object are same. True otherwise.
        """
        return not self == other

    def __hash__(self):
        return hash(str(self))

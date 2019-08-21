class Tableau:
    def __init__(self, body):
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
        string = ''
        for row in self.body:
            for entry in row:
                string += str(entry) + '\t'
            string += '\n'
        return string

    def add_new_box(self, i, element):
        if len(self.body) <= i:
            self.body.append([])
            self.shape.append(0)
        self.body[i].append(element)
        self.shape[i] += 1
        if len(self.shapeTranspose) < self.shape[0]:
            self.shapeTranspose.append(0)
        self.shapeTranspose[len(self.body[i])-1] += 1

    def del_row_lastbox(self, i):
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
        body = []
        for row in self.body:
            body.append(row.copy())
        return Tableau(body)

    def __eq__(self, other):
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
        return not self == other
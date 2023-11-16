class SparseMatrix:
    def __init__(self):
        self.matrix = {}
        self.rows = set()
        self.cols = set()

    def set(self, row, col, value):
        if value==0:
            raise ValueError("invalid value to set")
        elif value != 0:
            self.rows.add(row)
            self.cols.add(col)

            if row not in self.matrix:
                self.matrix[row] = {}

            self.matrix[row][col] = value
        elif row in self.matrix and col in self.matrix[row]:
            del self.matrix[row][col]
            if not self.matrix[row]:
                del self.matrix[row]
            if row in self.rows and not any(col in self.matrix[row] for row in self.rows):
                self.rows.remove(row)
            if col in self.cols and not any(col in self.matrix[row] for row in self.rows):
                self.cols.remove(col)

    def get(self, row, col):
        if row in self.matrix and col in self.matrix[row]:
            return self.matrix[row][col]
        else:
            return 0

    def recommend(self, vector):
        result = {}
        if not len(self.cols)==len(vector):
            raise ValueError("Columns and Vector length should be equal")
        for row in self.rows:
            total = 0
            for col in self.cols:
                total += self.get(row, col) * vector[col]
            result[row] = total
        return result

    def add_movie(self, matrix):
        for row, cols in matrix.matrix.items():
            for col, value in cols.items():
                self.set(row, col, value)
    def display(self):
        for row, cols in self.matrix.items():
            for col, value in cols.items():
                print(f"({row}, {col}): {value}")

    def to_dense(self):
        max_row = max(self.rows)
        max_col = max(max(self.cols), max((col for row in self.matrix for col in self.matrix[row])))
        dense_matrix = [[0 for _ in range(max_col + 1)] for _ in range(max_row + 1)]

        for row, cols in self.matrix.items():
            for col, value in cols.items():
                dense_matrix[row][col] = value

        return dense_matrix
spmat=SparseMatrix()
spmat.set(2,1,1)
spmat.display()


    
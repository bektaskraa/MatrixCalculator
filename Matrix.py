class Matrix:
    def __init__(self,matrix:list=None):
        if matrix!=None:
            self.matrix = matrix
            self.rows = len(matrix)
            self.cols = len(matrix[0])

    def create_matrix(self,row,col):
        self.matrix = []
        for i in range(row):
            _row = []
            for j in range(col):
                _row.append(0)
            self.matrix.append(_row)
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])
    def get_rows(self):
        return self.matrix
    def get_columns(self):
        columns = []
        rowColumn = []
        for i in range(self.cols):
            for row in self.matrix:
                rowColumn.append(row[i])
            columns.append(rowColumn)
            rowColumn = []
        return columns
    def print_matrix(self):
        for row in self.matrix:
            print(row)

def add(Matrix1:Matrix,Matrix2:Matrix):
    if Matrix1.rows == Matrix2.rows and Matrix1.cols == Matrix2.cols:
        result = Matrix()
        result.create_matrix(Matrix1.rows,Matrix1.cols)
        for i in range(result.rows):
            #print("index:",i,"r->",result.matrix[i],"m1->",Matrix1.matrix[i],"m2->",Matrix2.matrix[i])
            for j in range(Matrix1.cols):
                result.matrix[i][j] = Matrix1.matrix[i][j] + Matrix2.matrix[i][j]
        return result
    else:
        print("Error(add): Matris boyutları eşleşmiyor")
import numpy as np

class SquareMatrixCreator:
    def create_matrices(self):
        n = int(input("Enter the number of rows/columns you want to have: "))

        if input("Do you want to create the matrix manually? Type Y for Yes and N for No: ").strip().upper() == 'Y':
            matrix1 = self.create_matrix_manually(n, n)
            matrix2 = self.create_matrix_manually(n, n)
        else:
            matrix1 = self.create_random_matrix(n, n)
            matrix2 = self.create_random_matrix(n, n)
        
        return matrix1, matrix2

    def create_random_matrix(self, row, column):
        return np.random.randint(low=1, high=101, size=(row, column))

    def create_matrix_manually(self, row, column):
        matrix = []
        for i in range(row):
            row_data = []
            for j in range(column):
                value = int(input(f"Enter value for element ({i},{j}): "))
                row_data.append(value)
            matrix.append(row_data)
        return np.array(matrix)


class strassenAlg:
         
    def Strassen(self ,matrixA, matrixB):
        if len(matrixA)<=2:
            return self.bruteForceMultiply(matrixA , matrixB)
        a , b , c ,d = self.Split(matrixA)
        e , f , g , h =   self.Split(matrixB)  
        p1 =self.Strassen(a + d,e + h)
        p2 =self.Strassen( d ,g -e)
        p3 =self.Strassen(a + b,h)
        p4 =self.Strassen(b- d,g+h)
        p5 =self.Strassen(a,f- h)
        p6 =self.Strassen(c + d,e)
        p7 =self.Strassen(a - c,e + f)
        c11 = p1 + p2 - p3 + p4
        c12 = p5 + p3
        c21 = p6 + p2
        c22 = p5 + p1 -p6 -p7
        
        upper_half = np.hstack((c11, c12))
        lower_half = np.hstack((c21, c22))

        return np.vstack((upper_half, lower_half))
                                                                        
    def Split(self, matrix):
        length = matrix.shape[0]
        mid = length // 2
        return matrix[:mid, :mid], matrix[:mid, mid:], matrix[mid:, :mid], matrix[mid:, mid:]
    
    def bruteForceMultiply(self ,matrixA , matrixB):
        rowsA, colsA = matrixA.shape
        rowsB, colsB = matrixB.shape
    
        result = np.zeros((rowsA, colsB))

        for i in range(rowsA):
            for j in range(colsB):
                for k in range(colsA):
                    result[i, j] += matrixA[i, k] * matrixB[k, j]     
        return result


    def StartFixedStrassen(self ,matrixA , matrixB):
        lenght = len(matrixA)
        x = np.log2(lenght)
        if x.is_integer() == False:
            x = np.ceil(x)
            padded_matrixA = np.pad(matrixA, ((0, 2**int(x) - lenght), (0, 2**int(x) - lenght)), mode='constant')
            padded_matrixB = np.pad(matrixB, ((0, 2**int(x) - lenght), (0, 2**int(x) - lenght)), mode='constant')
            return self.Strassen(padded_matrixA , padded_matrixB)
        return self.Strassen(matrixA , matrixB) 
            
        
        
matrix_creator = SquareMatrixCreator()
matrix1, matrix2 = matrix_creator.create_matrices()

strassenalg = strassenAlg()
finalMatrix = strassenalg.StartFixedStrassen(matrix1, matrix2)
print("Matrix 1:")
print(matrix1)
print("Matrix 2:")
print(matrix2)

finalMatrix = finalMatrix.astype(int)
print("Final Matrix (Integers):")
print(finalMatrix)

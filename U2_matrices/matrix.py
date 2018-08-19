import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
        
        trace_sum = 0
        for i in range(self.h):
            trace_sum += self.g[i][i]
        
        return trace_sum
    
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        if(self.h == 1 and self.w == 1):
            """
            for 1x1 case:
            
            a
            
            simply return 1/a
            """
            self.g[0][0] = 1.0/self.g[0][0]
            return self
        elif(self.h == 2 and self.w == 2):  
            """
            for 2x2 case:
            
            a  b 
            c  d
            
            determinant = a*d - b*c
            """
            det = self.g[0][0]*self.g[1][1]-self.g[0][1]*self.g[1][0]
            """
            swap a and d.
            """
            tmp = (1.0/det)*self.g[0][0]  
            self.g[0][0] = (1.0/det)*self.g[1][1]
            self.g[1][1] = tmp
            """
            flip signs for c and d
            """
            self.g[0][1] = -(1.0/det)*self.g[0][1]
            self.g[1][0] = -(1.0/det)*self.g[1][0]
            return self
        
        else:
            return None
        

    def T(self):
        """
        
        Returns a transposed copy of this Matrix.
    
        """
        t_matrix = Matrix([[0.0 for _ in range(self.h)] for __ in range(self.w)])
        
        """
        intialize flipped matrix and flip around i and j
        
        """
        for i in range(self.h):
            for j in range(self.w):
                t_matrix.g[j][i] = self.g[i][j]
        
        return t_matrix
        
    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        
        matrix_sum = Matrix([[0.0 for _ in range(self.w)] for __ in range(self.h)])
        
        for i in range(self.h):
            for j in range(self.w):
                matrix_sum.g[i][j] = self.g[i][j] + other.g[i][j]

        return matrix_sum
    
    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        neg_matrix = Matrix([[0.0 for _ in range(self.w)] for __ in range(self.h)])
        
        for i in range(self.h):
            for j in range(self.w):
                neg_matrix.g[i][j] = -self.g[i][j]
        
        return neg_matrix
    
    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        
        matrix_sub = Matrix([[0.0 for _ in range(self.w)] for __ in range(self.h)])
        
        for i in range(self.h):
            for j in range(self.w):
                matrix_sub.g[i][j] = self.g[i][j] - other.g[i][j]

        return matrix_sub

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        if(self.w != other.h):
            return None
        else:
            new_matrix = Matrix([[0.0 for _ in range(other.w)] for __ in range(self.h)])
            """
            use one iterator for: 
            col of left & 
            row of right      
                           (l.w)        
                            a  b         (r.w)
                            c  d         a   b   c
                      (l.h) e  f         d   e   f  (r.h)     since l.w === r.h
            """
            for i in range(self.h): 
                for h in range(other.w):
                    for j in range(self.w):
                        #print("first: " + str(self.g[i][j]))
                        #print("second: " + str(other.g[j][h]))
                        new_matrix.g[i][h] += self.g[i][j]*other.g[j][h]
                    
        return new_matrix

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            for i in range(self.h):
                for j in range(self.w):
                    self.g[i][j] = other*self.g[i][j]
        else:
            raise(ValueError, "can only multiply numbers and matrices") 

        return self
            

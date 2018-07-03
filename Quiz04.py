#Gerardo Rattia
#Math 4330 - Quiz04


def ScaVecMulti(scalar, vector01):
  """
    This function takes a vector an a scalar as it’s arguments, and then it multiplies each element of the vector by the scalar, updating each element of the vector. 
  """  
  vector = []
  for i in range(len(vector01)):
    total = 0
    total += vector01[i] * scalar
    vector.append(total)
  return vector

def VecSub(vector01, vector02):
  """
    This function takes two vectors as its arguments, then it updates each of the elements inside the vector by subtracting them, returning a new updated vector.
  """
  VecSub = []
  for i in range(len(vector01)):
    total = 0
    total += vector01[i] - vector02[i]
    VecSub.append(total)
  return VecSub

def dot(vector01, vector02):
  """
    This function takes two vectors as its arguments. It multiplies each element of each vector before adding them, and returning the dot product of two 
    vectors as a scalar.
  """
  total = 0
  for i in range(len(vector01)):
    total += vector01[i] * vector02[i]
  return total


def norm(vector):
  """
  The two norms takes a vector as it's arguments, to compute the sum of the squares of each element of the vector, returning the square root of the sum.
  """
  total = 0
  for i in range(len(vector)):
    total += vector[i] ** 2
  total = total**(1/2)
  return total

def normalize(vector):
  """
  This function takes the infinity norm and uses it to normalize a vector, Returning a normalize vector with respect to the infinity norm.
  """
  normalizer = []
  for i in range(len(vector)):
    total = 0
    total += vector[i] * (1 / norm(vector))
    normalizer.append(total)
  return normalizer  

A = [[1, 2, 3], [1, 2, -4]]

def GramSchmidt(A):
  """
  The modified Gram-Schmidt algorithm takes a comlimn vector inside a matrix and computes orthonormal vectors. Q and R are returned after being substracted from the original matrix
  """

  n = len(A)
  m = len(A[0])
  Q = [[0] * m for i in range(n)]
  R = [[0] * n for i in range(n)]
  v = [[0] * m for i in range(n)]
  # Dimention of R and Q must match for the multiplication

  for i in range(n):
    v[i] = A[i]
  for i in range(n):
    R[i][i] = norm(v[i])
    # Taking two norm
    Q[i] = normalize(v[i])
    # normalizing 
    for j in range(i + 1, n):
      R[i][j] = dot(Q[i],v[j])
      # dot product 
      temp = ScaVecMulti(R[i][j], Q[i])
      # vector scalar multiplication
      v[j] = VecSub(v[j],temp)
      # vector substraction
  return [Q, R]

output = GramSchmidt(A)
print(output[0])
print(output[1])

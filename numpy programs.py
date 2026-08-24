#import numpy as np
# coefficient matrix
#A=np.array([[2,3],[1,1]])
#constant matrix
#B=np.array([8,3])
#solution=np.linalg.solve(A,B)
#print("solution is")
#print("x is",solution[0])
#print("y is",solution[1])

#import numpy as np
#coefficient matrix
#A=np.array([[3,1,3],[2,3,1],[1,1,2]])
#constant matrix
#B=np.array([11,10,7])
#solution=np.linalg.solve(A,B,)
#print("solution is")
#print("x is",solution[0])
#print("y is",solution[1])
#print("z is",solution[2])

#import numpy as np
#coefficient matrix
#A=np.array([[3,1,3],[2,3,1]])
#constant matrix
#B=np.array([11,10])
#solution=np.linalg.lstsq(A,B)
#print("solution is")
#print("x is",solution[0])
#print("y is",solution[1])
#print("z is",solution[2])

import numpy as np
#coefficient matrix
A=np.array([[3,1,3],[2,3,1]])
#constant matrix
B=np.array([11,10])
solution=np.linalg.lstsq(A,B,rcond=None)[0]
print("solution is")
print("x is",solution[0])
print("y is",solution[1])
print("z is",solution[2])
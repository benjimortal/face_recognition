import numpy as np
import random


np.random.seed(seed=60)
random_square = np.random.rand(5,5)
print(random_square)

print('first ROW====>>>>',random_square[0])

print('first COLUM====>>>>',random_square[:,0])
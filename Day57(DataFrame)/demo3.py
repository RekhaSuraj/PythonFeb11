import numpy as np
import pandas as pd
# 3. From a 2D array

n1 = np.array([[1,'Aparna'],[2,'Vittal'],[3,'Rama']])
s1 = pd.DataFrame(data=n1,columns=['id','Name'])
print(s1)

#   id    Name
# 0  1  Aparna
# 1  2  Vittal
# 2  3    Rama



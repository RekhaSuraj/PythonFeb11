import pandas as pd
# print(help(pd.Series))
# Series(data=None, index=None, dtype: 'Dtype | None' = None, name=None, copy: 'bool | None' = None,
# fastpath: 'bool | lib.NoDefault' = <no_default>) -> 'None'
# One-dimensional ndarray with axis labels (including time seri
# es).

dict1 = {'Name':'Rama',
         'Age':25,
         'Country':'India',
         'Job':'IT'
         }

print(pd.Series(dict1))

# Name        Rama
# Age           25
# Country    India
# Job           IT
# dtype: object


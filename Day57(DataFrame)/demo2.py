import pandas as pd
# 2. From a list of dictionaries

s2 = pd.DataFrame(
    [
        {'Name':'Aparna','Age':25,'Location':'IND'},
        {'Name':'Vittal','Age':26,'Location':'UK'}
    ]
)

print(s2)

#      Name  Age Location
# 0  Aparna   25      IND
# 1  Vittal   26       UK

print()

# Missing values will be automatically filled with Nan, Here Location is missing for 'Vittal' which is
# filled with Nan
s3 = pd.DataFrame(
    [
        {'Name':'Aparna','Age':25,'Location':'IND'},
        {'Name':'Vittal','Age':26,}
    ]
)

print(s3)

#      Name  Age Location
# 0  Aparna   25      IND
# 1  Vittal   26      NaN
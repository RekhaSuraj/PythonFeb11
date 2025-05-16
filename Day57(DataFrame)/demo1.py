import pandas as pd
# DataFrames:
#
# A DataFrame is a 2-dimensional, labeled data structure in Pandas, similar to a spreadsheet or SQL table.
# Rows → identified by index
# Columns → labeled with column names
# Each column can have a different data type

# How to Create a DataFrame
# 1. From a Dictionary of Lists

s1 = pd.DataFrame(
    {
        'id':[1,2,3,4,5],
        'Name':['Aparna','Vittal','Rama','Seetha','Krishna']

    }
)

print(s1)

#    id     Name
# 0   1   Aparna
# 1   2   Vittal
# 2   3     Rama
# 3   4   Seetha
# 4   5  Krishna


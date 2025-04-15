# Slicing - Fetching a part from a string
# Syntax : [start:stop:step]
# start : The index from where you want to fetch the string, default start value is 0
# stop : Till where you want to fetch, default value is n
# step : Jumps, default step value is 1

str1 = 'Happiness is everything'

# Fetch Happi from the above string
print(str1[0:5:1])
# Happi

# Wthout starting values
print(str1[:5:])
# Happi

# Fetch is from the above string
print(str1[10:12])

# Without ending values
print(str1[5:])
# ness is everything

# Fetch 'thing' from the above string
print(str1[18:])

# Jump using step 2
print(str1[::2])
# Hpiesi vrtig

# Without specifying any values
print(str1[::])
# Happiness is everything
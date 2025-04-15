import time

t1 = time.localtime()
print(t1)
print(type(t1))
# <class 'time.struct_time'>

# Returns time in string format
t_format = time.strftime('%y-%m-%d %a-%A',t1)
print(t_format)
print(type(t_format))
# <class 'str'>

t_asc = time.asctime()
print(t_asc)
# Mon Apr 14 10:27:42 2025

print(type(t_asc))
# <class 'str'>
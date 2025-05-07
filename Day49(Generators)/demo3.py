def fun1():
    yield 10
    yield 20
    yield 30
    yield 40
    yield 50
    yield 60


ob1 = fun1()
print(next(ob1))

print(ob1.__next__())
# 10
# 20
print('start from next value')
for i in ob1:
    print(i)


# 10
# 20
# start from next value
# 30
# 40
# 50
# 60



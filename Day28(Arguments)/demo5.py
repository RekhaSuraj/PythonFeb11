# 2. Using **kwargs (Multiple Keyword Arguments)
# ✅ Allows a function to accept any number of keyword arguments.
# ✅ Collects them into a dictionary.

def profile(**kwargs):
    print(kwargs)
    for k in kwargs.items():
        print(k)


profile(name='Test',age=25,salary=20000)
# {'name': 'Test', 'age': 25, 'salary': 20000}
# ('name', 'Test')
# ('age', 25)
# ('salary', 20000)
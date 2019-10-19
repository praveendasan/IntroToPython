x = 6
y = 0
try:
    print(x/y)
except ZeroDivisionError as e:
    print('cant divide by zero')
else:
    print('something else went wrong')
finally:
    print('this is our cleanup code')
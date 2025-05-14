#Grades
check_grade = lambda grade: 'you got an A' if grade >=90 else 'did not got an A'
add_func = lambda *num: sum(num)
sub_func = lambda num1, num2: num1 - num2
print(add_func(5,9))
def add(*num):
    c=0
    for i in num:
        c += i
    return c
print(add(5,2,6))
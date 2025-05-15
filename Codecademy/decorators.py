
def print_title(print_some_name_function):
    def wrapp(*name):
        print('Student:')
        print_some_name_function(name)
    return wrapp
@print_title
def print_my_name(*name):
    print(name)

def print_random_name():
    print('Maria')

print_my_name('Jake', 'Maria')

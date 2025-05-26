# polymorphism and Liskov substitution
class Animal:
    def to_feed(self):
        print('The animal is eating')

class Dog(Animal):
    def bark(self):
        print('The dog is barking')

class Cat(Dog):
    def mew(self):
        print('mew')
    def bark(self):
        raise Exception ('Cat doesnt bark') #Quebra da substituição de liskov, pois Dog não pode ser substituido por Cat sem afetar a execução do programa
    

obj1 = Animal()
obj2 = Dog()
obj3 = Cat()

obj1.to_feed()
obj2.bark()
obj3.bark()

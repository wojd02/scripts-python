from abc import ABC , abstractmethod 
class worker(ABC): #Vai ser uma interface
    @abstractmethod
    def work(self) -> None:
        pass
    @abstractmethod
    def lunch(self) -> None:
        pass
    @abstractmethod
    def go_home(self) -> None:
        pass

class architect:
    def work(self) -> None:
        print('The architect is working')
    def lunch(self) -> None:
        print('The architect is lunching')
    def go_home(self) -> None:
        print('The architect is going to home')

class cook:
    def work(self) -> None:
        print('The cook is working')
    def lunch(self) -> None:
        print('The cook is lunching')
    def go_home(self) -> None:
        print('The cook is going to home')

def call_worker (the_worker : worker):
    the_worker.work()
    print(f'Calling the worker')
    the_worker.go_home()

people1 = architect()
people2 = cook()

call_worker(people1)

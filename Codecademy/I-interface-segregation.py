from abc import ABC , abstractmethod 
class worker(ABC): #Vai ser uma interface
    @abstractmethod
    def work(self) -> None:
        pass
    @abstractmethod
    def lunch(self) -> None:
        pass
    @abstractmethod
    def benefits(self) -> None:
        pass
class temp_worker(ABC):
    @abstractmethod
    def work(self) -> None:
        pass
    @abstractmethod
    def lunch(self) -> None:
        pass

class architect:
    def work(self) -> None:
        print('The architect is working')
    def lunch(self) -> None:
        print('The architect is lunching')
    def benefits(self) -> None:
        print('The architect is consulting his benefits')

class cook:
    def work(self) -> None:
        print('The cook is working')
    def lunch(self) -> None:
        print('The cook is lunching')
    def benefits(self) -> None:
        print('The cook is consulting his benefits')

class substitute_cook(worker): #Quebra da segregação de interface (solução: criar uma nova interface para trabalhadores temporários e tirar a parte dos beneficios)
    def work(self) -> None:
        print('The substitute cook is working')
    def lunch(self) -> None:
        print('The substitute cook is lunching')

def call_worker (the_worker : worker):
    the_worker.work()
    print(f'Calling the worker')
    the_worker.lunch()

people1 = architect()
people2 = substitute_cook()

call_worker(people2)
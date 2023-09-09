""" 
    Interface Segregation Principle (ISP):
This principle states that clients should not be forced to depend on interfaces 
they do not use. In Python, you can create smaller, 
more focused interfaces instead of large, monolithic ones to avoid unnecessary dependencies._summary_
"""

from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

class Eater(ABC):
    @abstractmethod
    def eat(self):
        pass

class Engineer(Worker):
    def work(self):
        print("Engineer is working")

class Chef(Worker, Eater):
    def work(self):
        print("Chef is working")

    def eat(self):
        print("Chef is eating")

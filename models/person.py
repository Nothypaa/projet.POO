from abc import ABC, abstractmethod

class Person(ABC):
    """
    Abstract Person class with basic attributes.
    This demonstrates the Abstraction OOP principle.
    """

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age
    
    @age.setter  
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("age cannot be negative")

    @abstractmethod
    def get_details(self):
        """Abstract method that must be implemented by subclasses"""
        pass
"""
Name: Mejares Ebes
Date: 
Assignment 3: Vehichle Class
Description: This is the Vehicle Class which will act as the Parent    
"""

from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    def __init__(self, model = '', colour = '', speed = 0.0, position = 0):
        super().__init__()
        self.__model = model
        self.__colour = colour
        self.__speed = speed
        self.__position = position

    # get methods
    @property
    def model(self):
        """
        Returns:
            str: the car's model
        """
        return self.__model
    
    @property
    def colour(self):
        """
        Returns:
            str: the car's colour
        """
        return self.__colour
    
    @property
    def speed(self):
        """
        Returns:
            float: the car's speed
        """
        return self.__speed
    
    @property
    def position(self):
        """
        Returns:
            int: the car's position
        """
        return self.__position

    def get_position_int(self):
        """
        Returns:
            int: the car's position that had been turned to int
        """
        return int(self.position)
    
    # set methods
    def set_position(self, value):
        """
        It set the car's position
        Args:
            value (float): the position being assigned a new value
        """
        self.__position = value
    
    def set_speed(self, value):
        """
        It set the car's speed
        Args:
            value (float): the speed being assign a new value
        """
        self.__speed = value
        
    def move(self):
       """
       It adds the car position and speed and assigned sum as the new position 
       """
       self.set_position(self.position + self.speed)
    
    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def get_icon(self):
        pass    

    # other dunder methods
    def __repr__(self):
        """
        It output all the data of each car
        Returns:
            str: all info about the car
        """
        return f'Model: {self.__model}, Colour: {self.__colour}, Speed: {self.__speed:.2f}, Position: {self.get_position_int()}'
    
    def __str__(self):
        """
        It output 
        Returns:
            str: info about the model and the 
        """
        return f'{self.__model} {self.__colour}'
    
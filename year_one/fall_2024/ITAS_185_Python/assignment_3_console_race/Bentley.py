"""
Name: Mejares Ebes
Date: 
Assignment 3: Bentley Class
Description: This is the Bentley Class which will act as the Child of the Vehicle Class    
"""

import Vehicle as v

class Bentley(v.Vehicle):
    
    def __init__(self, model = '', colour = '', speed = 0.0, position = 0, is_two_motor = False):
        super().__init__(model, colour, speed, position)
        self.__is_two_motor = is_two_motor
        
    def accelerate(self):
        """
        it add the accel speed of .6 to the current speed
        if the car has two motor, the accel speed added is d.8
        Returns:
            float: idk what it does but thats what the instruction told me to do
        """
        
        # go to BMW.py for explanation on why this code of block look like this
        true_or_false_turned_to_str = str(self.__is_two_motor)
        
        match true_or_false_turned_to_str:
            case 'True':
                new_speed = self.speed + .8
                self.set_speed(new_speed)
                return super().accelerate()   
            case 'False':
                new_speed = self.speed + 0.6
                self.set_speed(new_speed)
                return super().accelerate()           
    
    def get_icon(self):
        """
        Returns:
            str return the Letter B as the icon
        """
        return 'B'
    
    def __str__(self):
        return f'Bentley {super().__str__()}'
    
    def __repr__(self):
        return f'(Car Brand: Bentley, {super().__repr__()}, Is_Two_Motor: {self.__is_two_motor})'
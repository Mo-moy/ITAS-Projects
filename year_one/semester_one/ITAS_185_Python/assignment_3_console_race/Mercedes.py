"""
Name: Mejares Ebes
Date: 
Assignment 3: Mercedes Class
Description: This is the Mercedes Class which will act as the Child of the Vehicle Class    
"""

import Vehicle as v

class Mercedes(v.Vehicle):
    
    def __init__(self, model = '', colour = '', speed = 0.0, position = 0):
        super().__init__(model, colour, speed, position)
        
    def accelerate(self):
        """
        it add the accel speed of .75 to the current speed
        Returns:
            float: idk what it does but thats what the instruction told me to do
        """
        new_speed = self.speed + .75
        self.set_speed(new_speed)
        return super().accelerate()
        
    def get_icon(self):
        """
        Returns:
            str return the Letter M as the icon
        """
        return 'M'
    
    def __str__(self):
        return f'Mercedes {super().__str__()}'
    
    def __repr__(self):
        return f'(Car Brand: Mercedes, {super().__repr__()})'
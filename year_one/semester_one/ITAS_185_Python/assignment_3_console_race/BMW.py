"""
Name: Mejares Ebes
Date: 
Assignment 3: BMW Class
Description: This is the BMW Class which will act as the Child of the Vehicle Class    
"""

import Vehicle as v

class BMW(v.Vehicle):
    
    def __init__(self, model = '', colour = '', speed = 0.0, position = 0, is_turbo = False):
        super().__init__(model, colour, speed, position)
        self.__is_turbo = is_turbo
        
    def accelerate(self):
        """
        it add the accel speed of .5 to the current speed
        if the car has turbo, the accel speed added is .6
        Returns:
            float: idk what it does but thats what the instruction told me to do
        """
        
       # i used to have an if-else with if self.__is_turbo, but somehow the if-else in not detecting the True boolean from the cars even I could print it in thi method as well
       # so all accel speed value is coming from else: even if the car is is_turbo = True, so i struggle trying to fix this and just move on with the other stuff and come back to this later on,
       # so i come back to this and decided to test if other attributes works in the if-else, the first i test was the colours and i test if 'Red' and 'Purple',(the colour of the BMW cars in vehicle1.txt)
       # sp i put those two colours in a switch statement and miraculously actually work since the two BMW has a different speed to each other, and no longer have to see have the same speed ever again,
       # so i search up how to turn a bool into a string, and replace the colour in the switch statement wth ' True' and 'False, i no longer bother trying to learn why the boolean didnt work since all it did was give me pain
        true_or_false_turned_to_str = str(self.__is_turbo) 
        
        match true_or_false_turned_to_str:
            case ' True': # need a space in the front or it doesnt work, idk why
                new_speed = self.speed + .6
                self.set_speed(new_speed)
                return super().accelerate()   
            case 'False':
                new_speed = self.speed + 0.5
                self.set_speed(new_speed)
                return super().accelerate()                             
       
    def get_icon(self):
        """
        Returns:
            str return the Letter B as the icon
        """
        return 'B'
    
    def __str__(self):
        return f'BMW {super().__str__()}'
    
    def __repr__(self):
        return f'(Car Brand: BMW, {super().__repr__()}, Is_Turbo: {self.__is_turbo})'
    
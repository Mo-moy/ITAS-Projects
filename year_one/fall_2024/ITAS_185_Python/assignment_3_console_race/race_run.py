"""
Name: Mejares Ebes
Date: 
Assignment 3: Race Run
Description:   
"""
# vehicles and racetrack classes
import Vehicle as v
import Mercedes as m
import Bentley as b
import BMW as bm
import Racetrack as r

# other impport
import random
import os

def read_file(filename):
    """
    this function read the txt file then use a switch case to assign each car info in each line to the car list
        
    Args:
        filename (str): the validated file name
    """
    race_cars = [] 
    
    try:
        position_count = 0
        with open(filename, 'r') as file:
            read_info = [_.strip().split(',') for _ in file.readlines()]
            for line in read_info:
                car_brand = line[0] # assign car_brand either Mercedes, BMW or Bentley since they are the first word in each line of the txt file so the switch case 
                
                match car_brand:
                    case 'Mercedes':
                        if len(line) >= 3:
                            car = m.Mercedes(line[1], line[2], 1.0, position_count) # this create a car with Mercedes class stuff with (model, colour, intial speed, and position which is 0)
                            race_cars.append(car)
                                
                    case 'BMW':
                        if len(line) >= 4:
                            car = bm.BMW(line[1], line[2], 1.0, position_count, line[3]) # same thing with Mercedes with the addition of a boolean: is_turbo
                            race_cars.append(car)
                                            
                    case 'Bentley':
                        if len(line) >= 4:
                            car = b.Bentley(line[1], line[2], 1.0, position_count, line[3]) # same thing with Mercedes with the addition of a boolean: is_two_motor
                            race_cars.append(car)
     
    except TypeError as e:
        print(f"Missing Parameter: {line[0]}'s {e}") # this check is a car is missing a parameter in the txt file
    
    except PermissionError:
        print(f'Error: you do not have permission to read {filename}')        
        
    except KeyboardInterrupt:
        print('\nUser has exit the Program')
        exit(0)    
    
    except Exception as e:
        print(f'\nAn unexpected error occured: {e}')
    
    else:
        return race_cars

def validate_file():
    """
    this function is used to validate the txt file and also exit
    Raises:
        FileNotFoundError: check if the file does exist or not

    Returns:
        it return a string of the filename  
    """
    while True:
        try:            
            filename = input('Enter the filename [Press [q]/[Q] or [CTRL + c] to exit the Program]: ') 
            
            if filename.lower() == 'q':
                raise KeyboardInterrupt
            
            if not os.path.isfile(filename):
                raise FileNotFoundError 
         
        except FileNotFoundError:
            print(f'The file {filename} does not exist.\nPlease Try Again')    
        
        except KeyboardInterrupt:
            print('User has exit the Program')
            exit(0)
            
        except Exception as e:
            print(f'\nAn unexpected error occured: {e}')
        
        else:
            return filename          

def get_race_track():
    """
    this ask the user for the track info
    Raises:
        ValueError: trigger when the track's length is below or equal 1
        TypeError: trigger when the track's length is not an integer
        TypeError: trigger if the track's name is empty

    Returns:
        variable: the racetrack info
    """
    while True:
        try:
            # track
            track_length = input('Input the length of the Track: ')
            
            if int(track_length) <= 1:
                raise ValueError(f'The Race Track should be longer than : {track_length}')
            
            if not track_length.isdigit():
                raise TypeError(f'Invalid Input: {track_length}\nPlease input an integer')    
            
            # track name
            track_name = input('Input the Track Name: ')
                        
            if track_name == '':
                raise TypeError('Track name is empty')
        
        except TypeError as e:
            print(e)
        
        except ValueError as e:
            print(e)
        
        except KeyboardInterrupt:
            print('User has exit the Program')
            exit(0)
            
        except Exception as e:
            print(f'\nAn unexpected error occured: {e}')
            
        else:
            racetrack = r.Racetrack(track_name, int(track_length))
            return racetrack
        
def random_event(car_list):
    """
    this will randomly boost or reduce the car's speed or does nothing
    Args:
        car_list (list): the car-'s list
    """
    random_speed = [.2, .3, .4, .5, 1.0] # a list of speed boost or speed reduction
    
    for car in car_list:
        choice = random.randint(1, 3) # it assign a random num from 1-3 to see if a car is gettin a boost, a reduction, or nothing 
        
        match choice:
            # for random speed boost
            case 1:
                speed_boost = car.speed + random.choices(random_speed, weights = [5, 4, 3, 2, 1], k = 1)[0]
                car.set_speed(speed_boost)
            # for random speed deduction
            case 2:  
                speed_reduct = car.speed - random.choices(random_speed, weights = [5, 4, 3, 2, 1], k = 1)[0]                 
                car.set_speed(speed_reduct)
            # car is spared from the random
            case 3:
                pass
            
def check_winner(racetrack, car_list):   
    """
    this check if any car pash the finish line,
    if its True it will call the champion method from Racetrack Class and return True
    if its False, it just return as False
    Args:
        racetrack (variable): the racetrack info
        car_list (list): lists of cars

    Returns:
        bool: if the race is finish is True or False
    """
    is_finish = False
    
    # for the race_table, also i could get the winner from here since i keep getting issue of the first car in the txt file being shown as the winner
    sorted_list = sorted(car_list, key = lambda car: car.get_position_int(), reverse = True)
    
    for car in car_list:
        if car.get_position_int() >= racetrack.length: # detect if the car's position is equal or higher than the track length
            is_finish = True # now the race is finish
            print(racetrack.race_table(sorted_list)) # print the race table to check each car info to know their position and speed
            racetrack.champion(sorted_list[0]) # print the thropy and congrats msg
            return is_finish 

    return is_finish 
        
def race_update(car_list):
    """
    this uses a for loop to use the accelerate and move method to update the speed and the position of each car
    Args:
        car_list (list): lists of car
    """
    for car in car_list:
        car.accelerate()
        car.move()

def set_race_track(racetrack, car_list):
    """
    it first output a sign board for the race name,
    then initialize variables for the while loop( round_count to check the rounds, and is_finish to keep looping until True),
    then there is a while loop that calls upon few functions, with display the race rounds first and increment round_count by 1, 
    then the track, do the random speed stuff, then update speed and pos for each car, and lastly check if a car has passed the finish line
    Args:
        racetrack (variable): the race track
        car_list (list): list of cars
    """
    # print the race track name adn the border
    print(f"\n{'|' * 10}{'|' * len(racetrack.name)}{'|' * 10}")
    print(f"{'|' * 3}{' ' * 7}{racetrack.name}{' ' * 7}{'|' * 3}")
    print(f"{'|' * 10}{'|' * len(racetrack.name)}{'|' * 10}\n")
    
    # initialize vars for the while loop
    round_count = 1
    is_finish = False 
    
    while is_finish == False: # if is_finish is True that race will end
        print(f'\nRace Round[{round_count}]\n')
        round_count += 1        
        print(racetrack.__str__(car_list))
        random_event(car_list)
        race_update(car_list)
        is_finish = check_winner(racetrack, car_list)
    

def main():
    """
    bunch of functions to make the race run to work, also make it easier to start
    """
    car_file = validate_file()    
    car_list = read_file(car_file)
    racetrack = get_race_track()
    set_race_track(racetrack, car_list)    
    
if __name__ == "__main__":
    main()
    
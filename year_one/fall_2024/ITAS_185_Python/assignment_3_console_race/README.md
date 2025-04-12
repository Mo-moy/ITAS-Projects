# Racing Game

This is the final project in my Introduction to Python Course.
This project is to make a race in the console, the way the race progress is through a round system. For the car to overtake each other, each brand has a constant accelerate value, and a unique boost such as two motor or turbo. There is also a random function that either add speed or lower to ensure the winner are not the same one everytime.

This project consist of 9 files:
- Vehicle.py - the parent class of Bentley.py, Mercedes.py, and BMW.py. 
    - Bentley.py - child class of Vehicle.py 
    - Mercedes.py - child class of Vehicle.py
    - BMW.py - child class of Vehicle.py
- Racetrack.py - a class that create the racetrack
- race_run.py - the file that run the race
- vehicle(1, 2, 3).txt - a text file containg the brand, name, and colour of the car

To run the program, put python -u "path file of race_run.py" and ensure you are in the same directory or folder with the program.
When prompted for filename, put any of the vehicle txt file.
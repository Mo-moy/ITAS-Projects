"""
   Course: ITAS 185 - Introduction to Programming
   Assignment 1: Word Homophone 
   Name: Mejares Ebes
   Date: Oct. 15 2024
   Updated: Oct. 22 2024
   Description: Create a dictionary of word homophone
   in which you could add, update, remove, search a homophone, and also display the entire content of the library.
   I have updated so the while loop now has a condition and not use while true and break, and made the menu display its own function.
"""

# functions

"""
This function display the menu.
It print a triple quote string to display the menu with six options.
"""
def display_menu():

    print("""You may:
    1. Add a new homophone
    2. Update a homophone
    3. Remove a homophone
    4. Search for a homophone
    5. Display your homophones
    6. Exit the program
    """)

"""
This function allow user to add a word homophone.
Using a while loop, I ensure that the user only input alphabetical characters using isalpha().
If the input is valid, it ask user for the original word which will act as the key.
It then ask for the homophone which will act as the value.
It then take both of those inside the dictionary "dict = {}".
"""
def add_homophone():
    
    while True:
        
        name = input("Input the original word to add: ")
        
        if name.isalpha():            
            homophone = input("Input the homophone: ")
            print("New entry added\n")
            dict[name] = homophone
            break
        else:
            print("\n --- Error || Alphabetical Characters Only ---\n")
    
"""
This function allow the user to update a word homophone.
It will ask for the original word, which an if-else statement detect if the word exist or not.
If the word does not exist, it will show an error that the orginal word does not exist to the user and send them back to the menu.
If the word exist, it will ask user to input the new homophone, which will update over the old homophone.
"""
def updt_homophone():
    orig_word =input("Input the original word to update: ")
    
    if orig_word in dict:
        updt_homophone = input("Input the new homophone: ")
        print("Homophone updated\n")
        dict.update({orig_word: updt_homophone})
    else:
        print(f"\n --- Error || [ {orig_word} ] does not exist in the dictionary ---\n")
        
"""
This function allow the user to remove both the original word and the word homophone.
It will ask for the original word, which an if-else statement detect if the word exist or not.
If the word does not exist, it will show an error that the orginal word does not exist to the user and send them back to the menu.
If the word exist, it will ask the user if its sure to delete the word homophone using a while loop.
If its yes, the original word and word homophone is deleted.
If its no, the user will return to the menu.
"""
def rmv_homophone():
    orig_word =input("Input the original word to remove: ")
    
    if orig_word in dict:
        while True:
            usr_input = input(f"Delete [ {orig_word} : {dict[orig_word]} ]? (Yes/No): ").title()
            
            if usr_input == "Yes":
                print(f"The original word : {orig_word}  and the homophone : {dict[orig_word]} are now deleted\n")
                del dict[orig_word]
                break
            elif usr_input == "No":
                print("User is returning to Menu\n")
                break
            else:
                print(f"\n --- Error || [ {usr_input} ] is an Invalid Input || Please Input Yes or No---\n")
    else:
        print(f"\n --- Error || [ {orig_word} ] does not exist in the dictionary ---\n")
        
"""
This function allow the user to search a word homophone.
It will ask for the original word, which an if-else statement detect if the word exist or not.
If the word does not exist, it will show an error that the orginal word does not exist to the user and send them back to the menu.
"""   
def srch_homophone():
    orig_word =input("Search the original word: ")
    
    if orig_word in dict:
        print(f"\nName: [ {orig_word} ] || Homophone: [ {dict[orig_word]} ]\n")
    else:
        print(f"\n --- Error || [ {orig_word} ] does not exist in the dictionary ---\n")
        
"""
This function allow user to print all the word homophone inside the dictionary.
It uses a for loop to print out each of the word homophone in a decent looking format.
"""
def prnt_homophone():
    print(f"\n{'Name ||':>18} {'Homophone':>10}")

    for orig_word, homophone in dict.items():
        print(f"[ {orig_word:>10}  ] ||  [ {homophone:>10} ]")
    print("\n") 

# the dictionary
dict = {}

# intizialize so my condition work in the while loop
usr_input = 0

print("\nWelcome to your Homophone list.")

"""
It uses a while loop for user to keep using the program until they quit.
It use if-else and the isdigit() to ensure that the input are valid.
Another if-else to ensure the input is 1-6 and not over 6 or lower than 1.
If the input is valid, it then go to a switch case and call upon a function based on the number the user input.
"""
while usr_input != 6:
    
    display_menu()
    
    usr_input = input("Please enter your choice: ")
    
    if usr_input.isdigit():
        usr_input = int(usr_input)
        
        if usr_input > 6 or usr_input < 1:
            print(f"\n --- Error || [ {usr_input} ] is Invalid || Only 1-6 are Valid ---\n")
        else:
            # case switch that lead to different functions and to quit the program
            match usr_input:
                case 1:
                    add_homophone()
                case 2:
                    updt_homophone()
                case 3:
                    rmv_homophone()
                case 4:
                    srch_homophone()
                case 5:
                    prnt_homophone()
                case 6:
                    print("\n --- User has quit the program ---\n")

    else:
        print(f"\n --- Error || [ {usr_input} ] is Invalid || Positive Integer Only ---\n")

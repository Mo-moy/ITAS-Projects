"""
   Course: ITAS 185 - Introduction to Programming
   Assignment 2: Hangman Game
   Name: Mejares Ebes
   Date: Nov. 15 2024
   Description: This is the Class for Hangman Game.
"""

import random
import string

class HangmanGame:
    
    def __init__(self, secret_word = '', current_word_status = '', __max_attempts = 7, attempts_left = 7, __guesses = set(), usr = '', condemned = '' ):
        self.secret_word = secret_word
        self.current_word_status = current_word_status
        self.max_attempts = __max_attempts
        self.attempts_left = attempts_left
        self.guesses = __guesses
        self.usr = usr
        self.condemned = condemned
    
    def __str__(self):
        """
        
        This function return the current word status.

        Returns:
            str: the current word status
        """
        return f'{''.join(self.current_word_status)}'
    
    def __repr__(self):
        """

        This function return a str comprised of every attribute in dunder init for debugging purpose.
        
        Returns:
            str: dunder init's atributes
        """
        return f'object_name({self.secret_word}, {self.current_word_status}, {self.max_attempts}, {self.attempts_left}, {self.guesses}, {self.usr}, {self.condemned})'
    
    def __len__(self):
        """
        
        This function return the length or amount of guesses done by the user.

        Returns:
            int: lenght or count of the guesses set
        """
        return len(self.guesses)
    
    def read_file(self):
        """
        
        This function will read each line of 'hangman.txt then turn each word in its own thing in a list.

        Returns:
            list: list of words from 'hangman.txt'
        """
        with open("hangman.txt") as read_info:
            read_info = read_info.readlines()
            word_list = [word.strip() for word in read_info]
            return word_list
                
    def select_word(self):
        """
        
        This function will take the list from function read_file(), then select a random word from it.

        Returns:
            str: the chosen random word for Hangman
        """
        word_list = self.read_file()
        chosen_word = random.choice(word_list)
        return chosen_word.upper()
    
    def make_guess(self, guess):
        """
        
        This function check if the guessed letter is in the secret word or not.

        Args:
            guess (str): the guessed letter
        """
        if guess in self.secret_word:
            for index, letter in enumerate(self.secret_word):
                if guess == letter:
                   self.current_word_status[index] = guess
        else:
            self.attempts_left -= 1
        
    def is_win(self):
        """
        
        This function will check if the user guess the secret word when there is no loger any dash in current word status.
        If there is none, it will return as True, then the usr win.
        If not it will return False.

        Returns:
            bool: True or False
        """
        if '-' not in self.current_word_status:
            return True
        else:
            return False
    
    def is_lost(self):
        """
        
        This function will check if the usr has no more attempts left.
        If there is none, it will return True and the usr lose.
        If there is still attempts left, it return False.

        Returns:
            _type_: _description_
        """
        if self.attempts_left == 0:
            return True
        else:
            return False
    
    def letter_validator(self, guess):
        """
        
        This function check if the usr input is an actual letter.
        If the guess letter has already been input twice it will show an error and return False.
        It will return True if the input is an alphabetical letter and has one length, and return False if not.
        If the guess is a numeric or special character, it will show an error and return False.

        Args:
            guess (str): the guessed input

        Returns:
            bool: True or False
        """
        
        if guess  in self.guesses:
            print(f' -- Error | {guess} has already been guessed -- ')
            return False
        
        if guess.isalpha() and len(guess) == 1:
            return True
        elif guess.isalpha() and len(guess) != 1:
            print(f' -- Error | [{guess}] has more than one character -- ')  
            return False
        else:
            print(f' -- Error | [{guess}] is not an alphabetical character -- ')
            return False  
        
    def non_guessed_letters(self):
        """
        
        This function will print out the letters that are not guessed yet.
        It uses import string so I can make a list of the ascii characters.
        The list will then be join to a new str var.
        Then a for loop to remove letters from the str var that equal the guess.
        Lastly, it return the str var.

        Returns:
            str: the non-guessed letters
        """
        non_guessed_list = list(string.ascii_uppercase)
        non_guessed_str = ''.join(non_guessed_list)
        for guess in self.guesses:  
            non_guessed_str = non_guessed_str.replace(guess, "")
        return non_guessed_str
    
    def dash_temp_name(self):
        """
        
        This function just replace each characters with dash in secret word.
        It just take the length of the secret word and multiply the int to the dash.

        Returns:
            str: the secret word but in all chars are dashes
        """
        return f'{'-' * len(self.secret_word)}'
    
    def hangman_art(self):
        """
        
        This is a switch case that return an ascii art depending on the attempts_left.
        
        Returns:
            str: an ascii art of the gallow and the person
        """
        match self.attempts_left:
            case 0:
                return """
            
                   +====+                   
                   |    |
                   0    |           
                  /|\\   |
                  / \\   |
                        |
                ==========
                """
            case 1:
                return """
            
                   +====+                   
                   |    |
                   0    |           
                  /|\\   |
                  /     |
                        |
                ==========
                """            
            case 2:
                return """
            
                   +====+                   
                   |    |
                   0    |           
                  /|\\   |
                        |
                        |
                ==========
                """                
            case 3:
                return """
            
                   +====+                   
                   |    |
                   0    |           
                  /|    |
                        |
                        |
                ==========
                """
            case 4:
                return """
            
                   +====+                   
                   |    |
                   0    |           
                   |    |
                        |
                        |
                ==========
                """                
            case 5:
                return """
            
                   +====+                   
                   |    |
                   0    |           
                        |
                        |
                        |
                ==========
                """               
            case 6:
                return """
            
                   +====+                   
                   |    |
                        |           
                        |
                        |
                        |
                ==========
                """
            case 7:                
                return """
            
                   +====+                   
                        |
                        |           
                        |
                        |
                        |
                ==========
                """   
    
    def result_msg(self):
        """
        
        This function return a result message depending wif is_win or is_lost is True.
        It also print out the guessed word and how many attempts it took.

        """
        if self.is_win() == True:
            return f"""                                                                                                                                                                      
oooooo   oooo                            oooooo   oooooo     oooo  o8o              .o. 
 `888.   .8'                              `888.    `888.     .8'   `"'              888 
  `888. .8'    .ooooo.  oooo  oooo         `888.   .8888.   .8'   oooo  ooo. .oo.   888 
   `888.8'    d88' `88b `888  `888          `888  .8'`888. .8'    `888  `888P"Y88b  Y8P 
    `888'     888   888  888   888           `888.8'  `888.8'      888   888   888  `8' 
     888      888   888  888   888            `888'    `888'       888   888   888  .o. 
    o888o     `Y8bod8P'  `V88V"V8P'            `8'      `8'       o888o o888o o888o Y8P 
            \n\t{self.usr} has guessed the word {self.secret_word}
            \n\t{self.condemned}, has been set free!
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                            _    ,
           __   __   __   __   __   --  -,_/\\_~0_\\ ___    __   __   __
                                  --    /  ___ \\-  `___`"-,
                                ---    `"-( @ )----( @ )---`
                                           '-'      '-'
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            \n\t{self.usr} has taken {len(self)} guesses.            
                """
            # print(f'\t{self.usr} has taken {len(self)} guesses.')
            
        elif self.is_lost() == True:
            return f"""                                                                                                                                                                                                                                                                
oooooo   oooo                            ooooo                                     .o. 
 `888.   .8'                             `888'                                     888 
  `888. .8'    .ooooo.  oooo  oooo        888          .ooooo.   .oooo.o  .ooooo.  888 
   `888.8'    d88' `88b `888  `888        888         d88' `88b d88(  "8 d88' `88b Y8P 
    `888'     888   888  888   888        888         888   888 `"Y88b.  888ooo888 `8' 
     888      888   888  888   888        888       o 888   888 o.  )88b 888    .o .o. 
    o888o     `Y8bod8P'  `V88V"V8P'      o888ooooood8 `Y8bod8P' 8""888P' `Y8bod8P' Y8P    
            \n\t{self.usr} did not guessed the word {self.secret_word}
            \n\t{self.condemned} has been hanged!
            \n{self.hangman_art()}
            \n\t{self.usr} has taken {len(self)} guesses.            
              """                   
            # print(f'\t{self.usr} has taken {len(self)} guesses.')    

    def try_again_prompt(self):
        """
        
        This function will ask user if they want to try again.
        If user press 'y', they will play again with the attempts_left reset to 7.
        If user press 'n', it will print a usr left msg and then exit.
        if user press something that is not 'y' or 'n', it print out an error msg and prompt the try_again function.
        
        """
        usr_input = input('\nWould you like to try again ([y] for yes, [n] for no): ').lower()       
        
        if 'y' in usr_input:
            self.attempts_left = 7 
            self.main()
        elif 'n' in usr_input:
            print(f'\n{self.usr} has left the Game!')
        else:
            print('-- Error | Invalid Input --')
            self.try_again_prompt()
            
    def intro(self):
        """
        
        This function is for asking the user's username, and the name of the condemned.
        If user did not put a name, user will be name 'User'.
        If user did not put the condemned's name, the condemned's name will be 'John Doe'.
        It introduced a welcoming msg, then initialize the secret_word and the current_world_status
        
        """
        self.usr = input(f'\n{'|' * 100}\n\nEnter Username: ').title()
        if self.usr == '':
            self.usr = 'User'    
        self.condemned = input('Enter the name of the condemned: ').title()  
        if self.condemned == '':
            self.condemned = 'John Doe'     
        print(f'\nWelcome {self.usr} to a game of Hangman. I have a word in mind.')
        print(f'You have {self.attempts_left} attemts to guess the word.')
        print(f'If the word is not guessed after {self.attempts_left} attempts. {self.condemned} will move to the afterlife.')
        print('Good Luck!')
        self.read_file()
        self.secret_word = self.select_word()
        self.current_word_status = list(self.dash_temp_name())        
                                    
    def main(self):
        """
        
        This function is just so the game could function.
        It consist of the intro function, a while loop that check if either is_wi or is_lost is no True, and the try again function.
        The while loop consist of print out of the acii art, the amount of attempts left, and asking what is you guess.
        The guess will then go through the letter valid function to check if its valid or not, if not it return an error msg for not having one alphabetical chars or non-alphabetical chars.
        If its valid, the guess will be added to the guesses set and then go through the make guess function.
        It then print out the current word status and the non-guessed letters for user to check if they have guessed something or not.
        If either is_win or is_lost condition are achieved, result_msg function detect it and print either a win or a lost msg.
        Lastly, it will ask user to try again or not.
        
        """

        self.intro()
            
        while not (self.is_win() or self.is_lost()):
            #print(repr(self)) # debugging also test case
            print(f'{self.hangman_art()}')           
            print(f'You have {self.attempts_left} attempts left')
            guess = input('Enter your guess: ').upper()
            if self.letter_validator(guess) == True:
                self.guesses.add(guess)
                self.make_guess(guess)
            # elif self.letter_validator(guess) == False:
                # print(f' -- Error | [{guess}] has more than one character -- ')      
            # else:
            #     print(f' -- Error | [{guess}] is not an alphabetical character -- ')       
                         
            print(str(self))            
            print(f'{self.non_guessed_letters()}\n\n{'|' * 100}')
            
        print(self.result_msg())
        self.try_again_prompt()
                        
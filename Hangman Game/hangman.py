'''
Project 5 - Hangman - Spring 2022
Author: Kevin Wang  PID: kevinwang

This file contains the Hangman class, which manages the internal
details of a Hangman game.

I have neither given or received unauthorized assistance on this assignment.
Signed:  Kevin Wang
'''

''' This file is initially INCOMPLETE. You must complete its implementation,
as well as that of the Hangman_Interface class (play_hangman.py) to have a
complete program.

First, read and understand the existing code. Then add appropriate code
wherever you see a TODO comment. Do not change any existing code. '''


import random

class Hangman:
    ''' This class manages the internal details of a game of
    Hangman. No user interface is presented or managed by this
    class. '''
    
    def __init__(self, filename, max_wrong):
        ''' Initializes a game by reading a list of potential
        words to guess from the specified file. Sets the
        maximum number of wrong guesses per game. '''
        
        self.word_list = []
                
        ''' TODO: Read the contents of the specified file and fill
        the word list. Make sure to strip the newline character from
        each word. '''
        
        
        
        with open(filename, 'r') as file:
            self.word_list = filename
            self.word_list = [word.strip() for word in file]
            
        
        self.MAX_WRONG_GUESSES = max_wrong
        self.new_game()
        

    def new_game(self):
        ''' Starts a new game by setting the number of wrong
        guesses to 0, randomly choosing a new word to guess,
        and setting the current status of the guessed word to
        the appropriate number of dashes. '''
        
        self.number_wrong_guesses = 0
        self.answer_word = random.choice(self.word_list)
        self.guess_word = '-' * len(self.answer_word)
        

    def process_guess(self, letter):
        ''' Processes the user's guess of the specified letter
        by searching the word for the letter and updating the
        current guess word. Returns True if the guessed letter
        was found anywhere in the answer word. '''
        
        found = False
        current = ''
        for i in range(len(self.answer_word)):
            if self.answer_word[i] == letter:
                current += letter
                found = True
            else:
                current += self.guess_word[i]
        
        self.guess_word = current
        if not found:
            self.number_wrong_guesses += 1
        return found


    def get_status(self):
        ''' Returns the current status of the game as a string.
        Returns 'won' if the guessed word matches the answer word,
        'loss' if the number of wrong guesses has reached the maximum
        allowed, and 'ongoing' otherwise. '''
        
        if self.guess_word == self.answer_word:
            return 'won'
        
        elif self.number_wrong_guesses == self.MAX_WRONG_GUESSES:
            return 'loss'
        else:
            return 'ongoing'
        
        ''' TODO: Replace the pass statement with code that fulfills
        purpose of the function as described in the function docstring. '''


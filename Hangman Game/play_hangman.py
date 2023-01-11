'''
Project 5 - Hangman - Spring 2022
Author: Kevin Wang PID: kevinwang

This file contains the Hangman_Interface class, which manages user
interface of a Hangman game.

I have neither given or received unauthorized assistance on this assignment.
Signed:  Kevin Wang
'''

''' This file is initially INCOMPLETE. You must complete its implementation,
as well as that of the Hangman class (hangman.py) to have a complete program.

First, read and understand the existing code. Then add appropriate code
wherever you see a TODO comment. Do not change any existing code. '''

from hangman import Hangman
from tkinter import *
from functools import partial

class Hangman_Interface:
    ''' This class represents a graphical user interface for a game of
    Hangman. The game's internal details are managed by a separate object. '''
    
    def __init__(self, game):
        ''' Initializes the hangman GUI as a window containing a canvas,
        a word to guess, the letter buttons (in two rows), and a new
        game button. '''
        
        self.game = game
        
#sets the teal background
        self.root = Tk()
        self.root.title('Hangman')
        self.root.minsize(500, 350)
        self.root.configure(background='teal')

#Sets the inner cyan background        
        self.canvas = Canvas(self.root, width=400, height=300, background='cyan')
        self.canvas.pack(pady=(30, 10))

        self.current_guess = StringVar()
        self.current_guess.set(self.game.guess_word)
        guess_label = Label(self.root, textvariable=self.current_guess, font=('Arial', 60))
        guess_label.configure(background=self.root['background'])
        guess_label.pack(pady=10)
    
        letter_buttons1_frame = Frame(self.root, background=self.root['background'])
        letter_buttons1_frame.pack(pady=10)
        letter_buttons2_frame = Frame(self.root, background=self.root['background'])
        letter_buttons2_frame.pack(pady=10)

        self.letter_buttons1 = {}
        self.letter_buttons2 = {}
       
        for letter in 'abcdefghijklm':
            process_guess_partial = partial(self.process_guess, letter)
            self.letter_buttons1[letter] = Button(letter_buttons1_frame, text=letter, font=('Arial', 18),
                        background='white', height=1, width=2, command=process_guess_partial)
            self.letter_buttons1[letter].pack(side=LEFT, padx=5)
        
        for letter in 'nopqrstuvwxyz':
            process_guess_partial = partial(self.process_guess, letter)
            self.letter_buttons2[letter] = Button(letter_buttons2_frame, text=letter, font=('Arial', 18),
                        background='white', height=1, width=2, command=process_guess_partial)
            self.letter_buttons2[letter].pack(side=LEFT, padx=5)
    
        new_game_button = Button(self.root, text='New Game', font=('Arial', 18), height=1, width=12,
                                 command=self.start_new_game)
        new_game_button.pack(pady=30)
    
        self.draw_initial_scene()


    def draw_initial_scene(self):
        ''' Draws the initial content on the canvas. '''
        
        # Base
        self.canvas.create_rectangle(30, 270, 370, 300, fill='burlywood', outline='gray')
        self.canvas.create_line(300, 270, 300, 50, 200, 50, width=5)
    
        ''' TODO: Draw the rope and noose, as well as the sun, to match
        the initial scene displayed in a new game. See the spec for
        screen shots. '''
        #rope
        self.canvas.create_line(200, 50, 200, 80, width =7, fill='Gray', dash=(7,4))
        #noose
        self.canvas.create_oval(180,80,220,125,width =7, outline='Gray', dash=(7,4))
        #sun
        self.canvas.create_oval(30,10,100,100,fill='yellow')
                            

    
    
    
    
    def process_guess(self, letter):
        ''' Updates the interface when the user presses a letter button. This
        is the event handler for all letter buttons.
        
        After the game object processes the letter, it updates either the guess
        word or the hangman figure, then disables the chosen button. Finally,
        it checks for a win or loss and updates accordingly. '''
        
        found = self.game.process_guess(letter)
            
        if found:
            self.current_guess.set(self.game.guess_word)
        else:
            self.update_figure()
        
        # Disable the chosen letter button
        if letter < 'n':
            self.letter_buttons1[letter]['state'] = 'disabled'
        else:
            self.letter_buttons2[letter]['state'] = 'disabled'
            
        status = self.game.get_status()
        if status != 'ongoing':
            self.disable_all_letter_buttons()
            if status == 'won':
                self.canvas.create_text(200, 285, text='You won!', font=('Arial', 28))
            else:
                self.canvas.create_text(200, 285, text='You lost!', font=('Arial', 28))
                self.canvas.delete(self.left_eye)
                self.canvas.delete(self.right_eye)
                
                ''' TODO: Draw x characters as eyes and display the answer word.
                See the appropriate screen shot in the spec. '''
                
                #left x
                self.canvas.create_text(190, 95, text='X', font=('Arial', 10))
                #right x
                self.canvas.create_text(208, 95, text='X', font=('Arial', 10))
                #displayed word
                self.canvas.create_text (80,190, text=(self.game.answer_word), font=('Arial',8))
                self.canvas.create_text (80,170, text ='The word was', font=('Arial',8))
                
            
                
                


    def update_figure(self):
        ''' Updates the hangman figure on the canvas by adding the appropriate
        body part. It assumes all other previous body parts have already been
        drawn. '''
        
        body_parts = self.game.number_wrong_guesses  # number of body parts to display
        
        # Head
        if body_parts == 1:
            self.canvas.create_oval(180, 80, 220, 130, fill='gray', width=2)
            self.left_eye = self.canvas.create_oval(188, 95, 195, 102, fill='black') # left eye
            self.right_eye = self.canvas.create_oval(202, 95, 209, 102, fill='black') # right eye
            self.canvas.create_line(190, 115, 210, 115) # mouth
        elif body_parts == 2: #body
            self.canvas.create_line(200,130,200,200, width=4)
        elif body_parts == 3: #right leg
            self.canvas.create_line(200,195,235,235, width=3)
        elif body_parts == 4: #left Leg
            self.canvas.create_line(200,195,165,235, width=3)
        elif body_parts == 5: #right arm
            self.canvas.create_line(200,152,250,150, width=2)
        elif body_parts == 6: #left arm
            self.canvas.create_line(200,152,150,150, width=2)


        ''' TODO: Add elif and else clauses that draw the appropriate body part
        based on the number of wrong guesses. See the screen shots in the spec. '''
        
    def enable_all_letter_buttons(self):
        ''' Enables all of the buttons used to guess a letter. '''
        for button in self.letter_buttons1.values():
            button['state'] = 'normal'
        for button in self.letter_buttons2.values():
            button['state'] = 'normal'


    def disable_all_letter_buttons(self):
        ''' Disables all of the buttons used to guess a letter. '''
        for button in self.letter_buttons1.values():
            button['state'] = 'disabled'
        for button in self.letter_buttons2.values():
            button['state'] = 'disabled'
        
        ''' TODO: Replace the pass statement with code that disables
        all letter buttons. '''


    def start_new_game(self):
        ''' Starts a new game by clearing the canvas and
        getting a new word to guess. '''
        
        self.game.new_game()
        self.canvas.delete('all')
        self.current_guess.set(self.game.guess_word)
        self.draw_initial_scene()
        self.enable_all_letter_buttons()


# Below is the main driver of the program. It is not part of
# the Hangman_Interface class.

def main():
    ''' Plays Hangman by creating a Hangman game object and
    an interface for it. '''
    
    game = Hangman('word_list.txt', 6)
    
    Hangman_Interface(game)


# The following statement prevents Web-CAT from running this
# program automatically. 
if __name__ == '__main__':
    main()
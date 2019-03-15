'''
Created on Mar 14, 2019

@author: bvhwa
'''
class Hangman:
    def __init__(self, secret, numGuesses):
        self.secret = secret;
        self.numGuesses = numGuesses;
        self.guesses = [];
    
    def guessWord(self, word):
        if word == self.secret:
            return True;
        else:
            self.numGuesses -= 1;
            return False;
    
    def guessLetter(self, letter):
        if letter in self.secret:
            if letter not in self.guesses:
                self.guesses.append(letter);
                
            return True;
        else:
            self.numGuesses -= 1;
            return False;
        
    def hasGuesses(self):
        if self.numGuesses == 0:
            return False;
        else:
            return True;
        
    def printWord(self):
        print("Word: ", end =" ");
        for i in range(0, len(self.secret)):
            letter = self.secret[i:i+1];
            
            if letter in self.guesses:
                print(letter + " ", end =" ");
            else:
                print("_ ", end =" ");
        print();
        print("# of guesses remaining : {0}" .format(self.numGuesses));
                
hangman = Hangman("spooky", 5);
correct = False;

while(hangman.hasGuesses()):
    hangman.printWord();
    print("1. Guess a letter. ");
    print("2. Guess the word. ");
    option = int(input("Choose an option: "));
    
    if option == 1:
        letter = input("Guess a letter: ");
        if(hangman.guessLetter(letter)):
            print(letter + " is in the word.");
        else:
            print(letter + " is not in the word.");
    else:
        word = input("Guess the word: ");
        if(hangman.guessWord(word)):
            print(word + " is the word!");
            correct = True;
            break;
        else:
            print(word + " is not the word!");

if(not correct):            
    print("You ran out of guesses, better luck next time!");
#Ali Reza Salimi
#326 Project
import random
from wordlist import hangman_words

class Game:
    """The primary class of this script, meant to hold the
    components of a hangman game"""


    def __init__(self):
        """Initializing key instances, and using 'self', to use across script"""
        self.word = random.choice(hangman_words).upper()
        self.completeword = "_" * len(self.word)
        self.guessed = False
        self.letterguess = set()
        self.wordsguess = set()
        self.tries = 6

    def stickfigure(self):
        """Returns the stick figure based on correct or incorrect guesses"""
        stickman = [
            r"""
               --------
               |      |
               |      O
               |     \|/
               |     / \
            """,
            r"""
               --------
               |      |
               |      O
               |     \|/
               |     /
            """,
            r"""
               --------
               |      |
               |      O
               |     \|/
               |
            """,
            r"""
               --------
               |      |
               |      O
               |     \|
               |
            """,
            r"""
               --------
               |      |
               |      O
               |      |
               |
            """,
            r"""
               --------
               |      |
               |      O
               |
               |
            """,
            r"""
               --------
               |      |
               |
               |
               |
            """
        ]
        return stickman[self.tries]




    def letter_guesser(self, guess):
        """Processes single letter guess"""
        if guess in self.letterguess:
            return f"{guess} has been guessed already"
        if guess not in self.word:
            self.tries -= 1
            self.letterguess.add(guess)
            return "Your guess is incorrect"
        self.letterguess.add(guess)
        listword = list(self.completeword)
        indices = [i for i, letter in enumerate(self.word) if letter == guess]
        for index in indices:
            listword[index] = guess
        self.completeword = "".join(listword)
        if "_" not in self.completeword:
            self.guessed = True
        return f"{guess} is correct"




    def word_guesser(self, guess):
        """Processes word guess"""
        if guess in self.wordsguess:
            return f"{guess} has been guessed already."
        if guess != self.word:
            self.tries -= 1
            self.wordsguess.add(guess)
            return "Your guess is incorrect"
        self.guessed = True
        self.completeword = self.word
        return "Your guess is correct"



    def play(self):
        """Hangman game"""
        print("Game time")
        while not self.guessed and self.tries > 0:
            print(self.stickfigure())
            print(self.completeword + "\n")
            guess = input("Take a guess (letter): ").upper()
            if len(guess) == 1 and guess.isalpha():
                print(self.letter_guesser(guess))
            elif len(guess) == len(self.word) and guess.isalpha():
                print(self.word_guesser(guess))
            else:
                print("Invalid guess")
        if self.guessed:
            print(f"Congratulations, you win, {self.word} is correct" )
        else:
            print(f"You lose. The word was {self.word}.")



def main():
    """main function"""
    playtime = Game()
    playtime.play()
    while input("Play again? (y/n): ").lower() == 'y':
        playtime = Game()
        playtime.play()

if __name__ == "__main__":
    main()
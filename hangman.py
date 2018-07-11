"""Main Hangman Module."""


class Hangman(object):
    """Docstring for Hangman."""

    def __init__(self):
        super(Hangman, self).__init__()
        self.word = "hangman"
        self.letters_used = []
        self.attempt = 9
        self.hint = []
        self.win = False

    def _decreass_attempt(self):
        self.attempt -= 1
        return self.attempt > 0

    def _get_input(self, text):
        return raw_input(text)

    def _validate_input(self, input):
        return (len(input) >= 1 and input.isalpha())

    def _validate(self, input):
        if len(input) > 1:
            return self._validate_full_word(input)
        else:
            return self._validate_guess(input)

    def _validate_full_word(self, input):
        return input == self.word

    def _set_init_hint(self):
        self.hint = list("-" * len(self.word))

    def _set_hint(self, indexes, guess):
        for index in indexes:
            self.hint[index] = guess
        if '-' not in self.hint:
            self.win = True
            return True
        return False

    def _print_hint(self):
        print "Letters already used: ", ''.join(self.letters_used), '\t', "Attempt left: ", self.attempt, '\n'
        print "".join(self.hint), '\n'

    def _get_hint_possition(self, guess):
        return [i for i, x in enumerate(self.word) if x == guess]

    def _validate_guess(self, guess):
        self.letters_used.append(guess)
        return guess in self.word

    def setnewword(self, new_word):
        if new_word.isalpha():
            self.word = new_word.lower()
            self._set_init_hint()
            print "New word succesfully set in lower case"
        else:
            print "Error: Please use alphabetic characters only and minimun one."

    def start(self):
        print "Welcome to the Hangman Game."
        self._set_init_hint()
        while self.attempt != 0:
            self._print_hint()
            guess = self._get_input("Guess a letter or the full word.\n> ").lower()
            while not self._validate_input(guess):
                guess = self._get_input("Please use alphabetic characters only and minimun one.\n> ").lower()

            if self._validate(guess):
                if len(guess) == 1:
                    indexes = self._get_hint_possition(guess)
                    if self._set_hint(indexes, guess):
                        break
                    print "Well Done guess, try the next one."
                else:
                    self.win = True
                    break
            else:
                print "Bad luck on this one, try again."
                self._decreass_attempt()
        if self.win:
            print "Well done, You guess the secret word."
        else:
            print "Ho .... bad luck."
            res = self._get_input("Do you want to try again? y/n\n")
            if 'y' in res:
                self.__init__()
                self.start()

game = Hangman()

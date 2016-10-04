import re
import random

class Swedishtrainer:
    
    def __init__(self):
        # Wordlist to hold the dictionary and seeding the RNG
        random.seed()
        self.wordlist = []
        self.question_amount = 1
        self.player_score = 0
        
    # Ask the user what dictionary they want to use
    def select_dictionary_prompt(self):
        print('Syötä haluamasi sanaston numero tai tiedostonimi:')
        print('1. Kappale 1')
        print('2. Kappale 5')
        print('3. Testidata')
        dictionary_selection = self.read_input('string')

        if dictionary_selection == '1':
            dictionary_name = 'kappale1.txt'
        elif dictionary_selection == '2':
            dictionary_name = 'kappale5.txt'
        elif dictionary_selection == '3':
            dictionary_name = 'testi.txt'
        else:
            dictionary_name = dictionary_selection

        print('Montako kysymystä?')
        self.question_amount = self.read_input('int')

        return dictionary_name
    

    # Read the dictionary file and collect data from it
    def read_dictionary_file(self, dictionary_name):

        try:
            # Opening file as read only with with for safety
            with open(dictionary_name, 'r') as dictionary_data:
                
                # Reading through all lines one by one and adding them into the wordlist as tuples
                for line in dictionary_data.readlines():

                    # Pair the Finnish and Swedish words that are separated by a : as a tuple
                    finnish_word = re.compile('(?<=:)[^:\n]+').search(line).group()
                    swedish_word = re.compile('(?<!:)[^:\n]+').search(line).group()

                    entry = finnish_word, swedish_word

                    self.wordlist.append(entry)

            # Sanasto file no longer needed, as it has been completely processed
            dictionary_data.close()
        except Exception:
            print('File does not exist.')

    def generate_single_question(self):

        # Select a random word from the wordlist and randomise the displayed language
        random_word = self.wordlist[random.randrange(len(self.wordlist))]
        language_flip = random.choice([True, False])

        # Show the random word and ask for translation
        print()
        print('Käännä tämä sana:')
        print(random_word[language_flip])
        translated_answer = input('Vastaus: ')

        # Check if the answer is correct and respond accordingly
        if translated_answer == random_word[not language_flip]:
            print('Oikein')
            self.player_score += 2
            print('Pisteesi ovat nyt %d.' % self.player_score)
        else:
            print('Väärin, oikea vastaus olisi ollut %s.' % (random_word[not language_flip]))
            self.print_score()

    def generate_questions(self):

        for index in range(self.question_amount):
            self.generate_single_question()

    def print_score(self):
        print('Pisteesi ovat nyt %d.' % (self.player_score))

    def read_input(self, user_input_type):

        input_ok = False

        while input_ok != True:
            try:

                user_input = input()

                if user_input_type == 'int':
                    user_input = int(user_input)

                if user_input_type == 'float':
                    user_input = float(user_input)

                if user_input_type == 'string':
                    user_input = str(user_input)

                input_ok = True

            except:
                print('Virheellinen syöte. Yritä uudelleen.')
        
        return user_input

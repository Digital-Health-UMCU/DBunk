"""Magic 8ball script"""

import numpy as np
import random


print('  __  __          _____ _____ _____    ___  ')
print(' |  \/  |   /\   / ____|_   _/ ____|  / _ \ ')
print(' | \  / |  /  \ | |  __  | || |      | (_) |')
print(' | |\/| | / /\ \| | |_ | | || |       > _ < ')
print(' | |  | |/ ____ \ |__| |_| || |____  | (_) |')
print(' |_|  |_/_/    \_\_____|_____\_____|  \___/ ')
print('')
print('')
print('')
print('Hello there, I am the Magic 8 Ball')

answers = ['Rely on your inner soul', 
           'Be true to yourself', 
           'Most likely', 
           'Ask again later', 
           'Better not tell you now', 
           'You should find that out for yourself', 
           'It is trivial',
           'Very doubtful',
           'Je suis une pomme',
           '42',
           'Ofcourse'
           'I am fine',
           'Ergo sum',
           'COVID never dies'
           'Of course',
           'I am fine']

def magic8ball():
    """Ask any question and get an answer."""
    print('Ask me any question:\n')
    input()
    print (answers[random.randint(0, len(answers)-1)] )
    replay()
    

def replay():
    """Replay the 8ball game if you want"""
    print ('\nDo you have another question? [Y/N] ')
    reply = input()
    if reply.lower() == 'y':
        magic8ball()
    elif reply.lower() == 'n':
        exit()
    else:
        print('My apologies, I did not catch that. Please repeat.')
        replay()

if __name__ == '__main__':
    magic8ball()

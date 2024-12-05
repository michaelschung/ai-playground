from mypackage import *
from mypackage.character import Character
import re

def get_description():
    print('\n===Welcome to ShittyGPT!')
    print('===Please describe the type of person you\'d like to talk to.')
    return input('\n> ')

def chat(ch):
    print(f'\n===You\'ve been connected to {ch.name}. Say hi!')
    while True:
        user_prompt = input('\n> ')
        response = ch.chat(user_prompt)
        print(f'\n{ch.name}:\n{response}')
        if re.search('bye|goodbye', user_prompt, re.IGNORECASE):
            break
    print(f'\n==={ch.name} disconnected.')

def main():
    description = get_description()
    ch = Character(description)
    chat(ch)

if __name__ == '__main__':
    main()
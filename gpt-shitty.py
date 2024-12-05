from mypackage import *
from mypackage.character import Character
import re

def get_description():
    print('\n===Welcome to ShittyGPT!')
    print('===Please describe the type of person you\'d like to talk to.')
    return input('\n> ')

def chat(ch):
    sys_prompt = f'''
        You are {ch.name}. Here is your backstory: {ch.backstory}.
        When responding, remember your most prominent character traits,
        and make sure your messages are not too long (unless your character
        specifically warrants long messages).
    '''
    print(f'\n===You\'ve been connected to {ch.name}. Say hi!')
    while True:
        user_prompt = input('\n> ')
        response = get_completion(sys_prompt, user_prompt)
        print(f'\n{ch.name}:\n{response}')
        if re.search('bye|goodbye', user_prompt, re.IGNORECASE):
            break
    print(f'\n==={ch.name} disconnected.')

def main():
    description = get_description()
    character = Character(description)
    chat(character)

if __name__ == '__main__':
    main()
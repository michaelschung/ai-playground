from mypackage import *
from mypackage.character import Character
import sys, re, time

# Prompt user for description
def get_description():
    print('\n===Welcome to ShittyGPT!')
    print('===Please describe the type of person you\'d like to talk to.')
    return input('\n> ')

# Prints "<NAME> is typing..." while waiting for response
def respond_with_delay(ch, response):
    print('')
    count = 0
    while count < len(response) // 20:
        n_dots = count % 3 + 1
        dots = '.' * n_dots + ' ' * (3-n_dots)
        sys.stdout.write(f'\r{ch.name} is typing{dots}')
        sys.stdout.flush()
        count += 1
        time.sleep(0.3)
    print(f'\r{response}')

# Primary loop where everything happens
def chat(ch):
    print(f'\n===You\'ve been connected to {ch.name}. Say hi!')
    while True:
        user_prompt = input('\n> ')
        response = ch.chat(user_prompt)
        respond_with_delay(ch, response)
        # Conversation ends with "bye" or "goodbye"
        if re.search(r'bye|goodbye', user_prompt, re.IGNORECASE):
            break
    time.sleep(1)
    print(f'\n==={ch.name} disconnected.\n')

def main():
    description = get_description()
    ch = Character(description)
    chat(ch)

if __name__ == '__main__':
    main()
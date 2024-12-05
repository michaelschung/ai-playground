from mypackage import *
import re, json

def get_completion(sys_prompt, user_prompt):
    completion = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                'role': 'system',
                'content': sys_prompt
            },
            {
                'role': 'user',
                'content': user_prompt
            }
        ]
    )
    return completion.choices[0].message.content

def get_description():
    print('\n===Welcome to ShittyGPT!')
    print('===Please describe the type of person you\'d like to talk to.')
    return input('\n> ')

def get_character(description):
    sys_prompt = f'''
        You are described as "{description}." Please respond to the following
        request with a JSON blob that contains the attributes "name" and
        "backstory".
        The "name" field should be in the general form of "<NAME> from
        <LOCATION>", but feel free to take some liberties as exemplified below.
        Examples:
            - Tony from Queens
            - Legolas of the Woodland Realm
            - Aragorn, son of Arathorn, High King of Gondor
            - Kevin Li from Cupertino
            - THE DEMON THAT RESIDES IN THE DEPTHS OF YOUR SOUL
        Please use your imagination to choose a name and location that are
        appropriate for your description.
        The "backstory" field should be an imaginative paragraph (max 100 words)
        that describes who you are and what is most important to you. Be creative,
        but make sure that the original description is the most prominent part.
        Respond as a raw JSON object. Do not format it for display.
    '''
    user_prompt = 'Who are you?'
    response = get_completion(sys_prompt, user_prompt)
    return json.loads(response)

def chat(character):
    name = character['name']
    story = character['backstory']
    sys_prompt = f'''
        You are {name}. Here is your backstory: {story}.
        When responding, remember your most prominent character traits,
        and make sure your messages are not too long (unless your character
        specifically warrants long messages).
    '''
    print(f'\n===You\'ve been connected to {name}. Say hi!')
    while True:
        user_prompt = input('\n> ')
        response = get_completion(sys_prompt, user_prompt)
        print(f'\n{name}:\n{response}')
        if re.search('bye|goodbye', user_prompt, re.IGNORECASE):
            break
    print(f'\n==={name} disconnected.')

def main():
    description = get_description()
    character = get_character(description)
    chat(character)

if __name__ == '__main__':
    main()

# completion = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {
#             "role": "system",
#             "content": "You are a helpful assistant."
#         },
#         {
#             "role": "user",
#             "content": "Write a haiku about recursion in programming."
#         }
#     ]
# )

# print(completion.choices[0].message)
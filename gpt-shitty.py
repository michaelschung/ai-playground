from mypackage import *

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

def get_sys_prompt():
    return input('Enter a system prompt for ChatGPT: ')

def chat(sys_prompt):
    while True:
        user_prompt = input('> ')
        if user_prompt == 'quit':
            break
        print(get_completion(sys_prompt, user_prompt))
    print('Thanks for chatting. Goodbye!')

def main():
    sys_prompt = get_sys_prompt()
    chat(sys_prompt)

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
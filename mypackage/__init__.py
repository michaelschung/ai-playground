from openai import OpenAI

client = OpenAI()

MODEL = 'gpt-4o-mini'

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
from openai import OpenAI

client = OpenAI()
MODEL = 'gpt-4o-mini'

# Prompts model using last message in context
# Assumes last message was a user prompt
def get_completion_with_context(msgs):
    completion = client.chat.completions.create(
        model=MODEL,
        messages=msgs
    )
    return completion.choices[0].message.content

# OpenAI example; no longer used, keeping for posterity
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
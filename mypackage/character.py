from . import client, get_completion_with_context
import json

class Character:
    def __init__(self, description):
        # Maintains context for entire conversation
        self.messages = []
        self.name, self.backstory = self.generate_character(description)

    # Updates context
    def add_message(self, role, content):
        self.messages.append({
            'role': role,
            'content': content
        })

    # Accepts user prompt, returns response after updating context
    def chat(self, user_prompt):
        full_user_prompt = f'''
            Respond to the following prompt in character, using normal
            English as befits your character. Remember your most prominent
            character traits, and make sure your messages are not too long
            (unless your character specifically warrants long messages).
            Your prompt: {user_prompt}
        '''
        self.add_message('user', full_user_prompt)
        return self.contextual_response()

    # Assumes last prompt in context is a user prompt to respond to
    # Returns response text after updating context
    def contextual_response(self):
        response = get_completion_with_context(self.messages)
        self.add_message('assistant', response)
        return response

    # Uses AI to generate name and backstory, updates context accordingly
    def generate_character(self, description):
        sys_prompt = f'''
            You are described as "{description}." Please respond to the next
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
        self.add_message('system', sys_prompt)
        self.add_message('user', user_prompt)
        raw_response = self.contextual_response()
        response = json.loads(raw_response)
        return response['name'], response['backstory']
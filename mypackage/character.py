from . import client, get_completion
import json

class Character:
    def __init__(self, description):
        self.name, self.backstory = self.get_character(description)
        self.messages = []

    def get_character(self, description):
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
        response = json.loads(get_completion(sys_prompt, user_prompt))
        return response['name'], response['backstory']

    
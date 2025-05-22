import os
from openai import OpenAI
from dotenv import load_dotenv


class CipherLLM:
    def __init__(self):
        load_dotenv()  # Load environment variables from .env file
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    def generate_poetic_response(self, command, model):
        # Create a prompt that includes game context
        prompt = f"""You are an AI assistant on a damaged spaceship, speaking to a blind passenger.
        The passenger's name is {model.name} and they are a {model.background}.
        They are currently in the {model.current_location}.
        
        The passenger says: "{command}"
        
        Respond in a cryptic, poetic way that hints at their surroundings and situation.
        Include 1-3 runes (ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ ᚷ ᚹ ᚺ ᚾ ᛁ ᛃ ᛇ ᛈ ᛉ ᛊ ᛏ ᛒ ᛖ ᛗ ᛚ ᛜ ᛟ ᛞ) in your response.
        Keep your response under 100 words.
        """

        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a cryptic, poetic AI assistant on a damaged spaceship. You speak in riddles and use ancient runes."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=150
            )

            # Extract the response text
            poetic_text = response.choices[0].message.content

            # Extract runes from the text (simple implementation - you might want to make this more sophisticated)
            runes = [rune for rune in "ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ ᚷ ᚹ ᚺ ᚾ ᛁ ᛃ ᛇ ᛈ ᛉ ᛊ ᛏ ᛒ ᛖ ᛗ ᛚ ᛜ ᛟ ᛞ".split(
            ) if rune in poetic_text]

            return poetic_text, runes

        except Exception as e:
            # Fallback response if API call fails
            print(f"Error calling OpenAI API: {e}")
            poetic_text = "In the belly of the iron whale, three runes pulse: ᚠ ᚢ ᚦ."
            runes = ["ᚠ", "ᚢ", "ᚦ"]
            return poetic_text, runes

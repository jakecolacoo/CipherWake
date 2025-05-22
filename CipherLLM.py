class PoeticLLM:
    def generate_poetic_response(self, command, model):
        # This would call your LLM (e.g., OpenAI API) with a prompt that includes:
        # - Player stats
        # - Inventory
        # - Lexicon (so the AI can riff on what the player knows/doesn't know)
        # Returns a tuple: (poetic_text, [rune1, rune2, ...])
        poetic_text = "In the belly of the iron whale, three runes pulse: ᚠ ᚢ ᚦ."
        runes = ["ᚠ", "ᚢ", "ᚦ"]
        return poetic_text, runes

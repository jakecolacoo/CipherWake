class GameController:
    def __init__(self, model, view, llm):
        self.model = model
        self.view = view
        self.llm = llm

    def main_loop(self):
        while True:
            self.view.show_lexicon(self.model.lexicon)
            command = self.view.get_input("What do you do? ")
            # Update model, generate prompt, call LLM, etc.
            ai_output, runes = self.llm.generate_poetic_response(command, self.model)
            self.view.display_text(ai_output)
            self.view.display_runes(runes)
            # Decoding mechanic
            guess = self.view.get_input("Guess a rune meaning or press Enter to continue: ")
            if guess:
                rune, meaning = guess.split("=")
                self.model.lexicon[rune.strip()] = meaning.strip()

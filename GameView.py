class GameView:
    def display_text(self, text):
        print(text)
    def display_runes(self, runes):
        print("Runes: " + " ".join(runes))
    def get_input(self, prompt):
        return input(prompt)
    def show_lexicon(self, lexicon):
        print("Your Lexicon:")
        for rune, meaning in lexicon.items():
            print(f"{rune}: {meaning}")

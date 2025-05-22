class GameController:
    def __init__(self, model, view, llm):
        self.model = model
        self.view = view
        self.llm = llm
        self.game_started = False

    def start_game(self):
        # Opening sequence
        opening_text = f"""
        Darkness. Complete and utter darkness.
        
        Your consciousness returns slowly, bringing with it a dull ache in your head and the distant sound of metal creaking.
        You try to open your eyes, but... nothing. Just darkness.
        
        A voice, mechanical yet somehow melodic, breaks through the silence:
        "Awakening detected. Visual systems compromised. Emergency protocols activated."
        
        The voice continues, speaking in cryptic verse:
        "In shadows deep where light once shone,
         A vessel broken, dreams undone.
         Two paths before you now appear,
         To mend within or venture near."
        
        The ship's AI seems to be offering you a choice:
        1. Investigate the ship's damage
        2. Don your suit and explore outside
        """

        self.view.display_text(opening_text)
        self.game_started = True
        self.main_loop()

    def main_loop(self):
        while True:
            if not self.game_started:
                self.start_game()
                continue

            self.view.show_lexicon(self.model.lexicon)
            command = self.view.get_input("What do you do? ")

            # Handle initial choices
            if not self.model.has_made_first_choice:
                if "1" in command or "investigate" in command.lower() or "damage" in command.lower():
                    self.model.has_made_first_choice = True
                    self.model.current_location = "ship_interior"
                    response = """
                    You decide to assess the ship's condition first.
                    The AI's voice echoes through the darkness:
                    "Through twisted halls of metal cold,
                     A story of damage yet untold.
                     Sensors detect a breach ahead,
                     Life support systems barely fed."
                    """
                    self.view.display_text(response)
                    continue
                elif "2" in command or "suit" in command.lower() or "outside" in command.lower():
                    self.model.has_made_first_choice = True
                    self.model.current_location = "outside"
                    response = """
                    You reach for your suit, its familiar contours a comfort in the darkness.
                    The AI chimes in:
                    "Beyond these walls, a world unknown,
                     Where alien winds have freely blown.
                     Your suit will shield you from the storm,
                     But what awaits in this new form?"
                    """
                    self.view.display_text(response)
                    continue

            # Regular game loop
            ai_output, runes = self.llm.generate_poetic_response(
                command, self.model)
            self.view.display_text(ai_output)
            self.view.display_runes(runes)

            # Decoding mechanic
            guess = self.view.get_input(
                "Guess a rune meaning or press Enter to continue: ")
            if guess:
                rune, meaning = guess.split("=")
                self.model.lexicon[rune.strip()] = meaning.strip()

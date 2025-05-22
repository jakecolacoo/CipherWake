class PlayerModel:
    def __init__(self, name, background):
        self.name = name
        self.background = background
        self.stats = {"health": 10, "intuition": 7, "tech": 5}
        self.inventory = []
        self.progress = {}
        self.lexicon = {}  # Dictionary to store rune meanings
        self.has_made_first_choice = False
        self.current_location = "unknown"
        self.health = 100
        self.oxygen = 100  # For outside exploration

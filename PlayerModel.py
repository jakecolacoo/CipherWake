class PlayerModel:
    def __init__(self, name, background):
        self.name = name
        self.background = background
        self.stats = {"health": 10, "intuition": 7, "tech": 5}
        self.inventory = []
        self.progress = {}
        self.lexicon = {}  # {rune/phrase: meaning}

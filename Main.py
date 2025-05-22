from PlayerModel import PlayerModel
from GameView import GameView
from GameController import GameController
from CipherLLM import CipherLLM


def main():
    # Opening sequence
    print("\n=== CIPHERWAKE ===\n")
    print("You awaken in darkness. What is your name?")
    name = input("> ")
    print("Describe your background in a single phrase (e.g., 'exiled engineer', 'lost poet'):")
    background = input("> ")

    # Initialize game components
    model = PlayerModel(name, background)
    view = GameView()
    llm = CipherLLM()  # This can be a mock for now, or connect to OpenAI later
    controller = GameController(model, view, llm)

    # Start the game with the opening sequence
    controller.start_game()


if __name__ == "__main__":
    main()

from PlayerModel import PlayerModel
from GameView import GameView
from GameController import GameController
from CipherLLM import CipherLLM

def main():
    # Set the stage: get player info
    print("You awaken in darkness. What is your name?")
    name = input("> ")
    print("Describe your background in a single phrase (e.g., 'exiled engineer', 'lost poet'):")
    background = input("> ")

    # Initialize the band
    model = PlayerModel(name, background)
    view = GameView()
    llm = PoeticLLM()  # This can be a mock for now, or connect to OpenAI later
    controller = GameController(model, view, llm)

    # Let the jam begin
    controller.main_loop()

if __name__ == "__main__":
    main()

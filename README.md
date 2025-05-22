# CipherWake
Cipherwake

Cipherwake is a text-based, sci-fi adventure game where the player wakes up blind on a damaged spaceship. The only way to interact with the world is through a malfunctioning AI assistant that communicates in cryptic poetry and runes. The player’s main challenge is to interpret these poetic clues and symbols, gradually building a personal dictionary (lexicon) of meanings in order to navigate, repair the ship, and uncover the story.

Project Overview
	•	Genre: Interactive fiction / text adventure
	•	Setting: Sci-fi, derelict spaceship
	•	Perspective: Player is blind; all information is delivered through text
	•	AI Role: The in-game assistant acts as a “dungeon master,” but only speaks in poetic fragments and runes

Core Features
	•	Poetic AI Output:The AI generates responses in verse and symbols, not plain language.
	•	Lexicon System:Players keep track of runes and their guessed meanings, which helps them progress.
	•	Contextual Gameplay:Progress depends on interpreting clues, not just issuing commands.
	•	Iterative Learning:The more the player decodes, the more the world opens up.

Technical Structure
	•	Model:Stores player data (name, background, stats, inventory, lexicon).
	•	View:Handles all input/output, focusing on text, poetry, and runes.
	•	Controller:Manages game flow, updates the model, and interacts with the AI.
	•	Poetic LLM:Generates the cryptic, poetic responses and runes.

Getting Started
	1.	Clone the repository.
	2.	Install dependencies:⁠pip install -r requirements.txt⁠
	3.	Run the game:⁠python main.py⁠
	4.	Follow the prompts, interpret the AI’s output, and build your lexicon as you play.

Goals

Cipherwake is designed as an experiment in language, context, and player-driven discovery. The focus is on clear, iterative mechanics that encourage players to think, interpret, and adapt as they play.

Status

This project is in early development. The core framework is modular and intended for easy iteration and expansion.

Contact

For questions or contributions, please open an issue or submit a pull request.
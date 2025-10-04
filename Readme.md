Hangman Game - Save BRO!

This is a simple Hangman Game built using Pygame, where the goal is to guess a secret name to save the character "BRO". If you guess wrong, you lose health points. If you run out of health, the game is over.

Features:

A random name is selected from a list of predefined names.

The player can guess letters to reveal parts of the name.

Images update to show the current state of the game (correct guesses, incorrect guesses, and health status).

A fun and interactive gameplay experience with engaging graphics and messages.

How to Run:

Prerequisites:

You must have Python installed on your computer.

Install Pygame using pip:

pip install pygame


Clone the Repository:

Clone the repository to your local machine using:

git clone https://github.com/YOUR_USERNAME/Hangman-Game.git
cd Hangman-Game


Prepare the Game Assets:

Ensure that you have the following image files in the project folder:

6.PNG (Initial image displayed)

7.PNG (Image shown when the player wins)

1.PNG through 6.PNG (Images representing different health stages)

These image files are essential for the game to work properly.

Run the Game:

Once you have everything set up, simply run the script:

python game.py


Gameplay:

Use your keyboard to input guesses (letters from A-Z).

The goal is to guess the correct name before your health runs out.

If you guess the name correctly, you win. If not, you lose!

Game Instructions:

A random name is chosen from the list.

Letters are represented by asterisks (*).

Every time you guess a correct letter, it replaces the asterisks.

For incorrect guesses, you lose health, and the image updates accordingly.

If your health reaches 0, you lose the game, and the real word is revealed.

Contributing:

If you'd like to contribute to the project:

Fork the repository.

Create a new branch (git checkout -b feature-name).

Make your changes.

Commit and push your changes.

Open a pull request.

License:

This project is open-source and available under the MIT License.

Contact:

For any questions or feedback, feel free to reach out via Your GitHub Profile
.

Acknowledgements:

Thanks to the Pygame community for providing great tools and resources for game development!

Example of Folder Structure:
Hangman-Game/
├── 1.PNG
├── 2.PNG
├── 3.PNG
├── 4.PNG
├── 5.PNG
├── 6.PNG
├── 7.PNG
├── hangman_game.py
└── README.md

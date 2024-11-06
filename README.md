# guessless-minesweeper

	1.	Board Representation:
	•	Use a 2D array to represent the game board. Each cell can hold values indicating whether it’s empty, contains a mine, or has a number (indicating how many adjacent mines there are).
	2.	Mine Placement:
	•	Randomly place a set number of mines on the board. Ensure that no mine is placed in a cell adjacent to an already revealed cell.
	3.	Revealing Cells:
	•	Implement a function to reveal a cell. If a cell contains a mine, the game ends. If it’s empty, reveal it and recursively reveal adjacent cells (if they are also empty).
	4.	Game Logic:
	•	Allow players to reveal cells until either they hit a mine or reveal all non-mine cells. Use the numbers in cells to guide their decisions without guessing.
	5.	User Input:
	•	Capture user input for row and column selections, and validate the input to ensure it’s within the board’s bounds and not on an already revealed cell.
	6.	End Condition:
	•	The game ends when all non-mine cells are revealed or a mine is hit. Display a message indicating the outcome.
	7.	Restarting the Game:
	•	Provide an option to restart the game after it ends.

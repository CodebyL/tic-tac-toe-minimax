🎯 Game Rules<br />

* You (Human) play as ‘X’. <br />
* The AI plays as ‘O’.<br />
* The game follows Tic-Tac-Toe rules: Three in a row wins!<br />
 ___________________________________________________________________________________________________

 📌 How it Works? <br />

1️⃣ Install Python (if not already installed)<br />
* Download and install Python 3.x from python.org.<br />

2️⃣ Download the Script<br />
* Save the tic_tac_toe.py file to your computer.<br />

3️⃣ Run the Game<br />
* Open a terminal (Command Prompt or Terminal) and navigate to the folder where the file is saved.<br />
* Run the following command: **python tic_tac_toe.py**<br />

4️⃣ Play the Game<br />
* Enter a number (1-9) to place your X.<br />
* The AI will respond with O.
* Keep playing until there is a winner or a draw.
 ___________________________________________________________________________________________________

🌟 Code Explanation<br />
<br />
```board = [[" " for _ in range(3)] for _ in range(3)]```<br />
* This creates a 3x3 grid, like the Tic-Tac-Toe board.<br />
* Each cell starts out empty.<br />
<br />

``` def print_board():```
<br />

* This shows the current state of the board.<br />
* It tells the player where the Xs and Os are.<br />
<br />

```def check_winner():```
<br />

* This checks if someone has 3 in a row (horizontally, vertically, or diagonally).<br />
* Returns ‘X’ if you win, ‘O’ if the AI wins.<br />
<br />

**Minimax Func.:** ```def minimax(is_maximizing):```
<br />

* This is the brain of the AI.<br />
* If it’s the AI’s turn (is_maximizing=True), it looks for the highest score.<br />
* If it’s the human’s turn (is_maximizing=False), it looks for the lowest score (because it wants to block the player).<br />
<br />

```def best_move():```
<br />

* The AI checks all empty spots and uses minimax() to find the best possible move.<br />
<br />

```def player_move():```
<br />

* This asks the user for input (row and column), and places an ‘X’ there.<br />
<br />

```def play_game():```
<br />
* The main loop that runs the game.<br />
* You play, then the AI plays, until someone wins or the board is full.<br />

 

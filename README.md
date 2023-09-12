# Blind-Chess-Game

## Rules and commands
Welcome to the blind chess game!
This Game has two kings that function like in chess but with a twist.
Now the two can stand next to each other as well as capture each other.
Each king is a first order "Markov king" since they take turns
utilizing a transition matrix to pick their next move.

- The game starts allowing the user to pick the size of their board.
- The game ends once one King takes the other.
- Our two kings are represented by an 'X' and an 'O'
- 'X' goes first. Enjoy.

To run the game run: ```python game.py```

To run test suite run: ```python -m unittest```

Note:
For all pieces in the game their persepctive is relative to the user.
So both the 'O' and 'X' piece will interpret up as the the users
perspective which is different from chess where up for the black
king is down for the white king.

## Personal Meaning
From the age of 3 I have been playing chess against my dad and despite
the intimadating lead in wins he has collected over the years, I remain
confident that one day I shall overcome that margin. 

This game was inspired from my love of chess and computer science.
Utilizing Markhov chains to allow the Kings to make their own moves was
an interesting exploration and opens the up the possibility of utilizing these 
probabilities to create a chess AI that estimates its opponents most likely
course of action, and creates a plan according to that. In the meantime
it is satisfying to watch the blind pieces wander across the board in
hopes of capturing one another.

## Challenges and next steps
This project allowed me to relearn Python. Shifting from a Java dominant background
to Python was a challenge; however, I feel satisfied with the outcome.



# Blind-Chess-Game

## Rules and commands
Welcome to the blind chess game!
This Game has two kings that function like in chess but with a twist.
Now the two can stand next to each other as well as capture each other.
Each king is a first-order "Markov king" since they take turns
utilizing a transition matrix to pick their next move.

- The game starts allowing the user to pick the size of their board.
- The game ends once one King takes the other.
- Our two kings are represented by an 'X' and an 'O'
- 'X' goes first. Enjoy.

To run the game run: ```python game.py```

To run the test suite run: ```python -m unittest```

Note:
For all pieces in the game, their perspective is relative to the user.
So both the 'O' and 'X' pieces will interpret "UP" from the user's
perspective which is different from chess where up for the black
king is down for the white king.

## Personal Meaning
From the age of 3 I have been playing chess against my dad and despite
the intimidating lead in wins he has collected over the years, I remain
confident that one day I shall overcome that margin. 

This game was inspired by my love of chess and computer science.
Utilizing Markov chains to allow the Kings to make their own moves was
an interesting exploration and opened up the possibility of utilizing these 
probabilities to create a chess AI that estimates its opponents' most likely
course of action, and creates a plan according to that. In the meantime,
it is satisfying to watch the blind pieces wander across the board in
hopes of capturing one another.

## Challenges and next steps
This project allowed me to relearn Python. Shifting from a Java-dominant background
to Python was a challenge; however, I feel satisfied with the outcome.

Throughout the creation of the project weighting design decisions based on time
complexity and space efficiency was a key hurdle. For example, deciding how to have
the board remain in sync with the pieces about their locations. Since the pieces needed
to know their locations on the board to calculate next moves I had to figure out
a way to update the pieces' location when a move was made in the board class. I ended
up deciding that utilizing the 'Game' class as an intermediary that would
call update methods on both the King class and Board class was most efficient, since
now only x, y coordinates of the move made would need to be sent to the King and the 
Board class, versus a cost-ineffective approach of sending the entire board object to
the King class.

Another challenge arose with utilizing a universal language for moves such that any piece,
regardless of where it was on the board, could utilize the same transitions in the 
transitions matrix to make a move. For example: 

- If we had an 'X' piece at (0,0) on a 3x3 board it could move to (0,1), (1,0) or (1,1)
- Well we could encode our transition matrix to have a probability for each of those moves:
  p((0,0)|(0,1)) = 0.4
  p((0,0)|(1,0)) = 0.4
  p((0,0)|(1,1)) = 0.2
- However, say now the 'X' piece is at (1,1), now we cannot use those transitions anymore
  since our origin point is different. We can start to see that we would need to have a
  transition matrix for every square on the board to every one of its neighboring squares
  on the board. For a board of size n with 8 neighbors that is n^8. Polynomial and a horrid
  one at that.
- The solution. We utilize a common language. Think like a human would when making a move and
  we arrive at utilizing 'UPLEFT', 'UP', 'UPRIGHT', 'LEFT' ... 'DOWNRIGHT'. Now we only need
  to know the probabilities for 8 moves.
- Now, when the move picker method in King.py receives a list of x, y coordinate moves, it
  converts it utilizing the king's location into the human-readable form. Finally, it is able
  to efficiently use the Markov chain to select a move.

## Importance 
My main motivation for this project was to take the skills and coding practices I learned 
from my SWE internship into this project. From code maintainability and scalability to adhering
to sound GitHub practices, I enjoyed putting those skills to use in a personal project.

## Next Steps
In the long run, it would be exciting to allow the kings to know each others' transition matrices,
and allow them to develop plans based upon the opponent's most likely moves. Now we would be venturing
into greater than first-order Markov chains, and delving into something similar to our modern
chess AI.

## Creativity
Under the criteria that creative systems are 1) Novel and 2) Valuable, this project is not
creative. Although I cannot be certain, utilizing probabilities through Markov chains or
a similar method to enhance chess AI's has been done before. Blind chess itself is a chess
variant and an inspiration for this game. Nevetheless whether or not someone has built a quirky
blind king chess game with modified kings is doubtful. In this sense this project could be
deemed as Novel. Value beyond my own entertainment is hard to find, so I would argue this
does not meet criteria 2, and conculde this not to be a creative system.

## Credits
I would like to credit Professor Sarah Harmon for her help in teaching us about computationally
creative systems, as well as Markov chains from which this project was inspired. Her help
and feedback were instrumental to its fruition.
  


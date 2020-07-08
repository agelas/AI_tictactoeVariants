<h1>About</h1>
Player has the option to play against three (for now) different AI players which select moves randomly, using a minimax algorithm, or using tabular Q reinforcement learning.
Briefly, the minimax algorithm takes in a board position and iteratively plays moves against itself (as both X and O) to determine which move is most favorable from the given
position. This particular implementation of the algorithm is pessimistic, in the sense that it prioritizes drawing over winning.  
For the NumHangman Program 

-it is a implementation of a classic game hangman with slight modification where we predict numbers instead of a word
-the algorithm for the program.
  -a random number is generated using 'random'.
  -for the main game function we initialize all important variables for the program.
  -then we initiate while loop statement where the loop run until the attempts are maximum.
  -if statement is used to see whether a certain number has already been guessed.
    -if yes, it generates a certain output
    -else, it run the code as usual
  -if user guesses the number within maximum number of attempts, it generates a output
    -else it give an output that suggest that the game is over. 
  -finally, the main function is called.

-problem faced
  -in this program, there is a logical error where the program does not break out of the while loop after the user has correctly guessed all the characters correctly.


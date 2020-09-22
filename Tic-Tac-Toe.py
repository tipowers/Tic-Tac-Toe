# This program simulates game of tic-tac-toe

# Create a global 3X3 matrix with spaces for initial values
# Create a global player that is set to default 'O'
grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
player = 'O'

# Define main function
# Set local variable 'continueGame' to True
# Create a condition that while continueGame equals True then play another round of the game
# This involves printing the grid with updated player values each turn
# Getting the player input
# and checking the results to see if there is a winner, a loser, or a draw
def main():
    continueGame = True
    while continueGame == True:
        printGrid()
        playerInput()
        if checkResults() == 'win':
            continueGame = False
        elif checkResults() == 'tie':
            continueGame = False
            tieGame()
        else:
            changePlayer()

    gameOver()
    
    # Author
    print('\nAuthor: Tim Powers')
   
# Create printGrid function
# This displays the grid to the user by calling each value in the global matrix
def printGrid():
    print('\n---------------')
    print('|',grid[0][0],'|',grid[0][1],'|',grid[0][2],'|')
    print('\n---------------')
    print('|',grid[1][0],'|',grid[1][1],'|',grid[1][2],'|')
    print('\n---------------')
    print('|',grid[2][0],'|',grid[2][1],'|',grid[2][2],'|')
    print('---------------')

# Create playerInput function
# Create a variable named 'goodSpot' and set it to False
# When goodSpot becomes True the user input value can be placed in the matrix
# Get input from user for the row and column and put input in its respective matrix index
def playerInput():
    goodSpot = False
    while goodSpot == False:
        xRow = eval(input('\nEnter a row (0 , 1, or 2) for player ' + player + ': '))
        xColumn = eval(input('\nEnter a column(0, 1, or 2) for player ' + player + ': '))
        if grid[xRow][xColumn] == ' ':
            grid[xRow][xColumn] = player
            goodSpot = True
        
# Define checkResults function
# Parameters do not need to be passed because we are referencing a global matrix
# If matrix was not global the proper parameters would need to be passed to the function
# Logic out the winning combinations of tic-tac-toe
# If a winning combination is satisfied the checkResults function returns True
# If not the ChecResults returns False and the game continues on
def checkResults():
    if grid[0][0] == grid[0][1] == grid[0][2] != ' ' or grid[1][0] == grid[1][1] == grid[1][2] != ' ' or grid[2][0] == grid[2][1] == grid[2][2] != ' ' \
               or grid[0][0] == grid[1][0] == grid[2][0] != ' ' or grid[0][1] == grid[1][1] == grid[2][1] != ' ' or grid[0][2] == grid[1][2] == grid[2][2] != ' ' \
               or grid[0][0] == grid[1][1] == grid[2][2] != ' ' or grid[0][2] == grid[1][1] == grid[2][0] != ' ':

        return 'win'

    elif grid[0][0] == grid[0][1] == grid[0][2] == grid[1][0] == grid[1][1] == grid[1][2] == grid[2][0] == grid[2][1] == grid[2][2] != ' ':
            
        return 'tie'

    else:
        return False
    
# Define changePlayer function
# I am not sure how to begin this function
def changePlayer():
    global player
    if player == 'O':
        player = 'X'
    else:
        player = 'O'
    

# Define changePlayer function
# If you do not reference the global 'player' variable this function will try to create a local 'player' variable
# This will no doubt throw an error
# During each iteration the changePlayer function is invoked which verifies the current player and changes to the opposite player
def gameOver():
    print('\nPlayer', player, 'won!')

def tieGame():
    print('\nTie game!')

# Call main function
main()



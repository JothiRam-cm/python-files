import pyttsx3
engine=pyttsx3.init()
voices = engine.getProperty('voices')
preferred_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
engine.setProperty('voice', preferred_voice_id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Test the voice
speak("""Sure, let's go through the code step by step:

The SnakeAndLadder class is defined to encapsulate the logic for the game. It contains a constructor where the board configurations are defined, including the positions of snakes and ladders.

The play_game method within the SnakeAndLadder class simulates the game based on the die inputs provided. It takes a list of die roll values as an argument.

Inside the play_game method:

current_position is initialized to 0, representing the player's starting position.
snakes_encountered and ladders_encountered are initialized to 0 to keep track of how many snakes and ladders the player encounters during the game.
The method iterates through each die roll in the moves list. For each move, it checks if the new position (current position + move) is within the bounds of the board (<= 100).

If the new position is within bounds, the current position is updated accordingly. If the current position is a snake or a ladder position, the player's position is further updated according to the rules of the game.

If the player's position reaches 100, the game is considered to be won, and the method returns "Possible" along with the number of snakes and ladders encountered during the game.

If the player's position does not reach 100 even after using all the die inputs, the method returns "Not possible" along with the number of snakes and ladders encountered and the position where the player's coin ends.

Finally, in the main block, an instance of the SnakeAndLadder class is created. The input die roll values are taken from the user as a space-separated string of integers and converted into a list of integers.

The play_game method is called with the die roll values, and the result is printed based on the returned values.

The code is designed to determine whether a player can reach the end of the Snake and Ladder board based on the die inputs and provides the number of snakes and ladders encountered during the gameplay""");
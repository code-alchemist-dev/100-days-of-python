# Treasure Island Adventure Game

## Instructions

Create your own "Choose Your Own Adventure" game by implementing conditionals such as `if`, `else`, and `elif` statements to structure the logic and pathways of your story.

You can refer to the flowchart from draw.io for guidance while writing the code. However, the most enjoyable part is crafting your own unique story 😊.

🧞‍♂️ 🐊 🧙‍♂️ 🧟 🧚‍♂️ 🧝‍♂️ 🥷 🤖 👽 🙀

If you prefer to continue with my example, feel free to use the following text snippets:

## Example Text Snippets

1. "You are at a crossroad. Where would you like to go? Type 'left' or 'right'."
2. "You have reached a lake with an island in the center. Type 'wait' to wait for a boat or 'swim' to swim across."
3. "You arrive at the island safely. There is a house with three doors: one red, one yellow, and one blue. Which color do you choose?"
4. "It's a room filled with fire. Game Over."
5. "You have found the treasure! You Win!"
6. "You enter a room full of wild beasts. Game Over."
7. "You chose a door that does not exist. Game Over."
8. "You are attacked by an angry trout. Game Over."
9. "You fell into a hole. Game Over."

## Escaping Characters

When using multiple sets of quotes within a single string, you may need to "escape" some of them with a backslash `\`. For example, see the sentence: "You are at a crossroad...". More information on escaping characters can be found [here](https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals).

## Extensions

Consider how you can make your program case-insensitive to a player's responses. For instance, the program should recognize "left" and "Left" as the same input.

You can also incorporate your own ASCII art into the game. To do this, use three single quotes `'''` at the beginning and the end of your artwork to create a multi-line string.

Here is an example of the structured adventure game using the provided snippets:

```python
print("You are at a crossroad. Where would you like to go? Type 'left' or 'right'.")
choice1 = input().lower()

if choice1 == 'left':
    print("You have reached a lake with an island in the center. Type 'wait' to wait for a boat or 'swim' to swim across.")
    choice2 = input().lower()
    if choice2 == 'wait':
        print("You arrive at the island safely. There is a house with three doors: one red, one yellow, and one blue. Which color do you choose?")
        choice3 = input().lower()
        if choice3 == 'red':
            print("It's a room filled with fire. Game Over.")
        elif choice3 == 'yellow':
            print("You have found the treasure! You Win!")
        elif choice3 == 'blue':
            print("You enter a room full of wild beasts. Game Over.")
        else:
            print("You chose a door that does not exist. Game Over.")
    else:
        print("You are attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
```

Enjoy creating your own adventure!
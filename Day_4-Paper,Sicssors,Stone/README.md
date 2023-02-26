Rock Paper Scissors
- Mini game of the traditional paper, scissors, stone
- AIM: Understanding randomization and Lists

Instructions
- Make a rock, paper, scissors game.
- Inside the main.py file, you'll find the ASCII art for the hand signals already saved to a corresponding variable: rock, paper, and scissors. This will make it easy to print them out to the console.
- Start the game by asking the player:
- "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."
![image](https://user-images.githubusercontent.com/100339175/221402306-32563335-65c3-4e9a-a55a-d071713bf3ba.png)


LEARNING

+++++++++++++++++++++++++++++++++++++
- Module: random — Generate pseudo-random numbers (https://docs.python.org/3/library/random.html)
- Snytax : randint(start, end)
- Parameters: (start, end) : Both of them must be integer type values.
- Returns: A random integer in range [start, end] including the end points.
- Example: r1 = random.randint(0, 10) - Returns a number from 0 to 10

+++++++++++++++++++++++++++++++++++++
- Python Lists 
- Lists are used to store multiple items in a single variable.
- List items are ordered, changeable, and allow duplicate values.
- List items are indexed, the first item has index [0], the second item has index [1] etc.
- Example: mylist = ["apple", "banana", "cherry"] 

+++++++++++++++++++++++++++++++++++++
- Combine List and random module.choice()
- The choice() method returns a randomly selected element from the specified sequence.
- Example: mylist = ["apple", "banana", "cherry"]
- print(random.choice(mylist))

+++++++++++++++++++++++++++++++++++++
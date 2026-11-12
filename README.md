# Simulating a Day in the Life as a Holy Cross Student

## Game Description:
### This game simulates a day in the life of a college student, inspired by Alex's actual schedule! The user will make decisions throughout the day and recieve points based on those choices. At the end of the day, all points will be added and the user will either win or lose based on their productivity (to Alex's standards)

## Game Instructions:
1) Start the game by running the Python program.
2) Answer each prompt about your daily choices and activities. 
3) Be careful to follow input instructions!
4) Some events in the game are random, just like they would be in day to day life.
5) Every choice you make will either gain or lose points!
6) Once you have gone through the whole day, your total points will be calculated.
7) If you reach a certain threshold, you win! Otherwise, try again to see what a more productive day would look like!

## User State Representation
Throughout the day, the game displays how many points the user gains or loses after each decision or event. At the end of the game, the final point count will be displayed and a win or loss is declared. However, the game does not keep a total of the points throughout the day, you only get a total at the end. The game not displaying total points throughout the game is meant to encourage honest choices, not ones just trying to get a higher score. Sometimes, not every day is our most productive and that's ok. 

## Control Flow
All components of the game are included and ran in the main() function, which calls each individual function from day_functions.py to simulate a day in the life of a Holy Cross student. 

Each function from day_functions.py represents a different part of the day and determines productivity based on user input, conditional statements, and occassionally randomness. Each day function that uses user input calls a separate input function from user_input.py to collect and validate responses. The functions in user_input mainly use while loops and exception handling to validate all responses. 

The random module is also incorporated in certain fucnctions to keep each game unique. For example part of the 9am function involves randomness to determine how crowded campus is, and therefore if the user makes it on time to class or not. The TA office hours function also utilizes randomness to determine if students attend or not. 

Each function keeps track of and returns the productivity points earned by the user during that portion of the day. Once all day functions have been run, a total is calculated in the main() function using sum(), and uses conditional statements to determine if the winner wins or looses based on their total points. 
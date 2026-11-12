from day_functions import *
from user_input import*

def main():
    """
    Puts all Holy Cross Day in the life functions 
    together to simulate user's day in the life
    and to find the overall productivity of the day
    and determine if the user won or lost. 
    """
    name=get_name()
    welcome(name)

    points=sum(
        [eight_am(),
         nine_am(),
         ten_to_eleven(),
         calc_participation(),
         twelve_to_three(),
         office_hours(),
         dinner(),
         bedtime()]
         )
    
    print(f"Your total score is {points}!")

    if points>=60:
        print("You win! You had a great day and got a lot done!")
    elif points>=45:
        print("You win! You had a solid day.")
    else:
        print("You lost! Try to be more productive tomorrow!")

    print(f"Thanks for playing {name}! Come back soon!")

if __name__=="__main__":
    main()

















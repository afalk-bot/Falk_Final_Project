from user_input import *
from constants import AFTERNOON_ACTIVITIES, DINNER_OPTIONS
import random

def welcome(name):
    """
    Asks for user's name and welcomes them into game

    Output: Welcome message
    """
    print(f"Welcome to a Day in the Life at Holy Cross {name}!\n"
          "Answer the following questions about your\n"
          "day's routine to see how productive you are!\n"
          "Let's get started!")


def eight_am():
    """
     Determines if user wakes up on time for 8am class 
     and other morning accomplishments. 

    Calls mins_before_8() to collect valid user input

    Output: Message about how morning went and 
            number of points gained or lost. 
    """
    print("Good Morning! You have class at 8am!")
    mins=mins_before_8()
    points=0 

    if mins>=60:
        points=10
        result= ("Great start to the day!\n"
        "You have time to study, get a coffee,\n" 
        "and make it to class on time!")
    elif mins<60 and mins>30:
        points=5
        result=("Good start to the day!\n" 
        "You have time to get a coffee\n"
        "and you get to class on time")
    elif mins<=30 and mins>20:
        points=3
        result=("You wake up to make class on time,\n"
        "but no time for coffee!")
    elif mins<=20 and mins>5:
        points=-3
        result=("You're late to class :(")
    else:
        points=-10
        result=("You missed your 8am.")
    
    print(result)
    print(F"You earned {points} productivity points")

    return points


def nine_am():
    """
    Determines if user makes it on time to 9 am
    based on how many minutes before they leave, 
    and if campus is crowded. 

    Inputs: 
    Calls mins_before_9 function to get valid number of minutes 
    before class user left.  

    Outputs: Whether or not user is on time, late, or don't make 
    it to class, and the points they gained or lost.
    """
    print("Now it's time for your 9am Python class!")

    points=0

    leave_for_nine_am=mins_before_9()

    random_num=random.random()
    is_crowded=random_num>0.5

    if leave_for_nine_am>=5:
        points=3
        result=("You make it to Python on time!")
    
    elif 1<=leave_for_nine_am<5:
        if is_crowded:
            points=-3
            result=("You were late to Python!")
        else:
            points=2
            result=("On time to Python")
    else:
        points=-10
        result=("You missed your Python class!")
    
    print(result)
    print(f"You earned {points} productivity points")

    return points


def ten_to_eleven():
    """
    Determines number of productivity points gained in 
    hour between Python class and Calc class based on 
    activities completed during that time. 
    
    Calls breakfast(), assignments(), and 
    studied() functions to get valid list of
    user's answers about the hour

    Outputs: Number of productivity points gained/lost
    """

    print("It's now 10am. You have an hour until calc at 11.\n" 
    "Try to make good use of this hour!")

    points=0
    
    eat_breakfast=breakfast()
    assignments_done=assignments()
    study=studied()
    
    if not eat_breakfast and assignments_done<1 and not study:
        points=-10
        result=("You were not productive.")
    elif eat_breakfast and study and assignments_done>=1:
        points=10
        result=("Great job, you were very productive!")
    elif (
        (eat_breakfast and not study and assignments_done<1) or 
        (not eat_breakfast and study and assignments_done<1) or
        (not eat_breakfast and not study and assignments_done>=1)):
        points=3
        result=("Nice, you did something productive")
    else:
        points=5
        result=("Great Work! You were productive!")
    
    print(result)
    print(f"You earned {points} productivity points")

    return points
    
    
def calc_participation():
    """
    Rewards productivity points based on how many times 
    user participates in 11am calc class

    Calls participate() for valid number of time participated

    Output: Statement of number of time participated and the points
    gained or lost.
    """
    print("It's now 11am and time for calc class.")
    points=0
    participate_count=participate()

    if participate_count<1:
        points=-5
        result=("You didn't participate in class")
    elif participate_count==1:
        points=1
        result=("You participated once. Nice!")
    elif participate_count ==2:
        points=2
        result=("Good participation!")
    else:
        points=3
        result="That was a super productive Calc class!"

    print(result)
    print(f"You earned {points} productivity points")
    
    return points


def twelve_to_three():
    """
    Allow user to choose how to spend their afternoon
    and calculate productivity based on decisions.
    Incorporate randomnes to determine how afternoon 
    really goes, and productivity points that result. 

    Call three_activities() function for chosen activities
    to get list of activities

    Output: Number of productivity points
    """
    
    print("It's now noon and you have 3 hours until your next scheduled event.\n" 
          "Let's see how you spend this time! \n"
          "Some activities may not go as planned!")

    completed_activities=three_activities()
    points=0
        
    for activity in completed_activities:
        activity_points=AFTERNOON_ACTIVITIES[activity]

        outcome=random.choice(["Good","Good","Bad"])
        
        if outcome=="Good":
            print(f"{activity} went well and was productive!")
            activity_points+=2
        else:
            print(f"Uh oh, {activity} didn't go as planned!")
            activity_points-=2
        
        points+=activity_points
        print(f"You earned {activity_points} points for {activity}!\n")
        
    print(f"You earned {points} productivity points")
    
    if points>=8:
        print("You had a productive afternoon!")
    else:
        print("You could have been more productive.")
        
    return points

    
def office_hours():
    """
    Randomly determines if students show up for help,
    and if they don't, how many assignments you get to grade. 
    """
    print("Now it's time for your TA office hours from 3-5")

    students_come=random.random()<0.4

    if students_come:
        points=10
        print("Students attended office hours so you helped them. Very productive!")
    else:
        print("No students showed up. Time to grade assignments!")

        number_assignments=num_assignments_input()

        assignments_graded=random.randint(0,number_assignments)
        print(f"You graded {assignments_graded} out of {number_assignments} during office hours.")

        if assignments_graded==number_assignments:
            points=10
            print("Awesome job, you finished all grading!")
        elif assignments_graded>=number_assignments/2:
            points=5
            print("Good work, you finished at least half of grading!")
        elif assignments_graded>number_assignments/4:
            points=3
            print("Nice, you got some grading done")
        elif assignments_graded>0:
            points=1
            print("You made some progress grading")
        else:
            points=-10
            print("You could have been more productive during this time.")
        
    print(f"You earned {points} productivity points")
    
    return points
 

def dinner():
    """
    Collects user input about choice of affordable 
    dinner option and awards productivity points
    based on input

    Calls money_input() and dinner_choice_input()
    to collect and validate user input

    Output: Number of productivity points earned
    """

    print("Now it's dinner time!")
    
    money=money_input()
    
    affordable=[]
    for option in DINNER_OPTIONS:
        if DINNER_OPTIONS[option]<=money:
            affordable.append(option)
    print(f"You can afford these dinner options: {affordable}")

    dinner_choice=dinner_choice_input(affordable)

    if dinner_choice=="Kimball":
        points=10
    elif dinner_choice=="Croads":
        points=8
    elif dinner_choice=="Pick up fast food":
        points=5
    elif dinner_choice=="Doordash":
        points=3
    elif dinner_choice=="Sitdown Restaurant":
        points=1
    
    cost=DINNER_OPTIONS[dinner_choice]
    money=money-cost

    print(f"You chose the dinner option:{dinner_choice}\n"
          f"You have {money} dollars remaining.\n"
          f"You earned {points} points based on how much you spent.\n")
    
    return points

    
def bedtime():
    """
    Determines prodcutvity points based on how much
    time the user spends scrolling before bed.

    Calls phone_time_input() to collect valid number of minutes

    Output: Number of productivity points earned
    """

    print("That was a long day, time for bed!")

    phone_time=phone_time_input()
    
    if phone_time==0:
        points=15
    elif phone_time<15:
        points=10
    elif phone_time<30:
        points=5
    elif phone_time<45:
        points=3
    else:
        points=0
    
    print(f"You spent {phone_time} minutes scrolling.\n"
          f"You get {points} points")
    
    return points
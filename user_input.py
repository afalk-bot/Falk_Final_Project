
from constants import AFTERNOON_ACTIVITIES

def get_name():
    """
    Asks for user's name and validates

    Output: Valid name given by user 
    """
    while True:
        name=input("Hello! What is your name?").strip()

        if not name.replace(" ","").isalpha():
            print("Please enter a valid name!")

        elif len(name)>15:
                print("Please enter a shorter name")
        
        else:
            return name
    

def mins_before_8():
     """
     Collects the number of minutes prior to
     8 am the user wakes up and validates input

     Output: Valid number of minutes before class
     """
     
     while True:
          try: 
               mins=int(input("How many minutes before 8am did you wake up?"))

               if 0<= mins <=180:
                    return mins
               else:
                    print("Please enter a number between 0 and 180!!")
                    
          except ValueError:
               print("Please enter a valid whole number!")
    

def mins_before_9():
     """
     Collects and validates number of mins
     before 9am student leaves for class

     Output: Valid number of minutes before 9 user leaves
     """
     while True:
          try: 
               mins=int(input("How many minutes before your\n" 
               "9am class did you leave?"))

               if -5<= mins <=45:
                    return mins
               else:
                    print("Please enter a number between -5 and 45!")
      
          except ValueError:
               print("Please print a valid whole number!")


def breakfast():
     """
     Asks if the user ate breakfast

     Output: Boolean indicating whether the user ate breakfast
     """
     while True:
          answer=input("Did you eat breakfast? (yes/no)").strip().lower()

          if answer== "yes":
               return True
          elif answer == "no":
               return False
          else:
               print("Please enter yes or no!")

def studied():
     """
     Asks if the user studied 

     Output: Boolean indicating whether the user studied
     """
     while True:
          answer=input("Did you study? (yes/no)").strip().lower()

          if answer== "yes":
               return True
          elif answer == "no":
               return False
          else:
               print("Please enter yes or no!")


def assignments():
     """
     Collects and validates number of assignments completed 
     by the user 

     Output: Valid number of assignments completed
     """
     while True:
          try:
            answer=int(input("How many assignments did you complete?"))
            if 0<=answer<=5:
                return answer
            else: 
               print("Please enter a number between 0 and 5!")
        
          except ValueError:
               print("Please enter a valid whole number!")


def participate():
      """
      Collect and validate number of times 
      participated in calc class

      Output: Valid number of times participated
      """
    
      while True:
           try:
                participate=int(input("How many times did you participate in calc today?"))
                if 0<=participate<=10:
                    return participate 
                else:
                    print("Please enter a number between 1 and 10")
           except ValueError:
                print("Please enter a valid whole number!")


def three_activities():
     """
     Collects and validates user input 
     for their activities between 12 and 3. 

     Output: List of 3 activities completed
     """
     
     hours=[1,2,3]
     completed=[]

     for hour in hours:
          print("Available Activities:")
          for option in AFTERNOON_ACTIVITIES:
               print(option)
          
          activity=input(f"Which activity will you do during hour {hour}")
          
          while activity not in AFTERNOON_ACTIVITIES:
               print("Invalid activity!")
               activity=input(f"Which activity will you do during hour {hour}")

          completed.append(activity)
     
     return completed


def num_assignments_input():
     """
     Collects and validates number of assignments 
     user needs to grade

     Output: Valid integer of assignments
     """
     while True:
          try:
               assignments=int(input("How many papers do you have to grade this week?"))

               if 0< assignments <200:
                    return assignments
               else:
                    print("Invalid input! \n" 
                     "Enter a positive whole number between 0 and 200!")
          except ValueError:
               print("Invalid input! Enter a positive whole number!")
     
     
def money_input():
     """
     Collects and validates amount of money
     user has available for dinner

     Output: Valid float representing money balance
     """ 

     while True: 
          try:
               money=float(input("How much money do you have to spend on dinner?"))

               if money>=0:
                    return money
               else:
                    print("Imvalid input! Enter a positive number!")
          except ValueError:
               print("Invalid Input! Enter a valid number!")


def dinner_choice_input(affordable):
     """
     Collects and validates user's dinner
     choice based on what they can afford

     Input: List of afforable dinner options
          based on user's money.
     
     Output: Valid dinner choice
     """

     choice=input("What will you have for dinner?")

     while choice not in affordable:
          print("Invalid choice! Choose from affordable options!")
          choice=input("What will you have for dinner?").strip()
     
     return choice

def phone_time_input():
     """
     Collects and validates amount of time
     user decides to scroll before bed

     Output: Positive float representing minutes.
     """

     while True:
          try:
               time=float(input("How many minutes did you spend scorlling before bed?"))
               if 0<=time<float(500):
                    return time
               else:
                    print("Invalid Input! Enter a number between 0 and 500!")

          except ValueError:
               print("Invalid Input! Please enter a number!")
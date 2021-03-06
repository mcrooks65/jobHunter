# TODO 
# DONE Save schedule interview date   # STORING IN AN ARRAY FOR MULTIPLE DATES
# Still requires new interview function to run when day matches.
# Create Cultural Interview function, will run first thing on scheduled days.  
# Add cultural interivew practice function and new stat to gauge cultural interview aptitutde.  (Number based skills rating 1 is novice 5 can be max)
# Add technical interview schedule follow up email message, to schedule the technical interview.
# Create Technical Interview function, will run first thing on scheduled days.
# Add technical interview practice function and new stat to gauge technical interview aptitutde.  (Number based skills rating 1 is novice 5 can be max)
# May need to add new selection to action_menu() to view current schedule.

import time

#Initialize date and several stats
date = 1
player_energy = 100 
player_stress = 0
application_count = 0
email_inbox = 0
cult_int_date = []

def action_menu():
    display_stats()
    print_choices()

def check_email():
    global date 
    global email_inbox
    global cult_int_date

    if email_inbox == 0:
        print("You have no messages from potential employers.  Better get more applications out!")
        time.sleep(1)
        action_menu()
    elif email_inbox == 1:
        print("You have " + str(email_inbox) + " message in your inbox.")
        time.sleep(1)
        player_input = input("Will you open this message? ")
        if player_input == 'y':
            print("You got a response from Techrosoft!  They'd like to schedule a cultural interview to see if you'd be a good fit!" )
            time.sleep(1)
            print("You tap out a response email and secure the interview for Day " + (str(date + 3)))
            cult_int_date.append(date+3) # WHY WONT THIS UPDATE? >_<  It's fine till it exits the function.
            time.sleep(1)
            print("You make sure to put the interview in your calender... Got it! All set for Day " + str(cult_int_date.pop()))
            time.sleep(1)
            print("Good work!  Securing interviews is a neccessary first step to landing a job!")  #If i'm going to add a point system this ought to be one of the things that adds score.
            time.sleep(1)
            email_inbox -= email_inbox
        elif player_input == 'n':
            print("You decide you'd rather not go forward with the offer and delete the email")
            time.sleep(1)
            email_inbox -= email_inbox
            print("You can't help but feel like this is counter productive...")
            time.sleep(1) 
            action_menu()
        else:
            print("You will need to respond with 'y' or 'n'.")
            time.sleep(1)
    
        action_menu()
    elif email_inbox >= 2:
        print("You have " + str(email_inbox) + " messages in your inbox.")
        time.sleep(1)
        player_input = input("Will you open the top message? ")
        if player_input == 'y':
            print("You got a response from Techrosoft!  They'd like to schedule a cultural interview to see if you'd be a good fit!" )
            time.sleep(1)
            print("You tap out a response email and secure the interview for Day " + (str(date + 3)))
            time.sleep(1)
            print("Good work!  Securing interviews is a neccessary first step to landing a job!")  #If i'm going to add a point system this ought to be one of the things that adds score.
            time.sleep(1)
            email_inbox = email_inbox -1
        elif player_input == 'n':
            print("You decide you'd rather not go forward with the offer and delete the email")
            time.sleep(1)
            email_inbox = email_inbox -1
            print("You can't help but feel like this is counter productive...")
            time.sleep(1) 
            action_menu()
        else:
            print("You will need to respond with 'y' or 'n'.")
            time.sleep(1)
        action_menu()

def apply_to_job():
    print("Browsing around on Indeed.com you find a developer postion that ought to fit and go through the applicaiton process")
    
    global application_count
    global player_energy 
    global player_stress

    if player_energy < 20:
        print("You're too tired to fill out anymore applicaitons today!  Go get some rest.")
        action_menu()
    elif player_energy >= 20:
        application_count += 1
        player_energy = player_energy - 20
        player_stress = player_stress + 10
        action_menu()

def play_vidya_games():
    global player_stress
    global player_energy

    if player_energy == 0:
        print("You're too tired to play games, you should really just go to bed.")
        time.sleep(1)
        action_menu()
    else:
        player_energy = 0 # Once you start with games you don't stop, lose all energy for the day!
        if player_stress >= 50:
            player_stress -= 50 # game playing currently removes 50 stress
        else:
            player_stress = 0 # 0 out stress if it's less than 50
        print("You sit down saying you'll just 'play for a little while', and then it's 3 AM and you've no choice but to sleep.")
        time.sleep(1)
        action_menu()

def go_to_sleep():
    print("You go to bed and rest up for another day of job hunting.")
    global player_energy 
    global player_stress
    global date
    global application_count
    global email_inbox
    global cult_int_date

    player_energy = 100
    if player_stress <= 25:
        player_stress = 0
    else:
        player_stress = player_stress - 25
    date += 1
    if application_count > 3: # Add chance to receive email of positive response from employer depending on how many applications were sent.  This will need to be adjusted... 
        email_inbox += 1

    ## WIP
    # if not cult_int_date: #Handles in case of empty array.
    #     print("Good Morning!  You have no cultural interviews scheduled today.")
    #     time.sleep(1)
    # else:
    #     if date != cult_int_date[0]:
    #         print("Good Morning!  You have no cultural interviews scheduled today.")
    #         time.sleep(1)
    #     else:
    #         Print("Good Morning!  You have a cultural interview today!")
    #         time.sleep(1)
    #         # cultural_interview() ##!Still need to define!

    action_menu()
    
def display_stats():
    # global cult_int_date

    print("Day " + str(date))
    # if len(cult_int_date) == 0:
    #     print("You have no interviews scheduled.")
    # else:
    #     print("Upcoming Interview(s): " + cult_int_date[0])
    print("Energy: " + str(player_energy))
    print("Stress: " + str(player_stress)) 
    print("Applications Sent: " + str(application_count))

def print_choices():
    print("What will you do?")
    print("1) Check Email (Does not cost energy)")
    print("2) Apply to a job (Cost: 20 energy 5 Stress)")
    print("3) Cultural Interview Practice (UNDER CONSTRUCTION)")
    print("4) Technical Interview Practice (UNDER CONSTRUCTION)")
    print("5) Vidya Games (Removes up to 50 stress.  Energy will be depleted!)")
    print("6) Sleep (Go to next Day, recover 100 energy (maxes at 100), relieve 25 stress")
    player_input = input("Select your next action: ")
    
    if player_input == "1":
        check_email()
    elif player_input == "2":
        apply_to_job()
    elif player_input == "3":
        print("UNDER CONSTRUCTION")
    elif player_input == "4":
        print("UNDER CONSTRUCTION")
    elif player_input == "5":
        play_vidya_games()
    elif player_input == "6":
        go_to_sleep()
    elif player_input == "7":
        print(cult_int_date)
    else:
        print("You need to select 1-6!")
        time.sleep(1)
        print_choices()
        
def main():
    print("Welcome to Job Hunter v0.1")
    time.sleep(1)
    player_name = input("What's your name? > ")
    print("Welcome to Job Hunter " + player_name + "!  It's time to carpe some diem!") 
    time.sleep(2)

    print("THE RULES OF Job Hunter: To win Job Hunter all you need to do is accept an offer to work at any company!  Start by sending out applications, then work your way through numerous stages of interviews until you get a job offer!")
    print("Not a good enough offer?  Get a higher end game score by securing a better job!")

    action_menu()
    
if __name__ == '__main__':
    main() 
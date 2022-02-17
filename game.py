import time


def check_email():
    print("You have no messages from potential employers.  Better get more applications out!")

def apply_to_job():
    print("Browsing around on Indeed.com you find a developer postion that ought to fit and go through the applicaiton process")
    #global application_count
    #application_count = application_count + 1
    #player_energy = player_energy - 20
    #player_stress = player_stress + 5

def display_stats():
    #Initialize date and several stats
    date = 1
    player_energy = 100 
    player_stress = 0
    application_count = 0

    print("Day " + str(date))
    print("Energy: " + str(player_energy))
    print("Stress: " + str(player_stress)) 

def print_choices():
    print("What will you do?")
    print("1) Check Email (Does not cost energy)")
    print("2) Apply to a job (Cost: 20 energy 5 Stress)")
    print("3) Cultural Interview Practice (UNDER CONSTRUCTION)")
    print("4) Technical Interview Practice (UNDER CONSTRUCTION)")
    print("5) Vidya Games (UNDER CONSTRUCTION)")
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
        print("UNDER CONSTRUCTION")
    elif player_input == "6":
        print("You go to bed and rest up for another day of job hunting.")
        #player_energy = 100
        #player_stress = player_stress - 25
        #global date
        #date += 1
    else:
        print("Okay fine bye then!")

def main():
    print("Welcome to Job Hunter v0.1")
    time.sleep(1)
    player_name = input("What's your name? > ")
    print("Welcome to Job Hunter " + player_name + "!  It's time to carpe some diem!") 
    time.sleep(2)

    print("THE RULES OF Job Hunter: To win Job Hunter all you need to do is accept an offer to work at any company!  Start by sending out applications, then work your way through numerous stages of interviews until you get a job offer!")
    print("Not a good enough offer?  Get a higher end game score by securing a better job!")

    display_stats()
    print_choices()

    
if __name__ == '__main__':
    main()
import time

def main():
    print("Welcome to Job Hunter v0.1")
    time.sleep(1)
    player_name = input("What's your name? > ")
    print("Welcome to Job Hunter " + player_name + "!  It's time to carpe some diem!") 
    time.sleep(2)
    print("THE RULES OF Job Hunter: To win Job Hunter all you need to do is accept an offer to work at any company!  Start by sending out applications, then work your way through numerous stages of interviews until you get a job offer!")
    print("Not a good enough offer?  Get a higher end game score by securing a better job!")

    #Initialize date and several stats
    date = "Day 1"
    player_energy = 100 
    player_stress = 0

    print(date)
    print("Energy: " + str(player_energy))
    print("Stress: " + str(player_stress)) 

if __name__ == '__main__':
    main()
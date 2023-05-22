import random
response = input("Do you want to roll the dice(y/n): ")
def counter(response):
    if response == 'y':
      no = random.randint(1,6)
      if no ==1:
        print("[     ]")
        print("[  o  ]")
        print("[     ]")
      if no ==2:
        print("[     ]")
        print("[o   o]")
        print("[     ]")
      if no ==3:
        print("[o    ]")
        print("[  o  ]")
        print("[    o]")
      if no ==4:
        print("[o   o]")
        print("[     ]")
        print("[o   o]")
      if no ==5:
        print("[o   o]")
        print("[  o  ]")
        print("[o   o]")
      if no ==6:
        print("[o   o]")
        print("[o   o]")
        print("[o   o]")
    elif response =='n':
      print("Program exited")
    else :
      print("Invalid response")
counter(response)
print("Hello and welcome to slightly modified NetworkChuck's coffee lab")

name = input("What is your name?")
if name == "Ben":
    evil_status = input("Are you evil Ben\n").lower()
    good_deeds = int(input("how many good deeds have you done today?"))
    if evil_status == "yes" and good_deeds <4:
        print("Your not welcome here")
        exit()
    else:
      print("Hello, " + name + " Thank you so much for coming in today\n\n\n")
    
else:
    print("Hello, " + name + " Thank you so much for coming in today\n\n\n")

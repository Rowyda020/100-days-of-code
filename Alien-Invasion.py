print('''
     o   o
      )-(
     (O O)  안녕
      \=/
     .-"-.
    //\ /\\
  _// / \ \\_
 =./ {,-.} \.=
     || ||
     || ||    
   __|| ||__  
  `---" "---'  
         _   _            
        | | (_)           
  __ _  | |  _    ___    _ __  
 / _` | | | | |  / _ \  | '_ \ 
| (_| | | | | |  |__/   | | | |
 \__,_| |_| |_|  \___|  |_| |_|                                          
''')
print("On your way back home after a long day at work, you found an alien on the middle of the road")
first = int(input("Would you\n1)Talk to it  2)Run away? "))
if first == 1:
  score+=1
  second = int(input("Mr.Anter <3 gave you two stones to choose from.\nWhich one would you pick?\n1)Blue 2)Red? "))
  if second ==2:
    print("Phew! that was the right choice. ")
    third = int(input("It then asked you who is the greatest band of all time?\n1)The beatles 2)Nirvana 3)Queen "))
    if third ==3:
      print("CONGRATULATIONS! You are now bestfriends")
      last = input("Mr.Alien asked you if you want to go home with it? Y OR N? ").lower()
      if last == "y":
        print("Mr.Alien took you to his homeland KWEST where they worship Kanye West.")
      else:
          print("Mr.Alien gave you a ride back home,tuck you into bed and gave you a goodnight kiss ")
    else:
      print("Mr.Alien shook his head in disgust and left.\nGAME OVER")
  else:
    print("Mr.Alien hit you in the head with the stone and ran away with your dead body.\nGAME OVER")
else:
  print("You went back home safely -_-\nGAME OVER")

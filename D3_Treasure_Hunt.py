print('''
*************************************************************
         _,-._
        ; ___ :           ,------------------------------.
    ,--' (. .) '--.__    |          Welcome to            |
  _;      |||        \   |       Treasure Island !        |
 '._,-----' ';=.____,"   |        Your mission is         |
   /// < o>   |##|       |      to find a treasure !      |
   (o        \`--'       //`-----------------------------'
  ///\ >>>>  _\ <<<<    //
 --._>>>>>>>><<<<<<<<  / 
 ___() >>>[||||]<<<<
 `--'>>>>>>>><<<<<<<
      >>>>>>><<<<<<
        >>>>><<<<<
         >>ctr<<
*************************************************************
''')
first_pick = input("You're at the crossroad, choose your road wisely.\nWhich way will you take? Type 'right' of 'left'. ").lower()
if first_pick == "left":
  print("You continue down the left path...")
  second_pick = input("You have reached a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ").lower()
  if second_pick == "wait":
    print("Good things come to those who wait. You take the boat.")
    third_pick = input("You have reached the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").lower()
    if third_pick == "red":
      print("You were burned by fire flames. Game Over.")
    elif third_pick == "blue":
      print("You were eaten by hungry pirates. Game Over.")
    elif third_pick == "yellow":
      print("You found the treasure! You Win!")
    else: 
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You were attacked by an angry trout. Game Over.")
else: 
  print("You fell into a hole. Game Over.")

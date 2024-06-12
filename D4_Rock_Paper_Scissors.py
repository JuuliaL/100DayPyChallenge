import random
greeting = 'Welcome to the Rock Paper Scissors Game!'
print(greeting)
rock = '''
                _....._
             .;;'      '-.
           .;;: _         '.
          /;;:' _           ;
         |;;:'_              |
         |;;: _              |
         |;;::.              |
          \;;::.            /
           ';;::.         .'
             '-;;:..___.-'

'''
paper = '''
             _______________
        ()==(              (@==()
             '______________'|
               |             |
               |             |
             __)_____________|
        ()==(               (@==()
             '--------------'
     '''
scissors = '''
                _    _
               (_)  / )
                 | (_/ 
                _+/  
               //|\`
              // | )
             (/  |/   
 '''
images = [rock, paper, scissors]
user_action = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

if user_action >= 3 or user_action < 0:
  print('You typed an invalid number, you lose!')
else: 
  print(f'You chose:\n {images[user_action]}')
  rand_action = random.randint(0,2)
  print(f'Computer chose:\n {images[rand_action]}')
  
  if user_action == rand_action:
    print(f"Both players selected {user_action}. It's a tie!")
  elif user_action == 0:
    if rand_action == 2:
      print("Rock smashes scissors! You win!")
    else:
      print("Paper covers rock! You lose.")
  elif user_action == 1:
    if rand_action == 0:
      print("Paper covers rock! You win!")
    else:
      print("Scissors cuts paper! You lose.")
  elif user_action == 2:
    if rand_action == 1:
      print("Scissors cuts paper! You win!")
    else:
      print("Rock smashes scissors! You lose.")
  

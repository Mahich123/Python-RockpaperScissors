import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [rock, paper, scissors]
userChoice = int(input("What you choose ? Type 0 for rock , 1 for paper & 2 for scissors\n"))

print(images[userChoice])

computerChoice = random.randint(0,2)
print(f"Computer choosed {computerChoice}")
print(images[computerChoice])

if userChoice >= 3 and userChoice <= 0:
    print("Typed invalid number, Try again")
elif userChoice == 0 and computerChoice == 2: 
  print("You win")
elif computerChoice == 0 and userChoice == 2 :
  print("You loose ") 
elif computerChoice > userChoice:
  print("You loose")
elif userChoice > computerChoice :
  print("You win")
elif computerChoice == userChoice:
  print("It's a Draw")
#Section 4 (Conditional Code)- Challenge: Guessing Game
#conditions- If user enters name of favorite food- output "Yep! So amazing!"; 
# else- "Yuck! That's not it!"
# always output- "Thanks for playing!"

favoriteFood = "pizza"
guessFood = input("Guess my favorite food: ")
if guessFood == favoriteFood:
    print("Yep! So amazing!")
else:
    print("Yuck! That's not it!")
print("Thanks for playing!")


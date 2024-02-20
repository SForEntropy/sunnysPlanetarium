print ("Welcome to Sunny's Planetarium!")

name = input("Please enter your name: ") 
print("Welcome, " + name + "! Let's test your planetary knowledge.")
score = 0

q1 = input ("What is the name of our galaxy?  ")
if q1.lower() == "milky way":
    print("That's right")
    score  +=1
else:
    print("Incorrect. The correct answer is Milky Way.")

q2 = input ("Which planet is closest to the Sun?  ")
if q2.lower() == "mercury":
    print("That's correct. Well done.")
    score  +=1
else:
    print("Incorrect. The correct answer is Mercury.")

q3 = input ("Is Pluto a planet?  ")
if q3.lower() == "no":
    print("That's right.")
    score  +=1
else:
    print("Unfortunately, Pluto was stripped of its planetary status in 2006.")

q4 = input ("What is between Mars and Jupiter? Hint: it's not a planet.  ")
if q4.lower() == "asteroid belt":
    print("That's correct. Well done.")
    score  +=1
else: 
    print("Incorrect. The correct answer is Asteroid Belt.")

q5 = input ("Last question! How many rings does Venus have?  ")
if q5.lower() == "none" or q5.lower() == "zero" or int(q5) == 0:  
    print("That's right. Well done.")
    score  +=1
else:
    print("That was a trick question. Venus has no rings.")

print("All done. Your final score is... " + str(score) + " out of 5." )

if score == 5:
    print ("Congratulations! Top marks.")

elif score == 4:
    print ("Well done. That's a solid attempt.")

elif score == 3:
    print ("That's alright. Keep practising.")

elif score == 2:
    print("It's time for some revision.")

else:("There's room for improvement.")





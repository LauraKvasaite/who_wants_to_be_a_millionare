#Who wants to be a millionare?

score = 0

#Question 1:

option_1 = "1982"
option_2 = "1874"
option_3 = "1912"
option_4 = "1812"

print("When did the tragic sinking of the great ship Titanic occur?")

print("A.", option_1)
print("B.", option_2)
print("C.", option_3)
print("D.", option_4)

answer = input("What is your answer? ")
print(answer)


if (answer == "c" or answer == "C"):
    score += 100
    print("\nCorrect!")
else:
    print("\nNope, sorry..")

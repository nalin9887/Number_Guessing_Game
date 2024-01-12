import random
hardness = input("choose dificulity 'Hard' or 'Easy' : ").lower()
print("Guess a num Between 1 to 100")
attmpt = 0
if hardness == "hard":

    attmpt = 5
elif hardness == "easy":

    attmpt = 10
else:

    print("Invalid Input")


def guess(a, chosen_num):
    global attmpt
    global flag
    if chosen_num > a:
        print("AREE AREE😅ITAA ZZYDA BHI NAHI SOCHHH NAA THAAA BEEE KMM SOCHO!!  ")
        attmpt -= 1
    elif chosen_num < a:
        print("ZYDAA SOCHOO YARRR😫!!!!!!!! ")
        attmpt -= 1
    elif chosen_num == a:
        print("7 CRORR EKDUM SAHI JAVAB😎")
        flag = False


flag = True

num_toGuessed = random.randint(1,101)

while flag:

    
    
    guess_num = int(input("Enter Guessed Num : "))
    guess(num_toGuessed, guess_num)
    if attmpt == 0:
        flag = False
    print(f"{attmpt} life left")
  

    
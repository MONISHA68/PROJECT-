class quiz:
    def question1(self):
     print("You chose the hard difficulty")
     print("Where is the Great Victoria lake located?")
     answer1 = input("A) Canada   B)West Africa   C)Australia   D)North America")
     score=0
     if answer1 == "C":
         print("Correct")
         score = score+1
         print("Score:",score)
         return "Correct"
     else:
         print("you failed the quiz")
         print("Score:",score)
         return "wrong"
        
    def question2(self):
         print("Who is most responsible for cracking the Enigma Code")
         answer2 = input("A) Alan Turing   B) Jeff Bezos   C) George Boole   D) Charles   Babbage")
         score=0
         if answer2 == "A":
             print("Correct")
             score = score+1
             print("Score:",score)
             return "Correct"
         else: 
             print("you failed the quiz")
             print("Score:",score)
             return "wrong"

    def question3(self):
         print("The language spoken by the people in pakistan?")
         answer3 = input("A) Hindi  B)Palavan  C) Sindhi D) Nauruan")
         score=0
         if answer3 == "C":
             print("Correct")
             score = score+1
             print("Score:",score)
             return "Correct"
         else: 
             print("you failed the quiz")
             print("Score:",score)
             return "wrong"

    def question4(self):
         print("The Central Rice Research Station is situated in?")
         answer4 = input("A) Chennai   B) Cuttack  C) Bangalore  D) Quilon")
         score=0
         if answer4 == "B":
             print("Correct")
             score = score+1
             print("Score:",score)
             return "Correct"
         else: 
             print("you failed the quiz")
             print("Score:",score)
             return "wrong"

    def question5(self):
         print("Indian Constitution has been divided under")
         answer5 = input("A) 10 parts   B) 20 parts  C) 24 parts  D) 6 parts")
         score=0
         if answer5 == "C":
             print("Correct")
             score = score+1
             print("Score:",score)
             return "Correct"
         else: 
             print("you failed the quiz")
             print("Score:",score)
             return "wrong"




    def question6(self):
            print("You chose the easy difficulty")
            print("What is the capital of Australia?")
            answer6 = input("A) Canberra   B) Sydney   C)Melbourne")
            score=0
            if answer6 == "A":
                print("Correct")
                score = score+1
                print("Score:",score)
                return "Correct"
            else:
             print("you failed the quiz")
             print("Score:",score)
             return "wrong"
           
    def question7(self):
        print("When was the Great Fire of London?")
        answer7 = input("A) 1666   B) 1555   C)1605")
        score=0
        if answer7 == "A":
             print("Correct")
             score = score+1
             print("Score:",score)
             return "Correct"

        else:
             print("you failed the quiz")
             print("Score:",score)
             return "wrong"

    def question8(self):
         print("The first Governor General of India was?")
         answer8 = input("A) Rajaji   B)Lord Canning  C) Warren Hasting   D) Lord Mount Battern")
         score=0
         if answer8 == "C":
             print("Correct")
             score = score+1
             print("Score:",score)
             return "Correct"
         else: 
             print("you failed the quiz")
             print("Score:",score)
             return "wrong"

    def question9(self):
         print("Which channel won the Media For Sanitation-FICCI Awards 2017")
         answer9 = input("A) Zee News   B) NDTV   C) The Times Group   D) Star India")
         score=0
         if answer9 == "B":
             print("Correct")
             score = score+1
             print("Score:",score)
             return "Correct"
         else: 
             print("you failed the quiz")
             print("Score:",score)
             return "wrong"

    def question10(self):
         print("The First Indian President of India ")
         answer10 = input("A) Zakir Husain   B) Rajendra Prasad   C) Venkata Giri   D) A.P.J.Abdul Kalam")
         score=0
         if answer10 == "B":
             print("Correct")
             score = score+1
             print("Score:",score)
             return "Correct"
         else: 
             print("you failed the quiz")
             print("Score:",score)
             return "wrong"
            
x=quiz()
print("Welcome to the quiz")
print("enter your name")
name=input("")
print("enter the roll_no")
roll_no=input("")
print("press any key to take up the quiz")
start=input("")
print("Please choose a difficulty:")
difficulty = input("A) Hard   B)Easy")

if difficulty == "A":   
    ts=0
    ls=list()
    print(ls)
    ls.append(x.question1())    
    ls.append(x.question2())
    ls.append(x.question3())
    ls.append(x.question4())
    ls.append(x.question5())
    for i in range(0,5):
        print("question no %d is %s"%((i+1),ls[i]))
    ts=ls.count("Correct")
    print("the total mark is :")
    print(ts)
    score = float(ts / 5) * 100
    print(ts,"out of 5, that is",score,"%")

else:
    ts=0
    ls=list()
    print(ls)
    ls.append(x.question6())    
    ls.append(x.question7())
    ls.append(x.question8())
    ls.append(x.question9())
    ls.append(x.question10())
    for i in range(0,5):
        print("question no %d is %s"%((i+1),ls[i]))
    ts=ls.count("Correct")
    print("the total mark is :")
    print(ts)
    score = float(ts / 5) * 100
    print(ts,"out of 5, that is",score,"%")

score=int(input("請輸入英文成績:"))
grade=int(input("請輸入數學成績:")) 

if  (score >=0 and score <=100) and (grade >= 0 and grade <= 100):

    if grade>=90 and score >=90:
        print("獲得獎品")
            
    elif grade>=60 and score <=60:
        print("處罰")
    elif grade<=60 or score<60:
        print("處罰")  
else:        
    print("ERROR")
num = int (input("输入成绩:"))
if num>=90 and num<101:
    print("A")
elif num>79 and num<90:
    print("B")
elif num>69 and num<80:
    print("c")
elif num>59 and num<70:
    print("D")

else:

    print("F")

    print("：：：第二次成绩整理：：：")
    if(90<=num<=100):
        print("A")
    elif(num>=80 and num<=89):
        print("B")
    elif(num>=70 and num<=79):
        print("C")
    elif(num>=60 and num<=69):
        print("D")
    elif(num>=0 and num<=59):
        print("F")
    else :
        print("分数输入错误 ")


    print("：：：第三次成绩整理：：：")
    if 0<=num<=100:
        if num>89 and num<101:
           print("A")
        elif num>79 and num<90:
           print("B")
        elif num>69 and num<80:
           print("C")
        elif num>59 and num<70:
         print("D")
        else:
          print("F")

    else:
        print("输入错误")

    











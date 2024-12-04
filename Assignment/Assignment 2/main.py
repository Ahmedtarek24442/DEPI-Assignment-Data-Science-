import calc


print ("                   ////////////////////////////////")
print ("                  //                            //")
print ("                 //          Welcome           //")
print ("                //             To             //")
print ("               //          Calculator        //")
print ("              //                            //")
print ("             ////////////////////////////////")
print ("")
print ("")
string = ""
while string != "exit" and string != "EXIT" and string != "Exit":
    n1 = input ("Enter a first number: ")
    op = input("Enter comand (add,sub,mult,div): ")
    n2 = input ("Enter a second number: ")
    if op == 'add': print(n1," + ",n2," = ",calc.add(int(n1),int(n2)))
    elif op == 'sub': print(n1," + ",n2," = ",calc.sub(int(n1),int(n2)))
    elif op == 'mult': print(n1," + ",n2," = ",calc.mult(int(n1),int(n2)))
    elif op == 'div': print(n1," + ",n2," = ",calc.div(int(n1),int(n2)))
    else : print("Enter a valid operator ")

    string = input("if you finish type 'Exit' : ")
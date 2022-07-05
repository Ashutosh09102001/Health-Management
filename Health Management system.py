a = int(input("Do you want to log an entry or retrieve entries \n press 1 to log or 2 to retrieve :"))
n1 = int(input("press 1 for Execersies and 2 for food"))
n2 = int(input("Press 1 for Harry, Press 2 for Rohan and 3 for mohammed"))


def getdate():
    import datetime
    return datetime.datetime.now()

if a ==1 :
    if n1==1 and n2==1 :
        f= open("harrye","a")
        inp =input("Enter the execerses performed by harry \n ")
        time = str(getdate())
        f.write(inp+ "[" + time + "]" +"\n")
        f.close()
    elif n1==2 and n2==1:
        f1=open("harryf","a")
        inp1=input("Enter the meals taken by harry \n")
        time = str(getdate())
        f1.write(inp1+ "[" + time+ "]" +"\n")
        f1.close()
    elif n1==1 and n2==2:
        f3=open("rohane","a")
        inp2=input("Enter the exercises done by rohan \n")
        time = str(getdate())
        f3.write(inp2+ "[" + time + "]" +"\n")
        f3.close()
    elif n1==2 and n2==2:
        f4=open("rohanf","a")
        inp3=input("Enter the  meals taken by rohan \n")
        time = str(getdate())
        f4.write(inp3+ "[" + time + "]" +"\n")
        f4.close()
    elif n1==1 and n2==3:
        f5=open("hammade","a")
        inp4=input("Enter the exercises done by hammad \n")
        time = str(getdate())
        f5.write(inp4+ "[" + time + "]" +"\n")
        f5.close()
    elif n1==2 and n2==3:
        f6=open("hammadf","a")
        inp5=input("Enter the meals taken by hammad \n")
        time = str(getdate())
        f6.write(inp5+ "[" + time + "]" +"\n")
        f6.close()
    else:
        print("enter valid details")
if a==2:
    if n1==1 and n2==1:
        f=open("harrye","rt")
        print(f.read())
        f.close()
    elif n1==2 and n2==1:
        f1=open("harryf")
        print(f1.read())
        f1.close()
    elif n1==1 and n2==2:
        f2=open("rohane")
        print(f2.read())
        f2.close()
    elif n1==2 and n2==2:
        f3=open("rohanf")
        print(f3.read())
        f3.close()
    elif n1==1 and n2==3:
        f4=open("hammade")
        print(f4.read())
        f4.close()
    elif n1==2and n2==3:
        f5=open("hammadf")
        print(f5.read())
        f5.close()
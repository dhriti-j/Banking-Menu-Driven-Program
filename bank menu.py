import csv
f= open("Bank.csv", "r")

accountslist= []
reader= csv.reader(f, delimiter= ",")

for row in reader:
        
        row0= int(row[0])
        row1= row[1]
        row2=int(row[2])
        accountslist.append([row0,row1,row2])
f.close()

        

def search():
    f= open("Bank.csv", "r")
    reader= csv.reader(f, delimiter= ",")
    acc= int(input("Enter account no: "))
    count= 0
    for row in reader:
        
        if int(row[0])== acc :
            
            print(row[0], "\t", row[1],'\t', row[2])
            count= count +1
    if count== 0:
        print("Account not found")
    f.close()
         


def display():
    f= open("Bank.csv", "r")
    reader= csv.reader(f, delimiter= ",")
    
    for row in reader:
        print(row[0], "\t", row[1], "\t", row[2])
    f.close()

        

def transaction():
    print("HANDLE TRANSACTIONS")
    print("1- Deposit money")
    print("2- Withdraw money")
    n= int(input("Enter choice: "))
    acc= int(input("Enter account no. : "))
    

    if n==1:
        count=0
        dep= int(input("Enter amount to deposit : "))
        
        count= count+1
        
        for j in range(len(accountslist)):    
         if accountslist[j][0] == acc:
                
                count= count+1
                f=open("Bank.csv", "w", newline="")
                writer= csv.writer(f, delimiter= ",")
                for i in range(len(accountslist)):
                 if accountslist[i][0]!= acc:
                    writer.writerow(accountslist[i])
                 else:
                    
                    accountslist[i][2]= accountslist[i][2]+ dep
                    writer.writerow(accountslist[i])
                    print("Amount deposited")
                    print("Record is " ,accountslist[i])
                f.close()
        if count==0:
                print("Account not found")
        
            

            

        
                
    if n==2:
        count=0
        for j in range(len(accountslist)):
            if accountslist[j][0]==acc:
                count=count+1
                
                
                f=open("Bank.csv", "w", newline="")
                writer= csv.writer(f, delimiter= ",")
                for i in range(len(accountslist)):
                 if accountslist[i][0]!= acc:
                    writer.writerow(accountslist[i])
                 else:
                    withdraw= int(input("Enter amount to withdraw: "))
                    if (accountslist[i][2]-withdraw)>= 1000:
                        accountslist[i][2]=accountslist[i][2]-withdraw
                        writer.writerow(accountslist[i])
                        print("Amount withdrawn")
                    else:
                        writer.writerow(accountslist[i])
                        print("Account only has ", accountslist[i][2], ".Can't withdraw")

        if count==0:
            print("Account not found")
        f.close()
             
                        
def insert():
 while True:
        f= open("Bank.csv", "a", newline= "")
        acc= int(input("Enter account number: "))
        name= input("Enter name of holder: ")
        bal= int(input("Enter balance: "))
        writer= csv.writer(f, delimiter= ",")
        writer.writerow([acc,name,bal])
        
        ans=input("Do you want to enter more records? (y/n)")
        if ans== "n":
               break
        print("Record ")

def modify():
        count=0
        acc=int(input("Enter account to modify: "))
        for j in range(len(accountslist)):
                if accountslist[j][0]== acc:
                        count= count+1
                        f=open("Bank.csv", "w", newline="")
                        writer= csv.writer(f, delimiter= ",")
                        for i in range (len(accountslist)):
                                if accountslist[i][0] != acc:
                                        writer.writerow(accountslist[i])
                                else:
                                     while True:  
                                       print("1- Acc no")
                                       print("2- Name of account holder")
                                       print("3- Balance in account")
                                       ch= int(input("Choose what you want to modify"))
                                       

                                       if ch==1:
                                               acc_new= int(input("Enter new account number: "))
                                               accountslist[i][0]= acc_new
                                               writer.writerow(accountslist[i])
                                               print("Account no. changed")
                                               ans=input("Do you want to change something else? (y/n)")
                                               if ans== "n":
                                                            break
                                       elif ch ==2:
                                                  
                                                  name_new= input("Enter new name: ")
                                                  accountslist[i][1]= name_new
                                                  writer.writerow(accountslist[i])
                                                  print("Account name changed")
                                                  ans=input("Do you want to change something else? (y/n)")
                                                  if ans== "n":
                                                            break

                                       elif ch ==3:
                                                  bal_new= int(input("Enter new balance: "))
                                                  accountslist[i][2]= bal_new
                                                  writer.writerow(accountslist[i])
                                                  print("Account balance changed")
                                                  ans=input("Do you want to change something else? (y/n)")
                                                  if ans== "y":
                                                            break

                                       else:
                                                 print("Wrong choice entered")

                        f.close()

                                                
                                       
        if count ==0:
                  print("Account not found")
          
                                        
        


while True:
 print("BANK ")
 print("1- Search record ")
 print("2- display all records")
 print("3- Do transactions")
 print("4-Update records")
 print("5- Modify existing record")
 n= int(input("Enter choice: "))
 if n==1: search()
 elif n==2: display()
 elif n==3: transaction()
 elif n==4: insert()
 elif n==5: modify()
 else: print("Wrong choice")
 ans=input("Do you want to exit this menu? (y/n)")
 if ans== "y":
        break



    
        
        

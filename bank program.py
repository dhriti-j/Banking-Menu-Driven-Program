import csv
f= open("Bank.csv", "w", newline= "")
writer= csv.writer(f, delimiter= ",")
while True:
    no=int(input("Enter account no: "))
    name= input("Enter name: ")
    bal=int(input("Enter balance: "))
    writer.writerow([no,name,bal])
    ans= input("Do you want to enter more records? (y/n): ")
    if ans=="n":
        break
    print("Entered all records")
f.close()

    

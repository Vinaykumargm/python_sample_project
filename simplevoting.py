import list1
import sys
import random
from collections import Counter
votes={} 
#list1.acc()
print("-----Welcome to VV Voting Management System----- ")
cho=0
ls1=[]
flag=0
winners=[]
def voting():
    print("----Welcome to Voting part----")
    print("---Before that lets look at the parties totally present--")
    b=len(ls1)
    for x in ls1:
        print(f"{x}")
    for x,y in list1.li.items():
        print(f"{y} : Choose one party to votes:(based on number assigned to it) ")
        for i,j in enumerate(ls1,1):
            print(f"{i}. {j}")
        while True:
            pc=input("Enter your  choice: ")
            if not pc.isdigit():
                print("Enter only numbers:)")
                continue
            pc=int(pc)
            if pc>b:
                print("Enter the choice correctly!!!!!!!!")
                continue
            break
        votes[x]=ls1[pc-1]
while cho!=4:
    print("\n1.Enter No of parties \n2.conduct Elections \n3.Check Results \n4.Quit")
    ch=input()
    if not ch.isdigit():
        print("Enter only numbers:)")
        continue
    ch=int(ch)
    if ch==2 and flag==0:
        print("select number of parties and name them to conduct elections:)")
    if ch==1:
        flag=1
        n=input("Enter no of parties: ")
        if not n.isdigit():
            print("Enter only numbers:)")
            continue
        n=int(n)
        print("Enter party names:")
        while n!=0:
            partn=input()
            ls1.append(partn)
            n-=1
        print("party names are: ")
        for x in ls1:
            print(f"{x}")
        #global Y,N
        while True:
            print("do u want to delete any parties?(1/0)")
            ch1=input("Enter only  (1-To delete/0-not delete): ")
            if not ch1.isdigit():
                print("Enter only numbers:)")
                continue
            ch1=int(ch1)
            break
        if ch1==1:
            par=input("Enter party name to delete: ")
            if par in ls1:
                ls1.remove(par)
                print("party names are: ")
                for x in ls1:
                    print(f"{x}")
            else:
                print("u entered party is not present:)")
        elif ch1==0:
            print("party names are: ")
            for x in ls1:
                print(f"{x}")
        else:
            print("Enter only (1/0)")
    elif ch==2 and flag==1:
        voting()
        vc = Counter(votes.values())
        mv = max(vc.values())
        winners = [p for p, c in vc.items() if c == mv]
    elif ch == 3 and flag==1:
        print("\nElection Results:")
        if len(winners)==1:
            print(f"The winner is {winners[0]} with {mv} votes!!!!")
        else:
            print("Result is tied.......(Election is reconsidered):")
            votes.clear()
            voting()
    elif ch==4:
        sys.exit()
    

        
            
        
   


import fs
import sys
class det():
    def start(self):
        ch=0
        se={1:"movieTicketBooking.txt",
            2:"DmartBilling.txt",
            3:"SmartBanking.txt",
            4:"FoodOrderingManagement.txt",
            5:"VotingManagement.txt"}
        print("--Welcome to git repository--")
        while ch!=3:
            i=input("1.Login\n2.Create account\n3.Exit\nSelect your choice : ")
            if not i.isdigit():
                print("Enter only numbers:)")
                continue
            i=int(i)
            if i==1:
                s=input("Enter name : ")
                if s in fs.di:
                    f=fs.di.get(s)
                    pa=input("Enter password : ")
                    if pa==f:
                        print("login sucessfully..")
                        print(f"--Welcome {s} to git repository")
                        while True:
                            s1=input("\n1.To check available projects\n2.To get source code\n3.To delete projects\n4.To go back\nSelect your choice : ")
                            if not s1.isdigit():
                                print("Enter only numbers:)")
                                continue
                            s1=int(s1)
                            if s1==1:
                                print("---Available projects are---")
                                print("{:<10} {:<10}".format("slno","projects"))
                                for x,y in se.items():
                                    print("{:<10} {:<10}".format(x,y))
                            elif s1==2:
                                print("---Available projects are---")
                                print("{:<10} {:<10}".format("slno","projects"))
                                for x,y in se.items():
                                    print("{:<10} {:<10}".format(x,y))
                                c=input("\nSelect projects based on number to it : ")
                                if not c.isdigit():
                                    print("Enter only numbers:)")
                                    continue
                                c=int(c)
                                f1=open(se.get(c),"r")
                                li=f1.readline()
                                while(li!=""):
                                    print(li)
                                    li=f1.readline()
                                f1.close()
                                #if c<=len(se):
                                    
                                #else:
                                    #print(f"projects are only {c}")
                            elif s1==3:
                                print("{:<10} {:<10}".format("slno","projects"))
                                for x,y in se.items():
                                    print("{:<10} {:<10}".format(x,y))
                                de=input("Do you want to delete any project. enter number of it : ")
                                if not de.isdigit():
                                    print("Enter only numbers:)")
                                    continue
                                de=int(de)
                                if de>=1 and de<=5:
                                    print(f"you deleted {se.get(de)}")
                                    se.pop(de)
                                else:
                                    print("Projects list are in the range(1-5)")
                                
                            elif s1==4:
                                break
                            else:
                                print("Enter correct choice:)")
                    else:
                        print("incorrect password!!")
                    
                else:
                    print("create account first!")
            elif i==2:
                name=input("Enter name :")
                passw=input("create password: ")
                conf=input("confirm password:")
                if passw == conf:
                    print("Account created sucessfully...")
                    fs.di.update({name:conf})
                else:
                    print("Enter correct password:")
            elif i==3:
                sys.exit()
            else:
                print("Enter correct choice:)")
o=det()
o.start()
            
                    
        

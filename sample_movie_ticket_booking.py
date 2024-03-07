# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 12:21:37 2023
@author: Admin
"""
import mov
import sys
ls=[]
cho=0
fl=0
print("\n-----Welcome to Vk movie Booking system-----")
def ml():
    print("\n---Welcome to Movie Booking---\n")
    print("{:<17} {:<17} {:<17}".format("MOVIES","RATINGS","INTERESTS"))
    print("{:17} {:17} {:<17}".format("Leo","7.9","300k"))
    print("{:17} {:17} {:<17}".format("Ghost","8.25","800k"))
    print("{:17} {:17} {:<17}".format("Vikrant-rona","8.9","1.2M"))
    print("{:17} {:17} {:<17}".format("Baby","8.5","250k"))
    print("{:17} {:17} {:<17}".format("SSE(side-B)","9.6","900k"))
while cho!=4:
    sel=input("\n1.See movies List\n2.Book a ticket\n3.view ticket status\n4.Exit: ")
    if not sel.isdigit():
        print("Enter only numbers:)")
        continue
    sel=int(sel)
    if sel==3 and fl==0:
        print("Please book a movie before viewing ticket status:)")
    elif sel==1:
        ml()
        fl=0
    elif sel==2:
        fl=1
        ml()
        ch=input("\nChosse your movie..(Enter correct movie name): ")
        if ch in mov.movie:
            md=mov.movie[ch]
            lang=md["language"]
            gene=md["Genre"]
            dur=md["Duration"]
            cas=md["Cast"]
            dire=md["Director"]
            print("-----you choose-----")
            print(f"\nMovie: {ch}\n")
            print(f"Language : {lang}")
            print(f"Genre: {gene}")
            print(f"Duration: {dur}")
            print(f"Cast {cas}")
            print(f"Director: {dire}")
            avail={"Leo":{"Total":"180","Best":"44","sold":"70","available":"66"},

            "Ghost":{"Total":"190","Best":"51","sold":"36","available":"103"},

            "Vikrant-rona":{"Total":"180","Best":"63","sold":"80","available":"37"},

            "Baby":{"Total":"170","Best":"48","sold":"40","available":"82"},
            "SSE(side-B)":{"Total":"170","Best":"48","sold":"40","available":"82"}
            }

            print("---AVAILABILITY---\n")

            sel = avail[ch]

            total= sel["Total"]

            best=sel["Best"]

            sold=sel["sold"]

            available= int(sel["available"])

            print(f"Total seats: {total}")

            print(f"Best sellers: {best}")

            print(f"Sold: {sold}")

            print(f"Available seats: {available}\n")
            
            while True:
                x=input("How many tickets do you want?")
                if not x.isdigit():
                    print("Enter only numbers:)")
                    continue
                x=int(x)
                break
            if x>0:   
                if x<available:
                    nam=input("Enter your name: ")
                    phno=input("Enter your phno: ")
                    ls.append(phno)
                    print(f"\nCongrats....Enjoy the show!--{x} Tickets confirmed")
                    print(f"you booked {x} seats")
                    print(f"\nMovie: {ch}\n")
                    print(f"Language : {lang}")
                    print(f"Genre: {gene}")
                    print(f"Duration: {dur}")
                    print(f"Cast {cas}")
                    print(f"Director: {dire}")
                    available-=x
                    print("Available Seats are: ",available)
                else:
                    print(f"\n Sorry! {x}  Tickets are not available. please rebook by seeing available seats:)")
            else:
                print("No tickets have been choosen :)")
        else:
            print("Sorry...you Entered movie is not available now...")
    elif sel==3 and fl==1:
        pno=input("Enter phone number to check ur Ticket status:)")
        if pno in ls:
            print(f"you booked {x} seats")
            print(f"\nMovie: {ch}\n")
            print(f"Language : {lang}")
            print(f"Genre: {gene}")
            print(f"Duration: {dur}")
            print(f"Cast {cas}")
            print(f"Director: {dire}")
        else:
            print("Sorry...No tickets are booked from this Number:)")
    elif sel==4:
        sys.exit()
    else:
        print("please Enter correct choice...")
        

    


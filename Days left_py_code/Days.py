#Code tells you days left in the year after the date you entered
dt=int(input("date of the month :-"))
mnt=int(input("Enter month in integer form ie. january is 1, feb is 2 :-"))
yr=int(input("Enter which year you are in :- "))
day=0
def lp_yr(yr): # function to chck leap year
    if(yr%100==0 and (yr/100)%4==0):
        return 1
    elif(yr%4==0 and yr%100!=0):
        return 1
        
    else:
        return 0
def cheq( dt,  mnt ,lp=1): #function for validation of date
    if((mnt==1 or mnt==3 or mnt==5 or mnt==7 or mnt==8 or mnt==10 or mnt==12) and dt<=31 and dt>=1):
            
            return 31
    elif((mnt==4  or mnt==6 or mnt==9 or mnt==11) and dt<=30 and dt>=1):
            
            return 30
    elif((mnt==2)and (dt<=28 and dt>=1 and lp==0)):
            return 28
    elif((mnt==2)and (dt<=29 and dt>=1 and lp==1)):
           return 29
    else:
            return 0
    
a=cheq(dt ,mnt,lp_yr(yr))
if(a!=0):
    for i in range(dt+1,a+1):
        day=day+1
    for j in range(mnt+1,13):
        day+=cheq(1,j,lp_yr(yr))
        
    print("Number of days remaining are :",day)

else:
    print("Enter data correctly")
    
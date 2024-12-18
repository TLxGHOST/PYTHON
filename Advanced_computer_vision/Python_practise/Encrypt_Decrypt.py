
from random import randint
def Encrypt(str):
    '''This function encryptes a message which is passed as a string to it 
    basic rules of Encryption are:
    1. If the word has only two characters it will be reversed 
    2.If the word contains more than two characters first two characters will be appended to the end and 3 extra characters will be added to both sides'''
    
    encrypted=" "
    str.rstrip()
    str.lstrip()
    lst=str.split()
    load=["-","-","-","-","-","-","-","-"]
    for i in lst:
        count=0
        for j in i:
            count=count+1
        if(count>2):
            frst_two=i[0:2]
            i=i.strip(frst_two)
            i=chr(randint(97,122))+chr(randint(97,122))+chr(randint(97,122))+i
            encrypted=encrypted+i+frst_two+chr(randint(97,122))+chr(randint(97,122))+chr(randint(97,122))+" "
        else:
            encrypted=encrypted+i[::-1]+" "
        
            print(f"{load}")
            
    return (encrypted)


          




def Decrytp(str):
    '''This code is just to decrypt the message you entered The text rules of encrypton are '''
    decrypted=""

    lst=str.split()
    for i in lst:
        count=0
        for j in i:
            count=count+1
        if (count>2):
        # i.lstrip(" ")
        # i.rstrip(" ")
            frst_three=i[0:3]
            lst_three=i[-1:-4:-1]
            i=i.lstrip(frst_three)
            i=i.rstrip(lst_three)
            jumbled_two=i[-1:-3:-1]
            i=i.rstrip(jumbled_two)
            decrypted=decrypted+jumbled_two[1]+jumbled_two[0]+i+" "
        else:
            decrypted=decrypted+i[::-1]+" "
            
    return (decrypted)




def main():
    print("HEllo user to encrypt talk \n ENter 1 to encrypt a message and press 2 to decrypt a message ")
    while True:
        a=int(input("Ente Choice"))
        if(a==1):
            s=input("Enter a string  to encode")
            print(Encrypt(s))
        elif(a==2):
           s=input("Enter a Encrypted message ")
           print(Decrytp(s))
        else:
            print("thank you for using !")
            break

if __name__=="main":
    main() 
    
    
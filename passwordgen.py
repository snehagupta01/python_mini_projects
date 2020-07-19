import string
import random

def generate():
    s1=string.ascii_lowercase
    # print(s1)
    s2=string.ascii_uppercase
    # print(s2)
    s3=string.digits
    # print(s3)
    s4=string.punctuation
    # print(s4)
    
    passwrdlen=int(input("Enter the password length : \n"))
    s=[]
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)

    # print(s)

    random.shuffle(s)

    res=("".join(s[0:passwrdlen]))

    print(res)

generate()
import json
import os
print("WELCOME IN LOGIN AND SIGNUP PAGE!")
def signup(p):
    if p>"a" or p<"z" and p>"A" or p<"Z" and p.isdigit():
        print(())
    else:
        print("min length is 6")
        p=input("Enter your password:")
        signup(p)
def cp(p,p1):
    if p==p1:
        print("correct")
    else:
        print("your confirm password is not match with password.")
        p1=input("Enter your confirm password:")
user=input("what you want to do login or signup:")
file=os.path.exists("signup.json")
if file ==False:
    if user=="signup":
        n=input("Enter your name:")
        p=input("Enter your password:")
        p1=input("Enter your confirm password:")
        print("congrats",n,"you signed up successfully")
        dob=input("Enter your dob")
        h=input("Enter your hoobies:")
        g=input("Enter your gender male or female:")
        d=input("Enter your description:")
        l=[]
        dic={}
        n1=["name","password","dob","hobby","gender","description"]
        info=[n,p,dob,h,g,d]
        for i in range(len(n1)):
            dic.update({n1[i]:info[i]})
        l.append(dic)
        with open("signup.json","a") as f:
            json.dump(l,f,indent=2)
elif file==True:
    if user=="signup":
        n=input("Enter your name:")
        p=input("Enter your password:")
        p1=input("Enter your confirm password:")
        r=open("signup.json","r")
        n2=r.read()
        if n in n2:
            print("name is already exists")
        else:
            print("congrats",n,"you are signed up successfully")
            dob=input("Enter your dob:")
            h=input("Enter your hobby:")
            g=input("Enter your gender:")
            d=input("Enter your description:")
            dic={}
            data=[]
            n1=["name","password","dob","hobby","gender","description"]
            info=[n,p,dob,h,g,d]
            for i in range(len(n1)):
                dic.update({n1[i]:info[i]})
            with open("signup.json","r") as f:
                data=json.load(f)
            data.append(dic)
            with open("signup.json","w") as f:
                json.dump(data,f,indent=2)
    elif user=="login":
        u=input("Enter your name :")
        u1=input("Enter your password:")
        with open("signup.json","r") as f:
            da=json.load(f)
            for i in range(len(da)): 
                if da[i]["name"]==u:
                    if da[i]["password"]==u1:
                        print("login successfully")
                        for x,y in da[i].items():
                            print(x,'=',y)    
                    else:
                        print("this name is not exist in this file.")
                        break



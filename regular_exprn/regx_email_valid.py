import re
while True:
    email=input("enter email address : ")
    user_inputs=input("enter yes/no : ").lower()
    email_patten=r"[a-zA-Z0-9]+(|[0-9]+)@[a-z]+\.(in|com)"
    res=re.match(email_patten,email)
    if user_inputs=='yes':
        if res:
            out=res.group()
            fw=open("email_data","a")
            fw.write(out+"\n")
            print("Email is valid and saved.")
        else:
            print("Invalid email address. Please try again.")


    elif user_inputs=='no':
        fr = open("email_data", "r")
        print(fr.read())





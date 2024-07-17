import re

user_email = input("Enter Email address: ").strip()

if re.search(".+@.+[.].+",user_email):
    print("Valid")

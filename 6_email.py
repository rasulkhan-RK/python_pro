user_input = input("Enter your email: ").lower()
email_validation = ''.join(user_input.split())
email = email_validation
invaild_email = False

if len(email) >=6:
  if email[0].isalpha():
    if(("@" in email) and (email.count("@") == 1)):
      if(email[-4] == ".") or (email[-3] == "."):
         print(f"Valid Email {email}")
      else:
        print("Invalid Email_4")
    else:
      print("Invalid Email_3")
  else:
    print("Invalid Email_2")
else:
  print("Please enter valid Email_1")
#Email Validation using RegEx
import re
email_characters =r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,}$'
user_email = input("Enter your email: ").lower()

if re.match(email_characters, user_email):
  print(f"Right Email: {user_email}")
else:
  print("Wrong Email")
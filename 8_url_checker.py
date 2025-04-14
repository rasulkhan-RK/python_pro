print("URL Checker")
url_checker = input("Please enter a website: ").lower()

if url_checker.startswith("https://"):
    print("This website use HTTPS (secure!)")
elif url_checker.startswith("http://"):
    print("This website use HTTP (not secure!)")
else:
    print("Invalid Url Please enter valid url")

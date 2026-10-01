Username = input("ENTER USERNAME")
Password = input("ENTER PASSWORD")

if (Username == "admin" and Password == "Pass"):
    print("lOGIN")

elif (Username != "admin"):
    print("Incorrect Username")
elif (Password != "Pass"):
    print("Incorrect Password")

else:
    print("Incorrect Username and Password")
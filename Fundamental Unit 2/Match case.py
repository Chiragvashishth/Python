color=input("Enter Color:")

match color:
    case "Green":
        print("GO")
    case "RED":
        print("Stop")
    case _:
        print("Wrong color")
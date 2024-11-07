command =""
while True:
    command = input("> ").lower()
    if command == "start ":
        print("Car is Started....")
    elif command == "Stop ":
        print("Car is stoped....")
    elif command == "help ":
        print("""
        Start - To start the car
        Stop  - To stop the car
        quit  -  To quit the game
         """)
    elif command == "quit ":
        break
    else:
        print("sorry i dont understand")


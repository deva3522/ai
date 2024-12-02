def vc(room, status):
    print(f"{room} is {status}")
    if status == 'dirty':
        print("Cleaning Room !!!")

status1 = input("Enter Status of room 1: ")
vc("room1", status1)
status2 = input("Enter Status of room 2: ")
vc("room2", status2)
print("Vacuum Cleaner Function Completed")

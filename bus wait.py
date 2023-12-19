import time
while True:
    print("Still waiting for the bus...")
    user_input = input("Has the bus arrived? (yes/no): ").strip().lower()
    
    if user_input == "yes":
        print("You can now board the bus.")
        break
    elif user_input == "no":
        continue
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

    time.sleep(10)
numbers = []
print("Typing 'done' will exit the program.")
while True:
    user_input = input("Please enter an integer: ")

    if user_input == 'done':
        break

    try:
        number = int(user_input)
        numbers.append(number)
        average = sum(numbers) / len(numbers)
        print(f"{numbers} , average = {average:.2f}")
        
    except ValueError:
        print("Invalid input! Enter again.")

print("---------- Bye !! -----------")

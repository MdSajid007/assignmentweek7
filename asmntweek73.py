sender_num = 0

with open("mbox.txt", "r") as file:

    for line in file:

        if line.startswith("From "):
            words = line.split()

            if len(words) >= 2:
                print(words[1])
                sender_num += 1

print(f"\nTotal {sender_num} lines were printed")

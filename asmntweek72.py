u_word = []

with open("romeo.txt", "r") as file:
    for line in file :
        words = line.split()

        
        for word in words:
            if word not in u_word:
                u_word.append(word)


u_word.sort()
print(u_word)

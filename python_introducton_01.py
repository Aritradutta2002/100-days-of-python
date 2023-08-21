name1 = input("What is your name: ")
name2 = input("What is their name: ")
name1 = name1.lower()
name2 = name2.lower()
names = name1 + name2
count1 = 0
true = names.count("t") + names.count("r") + names.count("u") + names.count("e")
love = names.count("l") + names.count("o") + names.count("v") + names.count("e")
true_love = int(str(true) + str(love))
print(f"You love is {true_love}")


